from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize("card_number, masked_number", [
    ("7000792289606361", "7000 79** **** 6361"),
    (7520226985214568, "7520 22** **** 4568")
])
def test_get_mask_card_number(card_number, masked_number):
    assert get_mask_card_number(card_number) == masked_number


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4305"
    assert get_mask_account("54155fd55115b44441") == "**4441"
