import re
from typing import Any, Dict, List


def search_transactions_by_description(transactions: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """
    Function for searching banking transactions by a string in the description.
    """
    # Compiling a regular expression ignoring case
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)

    # List to store results where the search string is found in 'description'
    matched_transactions = [
        transaction for transaction in transactions
        if pattern.search(transaction.get('description', ''))
    ]

    return matched_transactions


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Function for counting the number of transactions by category.
    """
    # Initializing a dictionary to count the number of operations by category
    category_count = {category: 0 for category in categories}

    # Walkthrough of all operations
    for transaction in transactions:
        # Is the description a field in the dictionary and is it empty?
        description: str = transaction.get('description', '').lower()

        # Check each category against the operation description
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
                break  # It is assumed that one operation belongs to only one category.

    return category_count
