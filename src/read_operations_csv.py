import csv
from typing import Any, Dict, List


def read_transactions_from_csv(file_path_CSV: str) -> List[Dict[str, Any]]:
    """
    Function that reads financial transactions from a CSV file.
    """
    try:

        with open(file_path_CSV, mode='r', encoding='utf-8') as file:  # Open the file
            csv_reader = csv.DictReader(file, delimiter=';')
            if not csv_reader.fieldnames:  # Check for headers
                return []
            return [row for row in csv_reader]  # Read all lines and return them as a list of dictionaries
    except FileNotFoundError:
        print(f"File not found: {file_path_CSV}")
        return []
    except IOError:
        print(f"I/O error while working with file: {file_path_CSV}")
        return []
    except csv.Error:
        print(f"Error processing CSV file: {file_path_CSV}")
        return []


file_path_CSV = read_transactions_from_csv('../data/transactions.csv')
