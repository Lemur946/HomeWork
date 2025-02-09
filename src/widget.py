from masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(card_or_account: str) -> str:
    nuber_card = []
    name_card = []
    card_or_account_list = card_or_account.split()
    if "Счет" in card_or_account_list:
        return f"Счет {get_mask_account(card_or_account_list[1])}"
    elif "MasterCard" or "Maestro" in card_or_account_list:
        return f"{card_or_account_list[0]} {get_mask_card_number(card_or_account_list[1])}"
    elif "Visa" in card_or_account_list:
        for i in card_or_account_list:
            if i.isdigit():
                nuber_card.append(i)
            else:
                name_card.append(i)
        str_numbers_card = " ".join(nuber_card)
        return f"{name_card[0]} {name_card[1]} {get_mask_card_number(str_numbers_card)}"




