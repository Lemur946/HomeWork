from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date
from src.read_operations_csv import read_transactions_from_csv
from src.read_operations_xlsx import read_transactions_from_excel
from src.search import search_transactions_by_description
from src.utils import get_transactions_dictionary
from src.widget import mask_account_card


def main() -> None:
    """
    A function that is responsible for the main logic of the project and connects functionalities together.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice: str = input("Пользователь: ").strip()

    transactions: list[dict[Any, Any]] = []

    if choice == '1':
        file_path_JSON: str = '../data/operations.json'
        transactions = get_transactions_dictionary(file_path_JSON)
        print("Для обработки выбран JSON-файл.")

    elif choice == '2':
        file_path_CSV: str = '../data/transactions.csv'
        transactions = read_transactions_from_csv(file_path_CSV)

        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        file_path_XLSX: str = '../data/transactions_excel.xlsx'
        transactions = read_transactions_from_excel(file_path_XLSX)

        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неправильный выбор.")
        return

    valid_state: List[str] = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        state: str = input("Введите статус для фильтрации (доступные: EXECUTED, CANCELED, PENDING): ").strip()
        if state.upper() in valid_state:
            transactions = filter_by_state(transactions, state)
            print(f"Операции отфильтрованы по статусу \"{state.upper()}\"")

            break
        else:
            print(f"Статус операции \"{state}\" недоступен.")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_transactions_by_date: str = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_transactions_by_date == 'да':
        order: str = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        ascending: bool = (order == "по возрастанию")

        try:
            transactions = sort_by_date(transactions, ascending)
        except TypeError as e:
            print("Ошибка при сортировке транзакций:", e)
            return

    filter_by_currency: str = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if filter_by_currency == 'да':
        transactions = [
            t for t in transactions
            if t.get('operationAmount', {}).get('currency', {}).get('code', '').upper() == 'RUB' or
            t.get('currency_code', '').upper() == 'RUB'
        ]

    filter_by_description: str = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if filter_by_description == 'да':
        search_str: str = input("Введите слово для фильтрации: ").strip()
        transactions = search_transactions_by_description(transactions, search_str)

    if transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(f"{transaction.get('date', '')} {transaction.get('description', '')}")
            account_from: str = transaction.get('from', '')

            account_to: str = transaction.get('to', '')

            if (isinstance(account_from, str) and account_from.lower() != 'nan' and account_to and
                    len(account_from) != 0):
                account_from_mask: str = mask_account_card(account_from)
                account_to_mask: str = mask_account_card(account_to)
                print(f"{account_from_mask} -> {account_to_mask}")
            elif account_to:
                account_to_mask_2: str = mask_account_card(account_to)
                print(account_to_mask_2)
            operation_amount: Dict[str, Any] = transaction.get('operationAmount', {})
            currency_info: Dict[str, Any] = operation_amount.get('currency', {})
            if operation_amount and currency_info:
                amount: str = operation_amount.get('amount', '')
                currency_code: str = currency_info.get('code', '')
                print(f"Сумма: {amount} {currency_code}")
            else:
                print(f"Сумма: {transaction.get('amount', '')} {transaction.get('currency_code', '')}")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
