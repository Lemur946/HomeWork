import re
import unittest
from typing import Any, Dict, List


# Определяем функции, которые будем тестировать
def search_transactions_by_description(transactions: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """
    Функция для поиска банковских транзакций по строке в описании.

    :param transactions: Список транзакций, где каждая транзакция - это словарь с ключом 'description'.
    :param search_str: Строка для поиска в описании транзакций.
    :return: Список транзакций, где описания содержат искомую строку.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    matched_transactions = [
        transaction for transaction in transactions
        if pattern.search(transaction.get('description', ''))
    ]
    return matched_transactions


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Функция для подсчета количества транзакций по категориям.

    :param transactions: Список транзакций, где каждая транзакция - это словарь с ключом 'description'.
    :param categories: Список категорий для подсчета.
    :return: Словарь, где ключи - это категории, а значения - количество транзакций в каждой категории.
    """
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
                break
    return category_count


class TestTransactionFunctions(unittest.TestCase):
    def setUp(self) -> None:
        """
        Настройка теста, создание тестовых данных.
        """
        self.transactions = [
            {'description': 'Payment to utility company'},
            {'description': 'Grocery store purchase'},
            {'description': 'Transfer to savings'},
            {'description': 'Utility payment overdue'},
            {'description': 'Grocery store refund'},
            {'description': 'Payment for online subscription'}
        ]
        self.categories = ['utility', 'grocery', 'subscription', 'transfer']

    def test_search_transactions_by_description(self) -> None:
        """
        Тестирование поиска транзакций по описанию.
        """
        result = search_transactions_by_description(self.transactions, 'utility')
        expected = [
            {'description': 'Payment to utility company'},
            {'description': 'Utility payment overdue'}
        ]
        self.assertEqual(result, expected)

        result_no_match = search_transactions_by_description(self.transactions, 'entertainment')
        self.assertEqual(result_no_match, [])

    def test_count_transactions_by_category(self) -> None:
        """
        Тестирование подсчета транзакций по категориям.
        """
        result = count_transactions_by_category(self.transactions, self.categories)
        expected = {
            'utility': 2,
            'grocery': 2,
            'subscription': 1,
            'transfer': 1
        }
        self.assertEqual(result, expected)

        # Тестирование с пустым списком транзакций
        result_empty_transactions = count_transactions_by_category([], self.categories)
        expected_empty = {category: 0 for category in self.categories}
        self.assertEqual(result_empty_transactions, expected_empty)


if __name__ == '__main__':
    unittest.main()
