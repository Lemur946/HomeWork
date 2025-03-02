import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Параметризированный тест для фильтрации по валюте
@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),  # Ожидаем 2 транзакции с валютой "USD"
    ("EUR", 1),  # Ожидаем 1 транзакцию с валютой "EUR"
    ("JPY", 0)  # Ожидаем 0 транзакций с валютой "JPY"
])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    filtered_transactions = list(filter_by_currency(sample_transactions, currency))
    assert len(filtered_transactions) == expected_count


###################################
@pytest.mark.parametrize("transactions, expected_descriptions", [
    # Тестируем с тремя транзакциями
    (
            [
                {"description": "Transaction 1"},
                {"description": "Transaction 2"},
                {"description": "Transaction 3"},
            ],
            ["Transaction 1", "Transaction 2", "Transaction 3"]
    ),
    # Тестируем с двумя транзакциями, одна без описания
    (
            [
                {"description": "Transaction 1"},
                {},
            ],
            ["Transaction 1"]
    ),
    # Тестируем с пустыми транзакциями
    (
            [],
            []
    ),
])
def test_transaction_descriptions(transactions, expected_descriptions):
    descriptions_generator = transaction_descriptions(transactions)
    # Проверяем количество возвращаемых описаний
    for expected in expected_descriptions:
        assert next(descriptions_generator) == expected

    # Проверяем, что следующая запись возвращает "Нет данных"
    for _ in range(5):  # Здесь можно проверить несколько раз
        assert next(descriptions_generator) == "Нет данных"


# Параметризированный тест для описаний транзакций
@pytest.mark.parametrize("description_count", [
    (3),  # Ожидаем, что описание будет в 3 транзакциях
])
def test_transaction_descriptions(sample_transactions, description_count):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions[:description_count]) == description_count


def test_transaction_descriptions_no_data(sample_transactions):
    empty_transactions = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert descriptions == ['Нет данных']  # Убедитесь, что логика соответствует тому, как функция реализована


def test_card_number_generator():
    # Проверяем получение правильных номеров карт
    start = 1
    stop = 5
    generated_numbers = list(card_number_generator(start, stop))
    expected_numbers = [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]
    assert generated_numbers == expected_numbers


@pytest.mark.parametrize("start, stop, exception", [
    ("invalid", 5, ValueError),
    (5, "invalid", ValueError),
    (0, 5, ValueError),
    (1, 10000000000000000, ValueError)
])
def test_card_number_generator_invalid_input(start, stop, exception):
    with pytest.raises(exception):
        list(card_number_generator(start, stop))
