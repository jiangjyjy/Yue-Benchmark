#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ARC Evaluation Script

This script evaluates model predictions for the ARC (AI2 Reasoning Challenge)
benchmark in Cantonese and English. It processes prediction files, calculates accuracies,
and generates CSV and JSON output files for analysis.

"""

import json
import os
import re
import csv
from typing import List, Dict
from collections import defaultdict
import Levenshtein

def extract_answer(prediction: str, options: str = 'ABCD', choices: List[str] = None, prompt: str = None) -> str:
    """
    Extract the answer from the model's prediction text.

    Args:
        prediction (str): The prediction text.
        options (str): The valid answer options.
        choices (List[str]): List of answer choices for similarity comparison.
        prompt (str): The original prompt containing the question and choices.

    Returns:
        str: The extracted answer, or an empty string if no answer is found.
    """
    if not prediction:
        return ''

    # Clean the prediction text
    prediction = prediction.strip()

    # Check if the prediction contains only one letter from the options
    option_letters = [letter for letter in prediction if letter.upper() in options]
    if len(option_letters) == 1:
        return option_letters[0].upper()

    # Search for explicit final answer statements
    final_answer = re.search(r'(?:So|Thus|因此|所以|综上所述|总之|故|結論是?).{0,20}?(?:Answer|Option|Chooce|答案|選擇|选择|选项|字母|標准答案|正确答案).{0,10}?是\s*[^ABCD]*?([ABCD])\b', prediction, re.IGNORECASE | re.DOTALL)
    if final_answer:
        return final_answer.group(1).upper()

    # Search for explicit answer statements
    explicit_answer = re.search(r'(?:^|。|\n)(?:[ABCD]|\s)*(?:Answer|Option|Chooce|答案|選擇|选择|选项|字母|標准答案|正确答案).{0,10}?(?:is|是|为|為|:).{0,10}?([ABCD])\b', prediction, re.IGNORECASE)
    if explicit_answer:
        return explicit_answer.group(1).upper()

    # Search for direct statement of answer
    direct_statement = re.search(r'(?:^|。|\n)\s*([ABCD])\s*(?:is|是|为|為|:|。)', prediction)
    if direct_statement:
        return direct_statement.group(1).upper()

    # Search for sentences containing answer keywords
    answer_sentence = re.search(r'(?:Answer|Option|Chooce|答案|選擇|选择|选项|字母|標准答案|正确答案).{0,10}?(?:is|是|为|為|:).{0,10}?([ABCD])\b', prediction, re.IGNORECASE)
    if answer_sentence:
        return answer_sentence.group(1).upper()

    # Direct match for single letter answer
    direct_match = re.search(rf'\b([{options}])\b', prediction)
    if direct_match:
        return direct_match.group(1).upper()

    # Search for formatted options like "A.", "B.", etc.
    formatted_option = re.search(rf'\b([{options}])\.\s*', prediction)
    if formatted_option:
        return formatted_option.group(1).upper()

    # Find the last occurrence of an option letter
    all_options = re.findall(rf'\b([{options}])\b', prediction)
    if all_options:
        return all_options[-1].upper()

    # Fallback to similarity-based mechanism
    if choices and prompt:
        choice_dict = {}
        for match in re.finditer(r'([A-D])\.\s*(.+?)(?=\n[A-D]\.|\nAnswer|答案:|\Z)', prompt, re.DOTALL):
            choice_dict[match.group(1)] = match.group(2).strip()

        best_match = max(choice_dict.items(), key=lambda x: Levenshtein.ratio(prediction.lower(), x[1].lower()))
        return best_match[0].upper()

    return ''

def calculate_accuracy(predictions: List[str], references: List[str]) -> float:
    """
    Calculate the accuracy of predictions.

    Args:
        predictions (List[str]): List of predicted answers.
        references (List[str]): List of correct answers.

    Returns:
        float: The accuracy as a percentage.
    """
    correct = sum(p == r for p, r in zip(predictions, references))
    return (correct / len(references)) * 100 if references else 0

def process_file(file_path: str) -> Dict[str, List[Dict]]:
    """
    Process a single prediction file.

    Args:
        file_path (str): Path to the prediction file.

    Returns:
        Dict[str, List[Dict]]: Processed results including predictions and references.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = []

    for idx, item in data.items():
        pred_text = item['prediction'][0] if isinstance(item['prediction'], list) else item['prediction']

        origin_prompt = ' '.join([prompt['prompt'] for prompt in item['origin_prompt'] if 'prompt' in prompt]) \
            if isinstance(item['origin_prompt'], list) else item['origin_prompt']

        choices = re.findall(r'([A-D]\. .+)', origin_prompt)
        choices = [choice.split('. ', 1)[1] for choice in choices]

        pred = extract_answer(pred_text, choices=choices, prompt=origin_prompt)
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
    """
    Evaluate all models in the given directory.

    Args:
        base_dir (str): Base directory containing model predictions.

    Returns:
        Dict[str, Dict[str, any]]: Evaluation results for all models.
    """
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
    """
    Print evaluation results to console.

    Args:
        results (Dict[str, Dict[str, any]]): Evaluation results for all models.
    """
    print("Evaluation Results:")
    print("=" * 50)
    for model, scores in results.items():
        print(f"Model: {model}")
        for shot in ['0shot', '5shot']:
            if f'{shot}-accuracy' in scores:
                print(f"  {shot}: {scores[f'{shot}-accuracy']:.2f}%")
        print("-" * 50)

def save_results_to_csv(results: Dict[str, Dict[str, any]], output_file: str):
    """
    Save evaluation results to a CSV file.

    Args:
        results (Dict[str, Dict[str, any]]): Evaluation results for all models.
        output_file (str): Path to the output CSV file.
    """
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
    """
    Save error cases to a JSON file.

    Args:
        results (Dict[str, Dict[str, any]]): Evaluation results for all models.
        output_file (str): Path to the output JSON file.
    """
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
    base_dir = '../ARC_c-en/prediction'
    results = evaluate_models(base_dir)
    print_results(results)

    save_results_to_csv(results, 'arc_english_results.csv')
    print("Results saved to arc_english_results.csv")

    save_errors_to_json(results, 'arc_english_errors.json')
    print("Error cases saved to arc_english_errors.json")