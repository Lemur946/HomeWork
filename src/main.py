from utils import get_transactions_dictionary
from read_operations_csv import read_transactions_from_csv
from read_operations_xlsx import read_transactions_from_excel
from processing import sort_by_date, filter_by_state
from search import search_transactions_by_description
from widget import mask_account_card
import math


def main():
    """
    A function that is responsible for the main logic of the project and connects functionalities together.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    transactions = []

    if choice == '1':
        file_path_JSON = '../data/operations.json'
        transactions = get_transactions_dictionary(file_path_JSON)
        print("Для обработки выбран JSON-файл.")

    elif choice == '2':
        file_path_CSV = '../data/transactions.csv'
        transactions = read_transactions_from_csv(file_path_CSV)

        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        file_path_XLSX = '../data/transactions_excel.xlsx'
        transactions = read_transactions_from_excel(file_path_XLSX)

        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неправильный выбор.")
        return

    valid_state = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        state = input("Введите статус для фильтрации (доступные: EXECUTED, CANCELED, PENDING): ").strip()
        if state.upper() in valid_state:
            transactions = filter_by_state(transactions, state)
            print(f"Операции отфильтрованы по статусу \"{state.upper()}\"")

            break
        else:
            print(f"Статус операции \"{state}\" недоступен.")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_transactions_by_date = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_transactions_by_date == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        ascending = (order == "по возрастанию")

        try:
            transactions = sort_by_date(transactions, ascending)
        except TypeError as e:
            print("Ошибка при сортировке транзакций:", e)
            return

    filter_by_currency = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if filter_by_currency == 'да':
        transactions = [
            t for t in transactions
            if t.get('operationAmount', {}).get('currency', {}).get('code', '').upper() == 'RUB' or
               t.get('currency_code', '').upper() == 'RUB'
        ]

    filter_by_description = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if filter_by_description == 'да':
        search_str = input("Введите слово для фильтрации: ").strip()
        transactions = search_transactions_by_description(transactions, search_str)

    if transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(f"{transaction.get('date', '')} {transaction.get('description', '')}")
            account_from = transaction.get('from', '')

            account_to = transaction.get('to', '')

            if isinstance(account_from, str) and account_from.lower() != 'nan' and account_to:
                account_from_mask = mask_account_card(account_from)
                account_to_mask = mask_account_card(account_to)
                print(f"{account_from_mask} -> {account_to_mask}")
            elif account_to:
                account_to_mask = mask_account_card(account_to)
                print(account_to_mask)
            operation_amount = transaction.get('operationAmount', {})
            currency_info = operation_amount.get('currency', {})
            if operation_amount and currency_info:
                amount = operation_amount.get('amount', '')
                currency_code = currency_info.get('code', '')
                print(f"Сумма: {amount} {currency_code}")
            else:
                print(f"Сумма: {transaction.get('amount', '')} {transaction.get('currency_code', '')}")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
