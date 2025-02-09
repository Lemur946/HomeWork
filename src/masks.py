from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """A function that takes a card number as input and outputs a masked number"""
    card_number = str(card_number)  # For further work, convert the integer to a string.
    # if len(card_number) != 16 or not card_number.isdigit():  # Checking that the card number is entered correctly
    #     raise ValueError(
    #         "Неверный номер карты! Проверте правильность введения"
    #     )  # Errors when entering the card number incorrectly.
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card_number  # Returning the masked card number via the f line.


def get_mask_account(account_number: Union[int, str]) -> str:
    """A function that takes a bank account number as input and outputs a masked number"""
    account_number = str(account_number)  # For further work, convert the integer to a string.
    # if len(account_number) < 4 or not account_number.isdigit():
    #     raise ValueError(
    #         "Неверный номер счета! Проверте правильность введения"
    #     )  # Errors when entering an account number incorrectly.
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number  # Returning the masked account number via the f line.


# Entering card and account numbers through the console.
# card_number = str(input("Введите номер карты "))
# account_number = str(input("Введите номер счета "))

# Output of masked card and account numbers to the console.
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))
