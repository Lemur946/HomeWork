from mypy.server.objgraph import Iterable
from data.transactions import transactions



def filter_by_currency(transactions: list[dict], currency: str) -> Iterable[dict]:
    for transaction in transactions:
        if 'operationAmount' in transaction and 'currency' in transaction['operationAmount']:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))



def transaction_descriptions(transactions: list[dict]) -> Iterable[str]:
    if not transactions:  # Если нет транзакций, сразу возвращаем "Нет данных"
        yield "Нет данных"
        return

    for trans in transactions:
        if "description" in trans:
            yield trans["description"]

    yield "Нет данных"  # Возвращаем "Нет данных" после всех описаний (если они были)

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start, stop):
    try:
        start = int(start)
        stop = int(stop)
    except ValueError:
        raise ValueError("Некорректные входные данные")
    if bool(isinstance(start, int)) and bool(
            isinstance(stop, int)) and start <= stop and start >= 1 and stop <= 9999999999999999:
        card_numbers = '0000000000000000'
        for card_number in range(start, stop + 1):
            card_number_gen = (card_numbers[:-len(str(card_number))] + str(card_number))
            card_number_format = f"{card_number_gen[0:4]} {card_number_gen[4:8]} {card_number_gen[8:12]} {card_number_gen[12:17]}"
            yield card_number_format

    else:
        raise ValueError("Некорректные входные данные")



for card_number in card_number_generator(1, 5):
    print(card_number)
