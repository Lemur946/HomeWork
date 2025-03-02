from mypy.server.objgraph import Iterable
from data.transactions import transactions
from typing import Generator, Union


def filter_by_currency(transactions: list[dict], currency: str) -> Iterable[dict]:
    """
    Function, which takes as input a list of dictionaries representing transactions and
returns an iterator that one by one produces transactions where the transaction currency matches the given one
"""
    for transaction in transactions:
        if 'operationAmount' in transaction and 'currency' in transaction['operationAmount']:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


# Example of using the function
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> Iterable[str]:
    """
    Generator, which takes a list of transaction dictionaries and returns a description of each operation in turn.
    """
    if not transactions:  # Если нет транзакций, сразу возвращаем "Нет данных"
        yield "Нет данных"
        return

    for trans in transactions:
        if "description" in trans:
            yield trans["description"]

    yield "Нет данных"  # Возвращаем "Нет данных" после всех описаний (если они были)


# Example of using the function
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: Union[int, str], stop: Union[int, str]) -> Generator[str, None, None]:
    """
    Generator, which provides bank card numbers in the format XXXX XXXX XXXX XXXX,
    Where X — digit of the card number.
    """
    try:
        start = int(start)
        stop = int(stop)
    except ValueError:
        raise ValueError("Некорректные входные данные")
    if (isinstance(start, int) and isinstance(stop, int) and start <= stop and 1 <= start <= 9999999999999999 and
            1 <= stop <= 9999999999999999):
        card_numbers = '0000000000000000'
        for card_number in range(start, stop + 1):
            card_number_gen = (card_numbers[:-len(str(card_number))] + str(card_number))
            card_number_format = (
                f"{card_number_gen[0:4]} {card_number_gen[4:8]} "
                f"{card_number_gen[8:12]} {card_number_gen[12:16]}"
            )
            yield card_number_format

    else:
        raise ValueError("Некорректные входные данные")


# Example of using the function
for card_number in card_number_generator(1, 5):
    print(card_number)
