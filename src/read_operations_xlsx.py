from typing import Any, Hashable

import pandas as pd


def read_transactions_from_excel(file_path: str) -> list[dict[Hashable, Any]]:
    """
    A function that reads financial transactions from an Excel file.
    """
    try:
        file_path = '../data/transactions_excel.xlsx'
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


transactions_excel = read_transactions_from_excel('transactions.xlsx')
print(transactions_excel)
