# Importing the functions to be tested and pytest
import pytest

from src.widget import get_date, mask_account_card


# Creating a parameterization and testing function mask account or card number
@pytest.mark.parametrize(
    "card_or_account_nuber, mask_card_or_account",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(card_or_account_nuber: str, mask_card_or_account: str) -> None:
    """A function that tests mask account or card number"""
    assert mask_account_card(card_or_account_nuber) == mask_card_or_account


def test_get_date(date: str) -> None:
    """A function that tests will accept a date and time in one format and convert it to another"""
    assert get_date(date) == "11.03.2024"
