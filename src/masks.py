import logging
from typing import Union

logger = logging.getLogger('mask')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """A function that takes a card number as input and outputs a masked number"""

    logger.info("The card number was received from the user")
    card_number = str(card_number)  # For further work, convert the integer to a string.
    if len(card_number) != 16 or not card_number.isdigit():  # Checking that the card number is entered correctly
        logger.error("An error has occurred. The card number entered is invalid.")
        raise ValueError(
            "Неверный номер карты! Проверьте правильность введения"
        )  # Errors when entering the card number incorrectly.
    else:
        logger.info("The card number is being masked")
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card_number  # Returning the masked card number via the f line.


def get_mask_account(account_number: Union[int, str]) -> str:
    """A function that takes a bank account number as input and outputs a masked number"""
    logger.info("The account number was received from the user")
    account_number = str(account_number)  # For further work, convert the integer to a string.
    if len(account_number) < 4 or not account_number.isdigit():
        logger.error("An error has occurred. The account number entered is invalid.")
        raise ValueError(
            "Неверный номер счета! Проверьте правильность введения"
        )  # Errors when entering an account number incorrectly.
    else:
        logger.info("The account number is being masked")
        masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number  # Returning the masked account number via the f line.


# Entering card and account numbers through the console.
card_number = str(input("Введите номер карты "))
account_number = str(input("Введите номер счета "))

# Output of masked card and account numbers to the console.
print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
