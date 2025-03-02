from datetime import datetime  # Importing the necessary functions from other files

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """A function that will accept a card or account number indicating the account and mask it"""
    nuber_card = []
    name_card = []
    card_or_account_list = card_or_account.split()
    # The cycle with which we check what type of card or account is coming in
    if "Счет" in card_or_account_list:
        return f"Счет {get_mask_account(card_or_account_list[1])}"
    elif "MasterCard" in card_or_account_list or "Maestro" in card_or_account_list:
        return f"{card_or_account_list[0]} {get_mask_card_number(card_or_account_list[1])}"
    elif "Visa" in card_or_account_list:
        for i in card_or_account_list:
            if i.isdigit():
                nuber_card.append(i)
            else:
                name_card.append(i)
        str_numbers_card = " ".join(nuber_card)
    return f"{name_card[0]} {name_card[1]} {get_mask_card_number(str_numbers_card)}"


def get_date(my_date: str) -> str:
    """A function that will accept a date and time in one format and convert it to another"""
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


# Checking the correct operation of the code
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
