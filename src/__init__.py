from typing import Any, Dict, List

from .external_api import convert_currency_to_rub
from .utils import get_transactions_dictionary

# Loading transactions from JSON file
transactions: List[Dict[str, Any]] = get_transactions_dictionary()

# Convert each transaction and output the result
for transaction in transactions:
    if 'description' in transaction:
        # Convert the transaction amount into rubles
        converted_amount = convert_currency_to_rub(transaction)
        # Output the conversion result
        print(f"Converted amount for '{transaction['description']}': {converted_amount} RUB")  # Вывод результата
    else:
        # If the transaction description is missing, we display an error
        print("Error: Transaction does not contain a description.")
