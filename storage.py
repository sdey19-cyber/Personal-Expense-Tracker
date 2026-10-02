import json
from config import FILE_NAME


def load_transactions():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_transactions(transactions):
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)