import csv
import unittest
from typing import Dict, List
from unittest.mock import mock_open, patch

from src.read_operations_csv import read_transactions_from_csv


class TestReadTransactionsFromCSV(unittest.TestCase):

    def test_file_not_found(self) -> None:
        """Test for a file that does not exist"""
        with patch('builtins.open', side_effect=FileNotFoundError):
            result: List[Dict[str, str]] = read_transactions_from_csv('non_existent_file.csv')
            self.assertEqual(result, [])

    def test_io_error(self) -> None:
        """Test for an IO Error exception"""
        with patch('builtins.open', side_effect=IOError):
            result: List[Dict[str, str]] = read_transactions_from_csv('io_error_file.csv')
            self.assertEqual(result, [])

    def test_csv_error(self) -> None:
        """Mock open to raise csv.Error"""
        with patch('builtins.open', mock_open(read_data='corrupted,data')):
            with patch('csv.DictReader', side_effect=csv.Error):
                result: List[Dict[str, str]] = read_transactions_from_csv('corrupted_file.csv')
                self.assertEqual(result, [])

    def test_empty_file(self) -> None:
        """Test an empty file"""
        with patch('builtins.open', mock_open(read_data='')):
            result: List[Dict[str, str]] = read_transactions_from_csv('empty.csv')
            self.assertEqual(result, [])

    def test_valid_csv(self) -> None:
        """Test a valid CSV with data"""
        mock_data: str = "name;amount;date\nJane Doe;100.0;2023-01-01\nJohn Doe;200.0;2023-01-02\n"
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result: List[Dict[str, str]] = read_transactions_from_csv('valid.csv')
            expected: List[Dict[str, str]] = [
                {'name': 'Jane Doe', 'amount': '100.0', 'date': '2023-01-01'},
                {'name': 'John Doe', 'amount': '200.0', 'date': '2023-01-02'}
            ]
            self.assertEqual(result, expected)
