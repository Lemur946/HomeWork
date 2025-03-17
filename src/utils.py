import json
from typing import Any, Dict, List


def get_transactions_dictionary() -> List[Dict[str, Any]]:
    """A function that loads transactions from a JSON file and returns them as a dictionary."""
    file_path = '../data/operations.json'  # Path to the file with transactions
    try:
        # Opening the file and loading JSON data
        with open(file_path, "r", encoding="utf-8") as operations:
            transactions = json.load(operations)
            return transactions  # Return the list of transactions

    except (json.JSONDecodeError, FileNotFoundError):
        # In case of error, return an empty list
        return []
