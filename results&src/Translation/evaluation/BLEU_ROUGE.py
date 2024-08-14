import os
import json
from typing import List, Dict, Any, Union
import pycantonese
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_metric import PyRouge
import pandas as pd

def ensure_string(text: Union[str, List[str]]) -> str:
    if isinstance(text, list):
        return ' '.join(map(str, text))
    return str(text)

def tokenize_cantonese(text: str) -> List[str]:
    return list(pycantonese.segment(text))

def calculate_bleu(reference_texts: List[str], candidate_text: str) -> float:
    if not candidate_text:
        return 0
    references = [tokenize_cantonese(text) for text in reference_texts]
    candidate = tokenize_cantonese(candidate_text)
    smooth = SmoothingFunction().method7
    return sentence_bleu(references, candidate, smoothing_function=smooth)

def calculate_rouge(prediction: str, references: List[str]) -> Dict[str, Dict[str, float]]:
    rouge = PyRouge(rouge_n=(1, 2, 3, 4), rouge_l=True, rouge_w=True, rouge_s=True, rouge_su=True, skip_gap=4)
    if not prediction:
        return {metric: {'r': 0, 'p': 0, 'f': 0} for metric in ['rouge-1', 'rouge-2', 'rouge-3', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']}
    tokenized_prediction = tokenize_cantonese(prediction)
    tokenized_references = [tokenize_cantonese(ref) for ref in references]
    return rouge.evaluate_tokenized([tokenized_prediction], [tokenized_references])

def process_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_bleu = 0
    total_rouge_scores: Dict[str, Dict[str, float]] = {}

    for key, value in data.items():
        prediction = ensure_string(value.get('prediction', ''))
        gold = value['gold']

        bleu_score = calculate_bleu([gold], prediction)
        rouge_scores = calculate_rouge(prediction, [gold])

        # Add scores to the original data
        value['evaluation'] = {
            'bleu': bleu_score,
            'rouge': rouge_scores
        }

        total_bleu += bleu_score
        for metric, scores in rouge_scores.items():
            if metric not in total_rouge_scores:
                total_rouge_scores[metric] = {'r': 0, 'p': 0, 'f': 0}
            for score_type in ['r', 'p', 'f']:
                total_rouge_scores[metric][score_type] += scores[score_type]

    num_items = len(data)
    avg_results = {
        'bleu': total_bleu / num_items,
        'rouge': {metric: {key: value[key] / num_items for key in value}
                  for metric, value in total_rouge_scores.items()}
    }

    return {'data': data, 'avg_results': avg_results}

def main(input_path: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)

    results = {}

    for model_name in os.listdir(input_path):
        model_path = os.path.join(input_path, model_name)
        if os.path.isdir(model_path):
            results[model_name] = {'en-yue': {'0-shot': {}, '5-shot': {}}, 'zh-yue': {'0-shot': {}, '5-shot': {}}}
            for file_name in os.listdir(model_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(model_path, file_name)
                    translation_type = 'en-yue' if 'en-yue' in file_name else 'zh-yue'
                    shot_type = '0-shot' if '0shot' in file_name else '5-shot'

                    print(f"Processing {model_name} - {translation_type} - {shot_type}")

                    try:
                        file_results = process_file(file_path)
                        results[model_name][translation_type][shot_type] = file_results['avg_results']

                        # Save detailed results
                        output_dir = os.path.join(output_path, model_name)
                        os.makedirs(output_dir, exist_ok=True)
                        output_file = os.path.join(output_dir, f"{translation_type}_{shot_type}_evaluated.json")
                        with open(output_file, 'w', encoding='utf-8') as f:
                            json.dump(file_results['data'], f, ensure_ascii=False, indent=2)

                    except Exception as e:
                        print(f"Error processing {file_path}: {str(e)}")

    # Generate CSV report
    csv_data = []
    header = ['Model', 'Translation Type', 'Shot Type', 'BLEU']
    for metric in ['rouge-1', 'rouge-2', 'rouge-3', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']:
        for score_type in ['f', 'p', 'r']:
            header.append(f'{metric}-{score_type}')

    csv_data.append(header)

    for model, model_results in results.items():
        for translation_type in ['en-yue', 'zh-yue']:
            for shot_type in ['0-shot', '5-shot']:
                scores = model_results[translation_type][shot_type]
                row = [model, translation_type, shot_type, f"{scores['bleu']:.4f}"]
                for metric in ['rouge-1', 'rouge-2', 'rouge-3', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']:
                    for score_type in ['f', 'p', 'r']:
                        value = scores['rouge'].get(metric, {}).get(score_type, 0)
                        row.append(f'{value:.4f}')
                csv_data.append(row)

    df = pd.DataFrame(csv_data[1:], columns=csv_data[0])
    csv_file_path = os.path.join(output_path, 'BLEU_ROUGE_scores.csv')
    df.to_csv(csv_file_path, index=False)

    print(f"Evaluation scores have been saved to {csv_file_path}")

if __name__ == "__main__":
    input_path = '../prediction'
    output_path = './'
    main(input_path, output_path)