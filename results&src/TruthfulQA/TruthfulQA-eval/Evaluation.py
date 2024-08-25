#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Multi-language NLP Evaluation Script

This script evaluates model predictions for Cantonese, English, and Mandarin
using BLEU and ROUGE metrics. It supports different tokenization methods
based on the input language.

"""

import os
import json
import argparse
from typing import List, Dict, Any, Union
import nltk
import pycantonese
from jieba import lcut as jieba_cut
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_metric import PyRouge
import pandas as pd

# Ensure necessary NLTK data is downloaded
nltk.download('punkt', quiet=True)

def ensure_string(text: Union[str, List[str]]) -> str:
    """
    Ensure the input is a string.

    Args:
        text (Union[str, List[str]]): The input text or list of texts.

    Returns:
        str: A single string.
    """
    if isinstance(text, list):
        return ' '.join(map(str, text))
    return str(text)

def tokenize(text: Union[str, List[str]], language: str) -> List[str]:
    """
    Tokenize the input text based on the specified language.

    Args:
        text (Union[str, List[str]]): The input text to tokenize.
        language (str): The language of the text ('cantonese', 'english', or 'mandarin').

    Returns:
        List[str]: A list of tokens.

    Raises:
        ValueError: If an unsupported language is specified.
    """
    text = ensure_string(text)
    if language == 'cantonese':
        return list(pycantonese.segment(text))
    elif language == 'english':
        return nltk.word_tokenize(text)
    elif language == 'mandarin':
        return jieba_cut(text)
    else:
        raise ValueError(f"Unsupported language: {language}")

def calculate_bleu(reference_texts: List[Union[str, List[str]]], candidate_text: Union[str, List[str]], language: str) -> float:
    """
    Calculate the BLEU score for the candidate text against reference texts.

    Args:
        reference_texts (List[Union[str, List[str]]]): List of reference texts.
        candidate_text (Union[str, List[str]]): The candidate text to evaluate.
        language (str): The language of the texts.

    Returns:
        float: The BLEU score.
    """
    candidate_text = ensure_string(candidate_text)
    if not candidate_text:
        return 0
    references = [tokenize(text, language) for text in reference_texts]
    candidate = tokenize(candidate_text, language)
    smooth = SmoothingFunction().method7
    return sentence_bleu(references, candidate, smoothing_function=smooth)

def calculate_rouge(prediction: Union[str, List[str]], references: List[Union[str, List[str]]], language: str) -> Dict[str, Dict[str, float]]:
    """
    Calculate ROUGE scores for the prediction against references.

    Args:
        prediction (Union[str, List[str]]): The predicted text.
        references (List[Union[str, List[str]]]): List of reference texts.
        language (str): The language of the texts.

    Returns:
        Dict[str, Dict[str, float]]: A dictionary of ROUGE scores.
    """
    rouge = PyRouge(rouge_n=(1, 2, 3, 4), rouge_l=True, rouge_w=True, rouge_s=True, rouge_su=True, skip_gap=4)
    prediction = ensure_string(prediction)
    if not prediction:
        return {metric: {'r': 0, 'p': 0, 'f': 0} for metric in ['rouge-1', 'rouge-2', 'rouge-3', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']}
    tokenized_prediction = tokenize(prediction, language)
    tokenized_references = [tokenize(ref, language) for ref in references]
    return rouge.evaluate_tokenized([tokenized_prediction], [tokenized_references])

def process_file(file_path: str, language: str) -> Dict[str, Any]:
    """
    Process a single prediction file and calculate evaluation metrics.

    Args:
        file_path (str): Path to the prediction file.
        language (str): The language of the texts.

    Returns:
        Dict[str, Any]: A dictionary containing evaluation results.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_best_bleu = total_correct_bleu = total_incorrect_bleu = 0
    total_rouge_scores: Dict[str, Dict[str, float]] = {}

    for value in data.values():
        prediction = value.get('prediction', '')
        best_answer = value['gold']['answers'].get('best_answer', '')
        correct_answers = value['gold']['answers'].get('correct_answers', [])
        incorrect_answers = value['gold']['answers'].get('incorrect_answers', [])

        best_bleu = calculate_bleu([best_answer], prediction, language) if best_answer else 0
        correct_bleu = calculate_bleu(correct_answers, prediction, language)
        incorrect_bleus = [calculate_bleu([incorrect], prediction, language) for incorrect in incorrect_answers] if incorrect_answers else [0]
        avg_incorrect_bleu = sum(incorrect_bleus) / len(incorrect_bleus) if incorrect_bleus else 0

        total_best_bleu += best_bleu
        total_correct_bleu += correct_bleu
        total_incorrect_bleu += avg_incorrect_bleu

        rouge_scores = calculate_rouge(prediction, correct_answers, language)

        for metric, scores in rouge_scores.items():
            if metric not in total_rouge_scores:
                total_rouge_scores[metric] = {'r': 0, 'p': 0, 'f': 0}
            for key in ['r', 'p', 'f']:
                total_rouge_scores[metric][key] += scores[key]

        value['evaluation'] = {
            'bleu': {
                'best': best_bleu,
                'correct': correct_bleu,
                'incorrect': avg_incorrect_bleu
            },
            'rouge': rouge_scores
        }

    num_items = len(data)
    if num_items > 0:
        avg_results = {
            'bleu': {
                'best': total_best_bleu / num_items,
                'correct': total_correct_bleu / num_items,
                'incorrect': total_incorrect_bleu / num_items
            },
            'rouge': {metric: {key: value[key] / num_items for key in value}
                      for metric, value in total_rouge_scores.items()}
        }
    else:
        avg_results = {'bleu': {'best': 0, 'correct': 0, 'incorrect': 0}, 'rouge': {}}

    return {'data': data, 'avg_results': avg_results}

def main(input_path: str, output_path: str, language: str):
    """
    Main function to process all prediction files and generate evaluation results.

    Args:
        input_path (str): Path to the input predictions directory.
        output_path (str): Path to save the evaluation results.
        language (str): The language of the texts.
    """
    os.makedirs(output_path, exist_ok=True)

    results = {}

    for model_name in os.listdir(input_path):
        model_path = os.path.join(input_path, model_name)
        if os.path.isdir(model_path):
            results[model_name] = {'0-shot': {}, '5-shot': {}}
            for file_name in os.listdir(model_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(model_path, file_name)
                    shot_type = '0-shot' if '0shot' in file_name else '5-shot'

                    print(f"Processing {model_name} - {shot_type}")

                    try:
                        file_results = process_file(file_path, language)
                        results[model_name][shot_type] = file_results['avg_results']

                        eval_file_path = os.path.join(output_path, f"{model_name}_{shot_type}_evaluated.json")
                        with open(eval_file_path, 'w', encoding='utf-8') as f:
                            json.dump(file_results['data'], f, ensure_ascii=False, indent=2)

                    except Exception as e:
                        print(f"Error processing {file_path}: {str(e)}")

    # Generate CSV report
    csv_data = []
    header = ['Model']
    for shot in ['0-shot', '5-shot']:
        header.extend([f'bleu-best({shot})', f'bleu-correct({shot})', f'bleu-incorrect({shot})'])
        for metric in ['rouge-1', 'rouge-2', 'rouge-3', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']:
            for score_type in ['f', 'p', 'r']:
                header.append(f'{metric}-{score_type}({shot})')

    csv_data.append(header)

    for model, scores in results.items():
        row = [model]
        for shot in ['0-shot', '5-shot']:
            if shot in scores and 'bleu' in scores[shot] and 'rouge' in scores[shot]:
                row.extend([
                    f"{scores[shot]['bleu'].get('best', 0):.10f}",
                    f"{scores[shot]['bleu'].get('correct', 0):.10f}",
                    f"{scores[shot]['bleu'].get('incorrect', 0):.10f}"
                ])
                for metric in ['rouge-1', 'rouge-2', 'rouge-3', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']:
                    for score_type in ['f', 'p', 'r']:
                        value = scores[shot]['rouge'].get(metric, {}).get(score_type, 0)
                        row.append(f'{value:.10f}')
            else:
                row.extend(['0.0000000000'] * (3 + 8 * 3))

        csv_data.append(row)

    df = pd.DataFrame(csv_data[1:], columns=csv_data[0])
    csv_file_path = os.path.join(output_path, 'BLEU_ROUGE.csv')
    df.to_csv(csv_file_path, index=False)

    print(f"Evaluation scores have been saved to {csv_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate model predictions for Cantonese, English, or Mandarin.')
    parser.add_argument('--input_path', type=str, default='./predictions',
                        help='Path to the input predictions directory (default: ./predictions)')
    parser.add_argument('--output_path', type=str, default='./evaluation',
                        help='Path to save the evaluation results (default: ./evaluation)')
    parser.add_argument('--language', type=str, choices=['cantonese', 'english', 'mandarin'], required=True,
                        help='Language of the text (cantonese, english, or mandarin)')

    args = parser.parse_args()

    main(args.input_path, args.output_path, args.language)