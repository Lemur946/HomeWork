import json
from typing import Any, Dict, List

# import os
#
# log_path = os.path.abspath('../logs/utils.log')
#
# logger = logging.getLogger('utils')
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler(log_path, mode='w')
# # file_handler = logging.FileHandler('../logs/utils.log', mode='w')
# file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)


def get_transactions_dictionary(file_path_JSON: str) -> List[Dict[str, Any]]:
    """A function that loads transactions from a JSON file and returns them as a dictionary."""
    # Path to the file with transactions
    try:
        # logger.info("Opening the file and loading JSON data")
        # Opening the file and loading JSON data
        with open(file_path_JSON, "r", encoding="utf-8") as operations:
            transactions = json.load(operations)
            if not isinstance(transactions, list):
                # logger.error("Error! Not a list was sent")
                return []
            # logger.info("Return a list of dictionaries with data")
            return transactions  # Return the list of transactions

    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        # logger.error(f"An error occurred: {ex}")
        # In case of error, return an empty list
        return []


file_path_JSON = get_transactions_dictionary('../data/operations.json')
# print(type(file_path_JSON))
