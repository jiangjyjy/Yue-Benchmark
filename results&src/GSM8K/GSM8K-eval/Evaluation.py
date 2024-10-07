#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GSM8K Evaluator

This script evaluates model performance on the GSM8K dataset for both English and Cantonese.
It processes prediction files and generates accuracy metrics, saving results to a CSV file.

"""

import json
import re
import os
import csv
from typing import Dict, Tuple, List
from typing import Union


class GSM8KEvaluator:
    #     def extract_answers(self, text: str) -> List[str]:
    #         """
    #         Extract numerical answers from the given text.
    #
    #         Args:
    #             text (str): The input text containing potential answers.
    #
    #         Returns:
    #             List[str]: A list of extracted answers or ['NULL'] if no answers found.
    #         """
    #         text = text.replace(',', '').replace('\n', ' ')
    #         answers = []
    #
    #         match = re.search(r'####\s*[$]?\s*(\d+\.?\d*)', text)
    #         if match:
    #             answers.append(match.group(1))
    #
    #         # NOTE: For Cantonese support, uncomment the following line and comment out the next line
    #         # split_text = re.split(r'Question:|Example:|問題：|樣例：', text, 1)
    #         split_text = re.split(r'Question:|Example:', text, 1)
    #         relevant_text = split_text[0].strip()
    #         numbers = re.findall(r'-?\d+\.?\d*', relevant_text)
    #         if numbers:
    #             answers.append(numbers[-1])
    #
    #         return answers if answers else ['NULL']

    def extract_answers(self, text: Union[str, List[str]]) -> List[str]:
        """
        Extract numerical answers from the given text or list of texts.

        Args:
            text (Union[str, List[str]]): The input text or list of texts containing potential answers.

        Returns:
            List[str]: A list of extracted answers or ['NULL'] if no answers found.
        """
        if isinstance(text, list):
            # If text is a list, join all elements into a single string
            text = ' '.join(map(str, text))

        if not isinstance(text, str):
            return ['NULL']

        text = text.replace(',', '').replace('\n', ' ')
        answers = []

        match = re.search(r'####\s*[$]?\s*(\d+\.?\d*)', text)
        if match:
            answers.append(match.group(1))

        # NOTE: For Cantonese support, uncomment the following line and comment out the next line
        # split_text = re.split(r'Question:|Example:|問題：|樣例：', text, 1)
        split_text = re.split(r'Question:|Example:', text, 1)
        relevant_text = split_text[0].strip()
        numbers = re.findall(r'-?\d+\.?\d*', relevant_text)
        if numbers:
            answers.append(numbers[-1])

        return answers if answers else ['NULL']

    def is_equal(self, pred: str, refer: str) -> bool:
        """
        Check if the predicted answer is equal to the reference answer.

        Args:
            pred (str): The predicted answer.
            refer (str): The reference answer.

        Returns:
            bool: True if the answers are equal, False otherwise.
        """
        try:
            if pred == 'NULL' or refer == 'NULL':
                return pred == refer
            return abs(float(pred) - float(refer)) < 1e-5
        except ValueError:
            return False

    def evaluate_file(self, file_path: str) -> Tuple[float, int, int]:
        """
        Evaluate a single prediction file.

        Args:
            file_path (str): Path to the prediction JSON file.

        Returns:
            Tuple[float, int, int]: Accuracy, number of correct predictions, and total predictions.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Unable to parse JSON in {file_path}")
            return 0.0, 0, 0

        correct = 0
        total = len(data)
        for key, item in data.items():
            try:
                pred_answers = self.extract_answers(item['prediction'])
                gold_answers = self.extract_answers(item['gold'])
                is_correct = any(self.is_equal(pred, gold)
                                 for pred in pred_answers
                                 for gold in gold_answers)
                if is_correct:
                    correct += 1
                data[key]['is_correct'] = is_correct
            except KeyError:
                print(f"Error: Missing 'prediction' or 'gold' in item {key}")
                continue

        accuracy = (correct / total) * 100 if total > 0 else 0.0

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError:
            print(f"Error: Unable to write to {file_path}")

        return accuracy, correct, total


def process_folders(base_path: str) -> Dict[str, Dict[str, float]]:
    """
    Process all prediction folders and evaluate model performances.

    Args:
        base_path (str): Base path containing the GSM8K folders.

    Returns:
        Dict[str, Dict[str, float]]: A dictionary of model performances.
    """
    evaluator = GSM8KEvaluator()
    results = {}
    for lang in ['en', 'yue']:
        folder_path = os.path.join(base_path, f'GSM8K-{lang}', 'predictions')
        if not os.path.exists(folder_path):
            print(f"Warning: Folder not found: {folder_path}")
            continue
        for model in os.listdir(folder_path):
            model_path = os.path.join(folder_path, model)
            if os.path.isdir(model_path):
                for file in os.listdir(model_path):
                    if file.endswith('.json'):
                        file_path = os.path.join(model_path, file)
                        accuracy, _, _ = evaluator.evaluate_file(file_path)
                        shot = '0shot' if '0shot' in file else '5shot'
                        if model not in results:
                            results[model] = {}
                        results[model][f'{lang}_{shot}'] = accuracy
    return results


def write_csv(results: Dict[str, Dict[str, float]], output_file: str):
    """
    Write evaluation results to a CSV file.

    Args:
        results (Dict[str, Dict[str, float]]): The evaluation results.
        output_file (str): Path to the output CSV file.
    """
    fieldnames = ['Model', 'en_0shot', 'en_5shot', 'yue_0shot', 'yue_5shot']
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for model, scores in results.items():
                row = {'Model': model}
                row.update(scores)
                writer.writerow(row)
    except IOError:
        print(f"Error: Unable to write to {output_file}")


def main():
    """Main function to run the GSM8K evaluation."""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results = process_folders(base_path)
    output_file = os.path.join(base_path, 'GSM8K-eval', 'GSM8K_evaluation_results.csv')
    write_csv(results, output_file)
    print(f"Evaluation results have been saved to {output_file}")


if __name__ == "__main__":
    main()