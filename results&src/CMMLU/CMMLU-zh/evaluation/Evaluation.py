#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CMMLU Chinese Evaluation Script

This script evaluates model predictions for the CMMLU (Chinese Multi-task Language
Understanding) benchmark in Chinese. It processes prediction files, calculates
accuracies, and generates CSV and JSON output files for analysis.

Author: CHEN Pengan
Date: Aug 11 2024
License: MIT
"""

import json
import os
import re
import csv
from typing import List, Dict, Tuple
from collections import defaultdict
import argparse
from tqdm import tqdm
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
    final_answer = re.search(r'(?:因此|所以|综上所述|总之|故|結論是?).{0,20}?(?:答案|選擇|选择|选项|字母|標准答案|正确答案).{0,10}?是\s*[^ABCD]*?([ABCD])\b', prediction, re.IGNORECASE | re.DOTALL)
    if final_answer:
        return final_answer.group(1).upper()

    # Search for explicit answer statements
    explicit_answer = re.search(r'(?:^|。|\n)(?:[ABCD]|\s)*(?:答案|選擇|选择|选项|字母|標准答案|正确答案).{0,10}?(?:是|为|為|:).{0,10}?([ABCD])\b', prediction, re.IGNORECASE)
    if explicit_answer:
        return explicit_answer.group(1).upper()

    # Search for direct statement of answer
    direct_statement = re.search(r'(?:^|。|\n)\s*([ABCD])\s*(?:是|为|為|:|。)', prediction)
    if direct_statement:
        return direct_statement.group(1).upper()

    # Search for sentences containing answer keywords
    answer_sentence = re.search(r'(?:答案|選擇|选择|选项|字母|標准答案|正确答案).{0,10}?(?:是|为|為|:).{0,10}?([ABCD])\b', prediction, re.IGNORECASE)
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
        for match in re.finditer(r'([A-D])\.\s*(.+?)(?=\n[A-D]\.|\n答案:|\Z)', prompt, re.DOTALL):
            choice_dict[match.group(1)] = match.group(2).strip()

        best_match = max(choice_dict.items(), key=lambda x: Levenshtein.ratio(prediction.lower(), x[1].lower()))
        return best_match[0].upper()

    return ''

def extract_choices_from_prompt(prompt: str) -> List[str]:
    """
    Extract choices from the prompt.

    Args:
        prompt (str): The prompt text.

    Returns:
        List[str]: List of extracted choices.
    """
    choices = re.findall(r'([A-D]\. .+)', prompt)
    return [choice.split('. ', 1)[1] for choice in choices]

def process_file(file_path: str) -> Dict:
    """
    Process a single prediction file and calculate accuracy.

    Args:
        file_path (str): Path to the prediction file.

    Returns:
        Dict: A dictionary containing accuracy, sample count, and errors.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    correct_count = 0
    total_count = 0
    errors = []

    for idx, item in data.items():
        if isinstance(item['prediction'], list):
            pred_text = item['prediction'][0]
        else:
            pred_text = item['prediction']

        # Extract choices and prompt
        if isinstance(item['origin_prompt'], list):
            # For 5-shot, use the last prompt
            last_prompt = item['origin_prompt'][-1]['prompt']
            choices = extract_choices_from_prompt(last_prompt)
            prompt = last_prompt
        else:
            # For 0-shot
            choices = extract_choices_from_prompt(item['origin_prompt'])
            prompt = item['origin_prompt']

        pred = extract_answer(pred_text, choices=choices, prompt=prompt)
        ref = item['gold']

        total_count += 1
        if pred == ref:
            correct_count += 1
        else:
            errors.append({
                'id': idx,
                'original': item,
                'extracted_answer': pred
            })

    accuracy = (correct_count / total_count) * 100 if total_count else 0
    return {
        'accuracy': accuracy,
        'n_samples': total_count,
        'errors': errors
    }

def evaluate_cmmlu(args):
    """
    Evaluate CMMLU predictions for all models and subjects.

    Args:
        args: Command line arguments containing paths and settings.
    """
    results = defaultdict(lambda: defaultdict(dict))
    all_subjects = set()

    for model in os.listdir(args.predictions_dir):
        model_dir = os.path.join(args.predictions_dir, model)
        if os.path.isdir(model_dir):
            for file in os.listdir(model_dir):
                if file.endswith('.json'):
                    parts = file.split('-')
                    subject = '-'.join(parts[1:-1])
                    # subject = '-'.join(parts[2:-1])
                    shot = parts[-1].split('.')[0]

                    all_subjects.add(subject)

                    file_path = os.path.join(model_dir, file)
                    file_results = process_file(file_path)

                    results[model][shot][subject] = file_results

    # Generate CSV file
    csv_file = os.path.join(args.output_dir, "cmmlu_results.csv")
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        header = ['Subject']
        for model in results:
            header.extend([f"{model}-0shot", f"{model}-5shot"])
        writer.writerow(header)

        for subject in sorted(all_subjects):
            row = [subject]
            for model in results:
                for shot in ['0shot', '5shot']:
                    accuracy = results[model][shot].get(subject, {}).get('accuracy', 0)
                    row.append(f"{accuracy:.2f}")
            writer.writerow(row)

        avg_row = ['Average']
        for model in results:
            for shot in ['0shot', '5shot']:
                total_correct = sum(subj_result['accuracy'] * subj_result['n_samples'] / 100
                                    for subj_result in results[model][shot].values())
                total_samples = sum(subj_result['n_samples'] for subj_result in results[model][shot].values())
                avg_accuracy = total_correct / total_samples * 100 if total_samples else 0
                avg_row.append(f"{avg_accuracy:.2f}")
        writer.writerow(avg_row)

    print(f"CSV results saved to {csv_file}")

    # Generate error cases JSON file
    errors_file = os.path.join(args.output_dir, "cmmlu_errors.json")
    errors = defaultdict(lambda: defaultdict(dict))
    for model in results:
        for shot in ['0shot', '5shot']:
            for subject in results[model][shot]:
                errors[model][shot][subject] = results[model][shot][subject]['errors']

    with open(errors_file, 'w', encoding='utf-8') as f:
        json.dump(errors, f, ensure_ascii=False, indent=2)

    print(f"Error cases saved to {errors_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate CMMLU Chinese predictions.')
    parser.add_argument("--predictions_dir", type=str, default="../predictions",
                        help="Directory containing prediction files (default: predictions)")
    parser.add_argument("--output_dir", type=str, default="./",
                        help="Directory to save output files (default: current directory.)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    evaluate_cmmlu(args)