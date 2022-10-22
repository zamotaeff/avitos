import csv
import json

FILE_CSV_ADS = '../datasets/ad.csv'
FILE_CSV_CATEGORIES = '../datasets/category.csv'
FILE_CSV_LOCATIONS = '../datasets/location.csv'
FILE_CSV_USERS = '../datasets/user.csv'

FILE_JSON_ADS = '../datasets/ads.json'
FILE_JSON_CATEGORIES = '../datasets/categories.json'
FILE_JSON_LOCATIONS = '../datasets/locations.json'
FILE_JSON_USERS = '../datasets/users.json'


def convert_csv_to_json(csv_file, json_file):
    """

    """
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(rows, file, ensure_ascii=False)
