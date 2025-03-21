import csv
from typing import Any, Dict, List


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Function that reads financial transactions from a CSV file.
    """
    try:

        with open(file_path, mode='r', encoding='utf-8') as file:  # Open the file
            csv_reader = csv.DictReader(file, delimiter=';')
            if not csv_reader.fieldnames:  # Check for headers
                return []
            return [row for row in csv_reader]  # Read all lines and return them as a list of dictionaries
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError:
        print(f"I/O error while working with file: {file_path}")
        return []
    except csv.Error:
        print(f"Error processing CSV file: {file_path}")
        return []


file_path = read_transactions_from_csv('../data/transactions.csv')
print(file_path)
