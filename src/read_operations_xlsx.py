from typing import Any, Hashable

import pandas as pd


def read_transactions_from_excel(file_path: str) -> list[dict[Hashable, Any]]:
    """
    A function that reads financial transactions from an Excel file.
    """
    try:

        df = pd.read_excel(file_path)  # Open the Excel file and read the contents
        if df.empty:  # Checking if a file is empty
            return []
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError:
        print(f"I/O error while working with file: {file_path}")
        return []
    except ValueError:
        print(f"Error processing Excel file: {file_path}")
        return []


file_path = read_transactions_from_excel('../data/transactions_excel.xlsx')
print(file_path)
