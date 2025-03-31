from src.external_api import convert_currency_to_rub
from src.utils import get_transactions_dictionary

# Loading transactions from JSON file
file_path = get_transactions_dictionary('../data/operations.json')

# Convert each transaction and output the result
for transaction in file_path:
    if "description" in transaction:
        # Convert the transaction amount into rubles
        converted_amount = convert_currency_to_rub(transaction)
        # Output the conversion result
        # print(f"Converted amount for '{transaction['description']}': {converted_amount} RUB")  # Вывод результата
    else:
        pass
        # If the transaction description is missing, we display an error
        # print("Error: Transaction does not contain a description.")
if __name__ == "__main__":
    print(file_path)
