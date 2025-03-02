# Importing the functions to be tested, pytest and typing
from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),  # We are expecting 2 transactions with the currency "USD"
    ("EUR", 1),  # We expect 1 transaction with the currency "EUR"
    ("JPY", 0)  # We expect 0 transactions with the currency "JPY"
])
def test_filter_by_currency(sample_transactions: List[Dict[str, Any]], currency: str, expected_count: int) -> None:
    """A function that checks that the function correctly filters transactions for the given currency."""
    filtered_transactions = list(filter_by_currency(sample_transactions, currency))
    assert len(filtered_transactions) == expected_count


@pytest.mark.parametrize("description_count", [
    (3),  # We expect the description to be in 3 transactions
])
def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]], description_count: int) -> None:
    """A function that tests the operation of a function with a different number of input transactions"""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions[:description_count]) == description_count


def test_transaction_descriptions_no_data(sample_transactions: List[Dict[str, Any]]) -> None:
    """Function testing the operation of a function with an empty list"""
    empty_transactions = []
    descriptions = list(transaction_descriptions(empty_transactions))
    assert descriptions == ['Нет данных']


def test_card_number_generator() -> None:
    """Function testing the correct formatting of card numbers"""
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
def test_card_number_generator_invalid_input(start: Any, stop: Any, exception: type) -> None:
    """A function that checks that the generator produces the correct card numbers in a given range."""
    with pytest.raises(exception):
        list(card_number_generator(start, stop))
