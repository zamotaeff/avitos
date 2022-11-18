"""csv and json modules for read files"""
import csv
import json


def convert_csv_to_json(csv_file, json_file) -> None:
    """Open csv file and convert to json
    """
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(rows, file, ensure_ascii=False)
