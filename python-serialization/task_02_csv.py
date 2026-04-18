#!/usr/bin/python3
"""
converting csv to json
"""
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
    except Exception:
        return False
    with open('data.json', mode='w', encoding='utf-8') as jsonfile:
        try:
            json.dump(data, jsonfile, indent=4)
            return True
        except Exception:
            return False