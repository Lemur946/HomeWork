# Importing the functions to be tested, pytest and typing
from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Creating a parameterization and testing function mask card number
@pytest.mark.parametrize(
    "card_number, masked_number",
    [("7000792289606361", "7000 79** **** 6361"), (7520226985214568, "7520 22** **** 4568")],
)
def test_get_mask_card_number(card_number: Union[int, str], masked_number: str) -> None:
    """A function that tests mask card number"""
    assert get_mask_card_number(card_number) == masked_number


def test_get_mask_account(account_number: Union[int, str]) -> None:
    """A function that tests mask account number"""
    assert get_mask_account(account_number) == "**4305"
    # assert get_mask_account("54155fd55115b44441") == "**4441"
