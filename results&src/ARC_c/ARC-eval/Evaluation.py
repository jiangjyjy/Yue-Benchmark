import json
import os
import re
import csv
from typing import List, Dict
from collections import defaultdict
import Levenshtein

def extract_answer(text: str, options: str = 'ABCD', choices: List[str] = None) -> str:
    """
    Extracts the answer options from the generated text using a more flexible approach.
    If direct extraction fails, it falls back to a similarity-based fallback mechanism.
    """
    if not text:
        return ''
    # 1. Directly match single letter answers
    direct_match = re.search(rf'\b([{options}])\b', text)
    if direct_match:
        return direct_match.group(1)

    # 2. Look for sentences that contain keywords such as "answer", "response", etc
    answer_sentence = re.search(r'(答案|回應|選擇|答)[:：是為]?\s*([^。\n]+)', text)
    if answer_sentence:
        option_in_sentence = re.search(rf'\b([{options}])\b', answer_sentence.group(2))
        if option_in_sentence:
            return option_in_sentence.group(1)

    # 3. Look for options in the format "A.", "B.", etc
    formatted_option = re.search(rf'\b([{options}])\.\s*', text)
    if formatted_option:
        return formatted_option.group(1)

    # 4. Look for the last option letter that appears
    all_options = re.findall(rf'\b([{options}])\b', text)
    if all_options:
        return all_options[-1]

    # 5. If the text is short, return the first matching letter directly
    if len(text) <= 5:
        match = re.search(rf'([{options}])', text)
        if match:
            return match.group(1)

    
    # 6. If all else fails, use a fallback mechanism based on similarity
    if choices:
        try:
            similarities = [Levenshtein.ratio(text.lower(), choice.lower()) for choice in choices]
            max_similarity_index = similarities.index(max(similarities))
            return options[max_similarity_index]
        except Exception as e:
            print(f"Error in similarity calculation: {e}")
            print(f"Text: {text}")
            print(f"Choices: {choices}")
            return ''

    # 7. If no options are provided, return an empty string
    return ''

def calculate_accuracy(predictions: List[str], references: List[str]) -> float:
    """
    计算准确率。
    """
    correct = sum(p == r for p, r in zip(predictions, references))
    return (correct / len(references)) * 100 if references else 0

def process_file(file_path: str) -> Dict[str, List[Dict]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = []

    for idx, item in data.items():
        if isinstance(item['prediction'], list):
            pred_text = item['prediction'][0]
        else:
            pred_text = item['prediction']

        # Handle situations where origin_prompt may be a list
        if isinstance(item['origin_prompt'], list):
            origin_prompt = ' '.join([prompt['prompt'] for prompt in item['origin_prompt'] if 'prompt' in prompt])
        else:
            origin_prompt = item['origin_prompt']

        # Extract options from the original prompt
        choices = re.findall(r'([A-D]\. .+)', origin_prompt)
        choices = [choice.split('. ', 1)[1] for choice in choices]

        pred = extract_answer(pred_text, choices=choices)
        ref = item['gold']

        results.append({
            'id': idx,
            'prediction': pred,
            'reference': ref,
            'is_correct': pred == ref,
            'original_text': pred_text
        })

    return results
def evaluate_models(base_dir: str) -> Dict[str, Dict[str, any]]:
    results = defaultdict(dict)

    for model in os.listdir(base_dir):
        model_dir = os.path.join(base_dir, model)
        if os.path.isdir(model_dir):
            for shot in ['0shot', '5shot']:
                file_path = os.path.join(model_dir, f'ARC-c_{shot}.json')
                if os.path.exists(file_path):
                    data = process_file(file_path)
                    accuracy = calculate_accuracy([item['prediction'] for item in data],
                                                  [item['reference'] for item in data])
                    results[model][f'{shot}-accuracy'] = accuracy
                    results[model][f'{shot}-data'] = data

    return results

def print_results(results: Dict[str, Dict[str, any]]):
    print("Evaluation result：")
    print("=" * 50)
    for model, scores in results.items():
        print(f"模型: {model}")
        for shot in ['0shot', '5shot']:
            if f'{shot}-accuracy' in scores:
                print(f"  {shot}: {scores[f'{shot}-accuracy']:.2f}%")
        print("-" * 50)

def save_results_to_csv(results: Dict[str, Dict[str, any]], output_file: str):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Model', '0shot-accuracy', '5shot-accuracy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for model, scores in results.items():
            writer.writerow({
                'Model': model,
                '0shot-accuracy': f"{scores.get('0shot-accuracy', 'N/A'):.2f}%",
                '5shot-accuracy': f"{scores.get('5shot-accuracy', 'N/A'):.2f}%"
            })

def save_errors_to_json(results: Dict[str, Dict[str, any]], output_file: str):
    errors = defaultdict(lambda: defaultdict(list))

    for model, data in results.items():
        for shot in ['0shot', '5shot']:
            if f'{shot}-data' in data:
                for item in data[f'{shot}-data']:
                    if not item['is_correct']:
                        errors[model][shot].append({
                            'id': item['id'],
                            'prediction': item['prediction'],
                            'reference': item['reference'],
                            'original_text': item['original_text']
                        })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(errors, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    base_dir = '../ARC_c-yue/prediction'
    results = evaluate_models(base_dir)
    print_results(results)

    # Save results to CSV file
    save_results_to_csv(results, 'arc_cantonese_results.csv')
    print("Results have been saved to arc_cantonese_results.csv")

    # Save the wrong answer to a JSON file
    save_errors_to_json(results, 'arc_cantonese_errors.json')
    print("Wrong Answer have been saved to arc_cantonese_errors.json")