#!/bin/usr/python3
"""module that reads data from CSV file to JSON format"""
import csv
import json


def convert_csv_to_json(filename):
    """Converts a CSV file to a JSON"""
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as csvfile:
            csvReader = csv.DictReader(csvfile)
            for rows in csvReader:
                data.append(rows)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
            return True

    except Exception:
        return False
