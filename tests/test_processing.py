# Importing the functions to be tested and pytest
import pytest

from src.processing import filter_by_state, sort_by_date


# Creating a parameterization and testing function for the filtering function by key "CANCELED"
@pytest.mark.parametrize(
    "operation_1, state_1, filtered_data_1",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"},
            ],
        )
    ],
)
def test_filter_by_state_1(operation_1: list[dict], state_1: str, filtered_data_1: list[dict]) -> None:
    """A function that tests a data filter by key"""
    assert filter_by_state(operation_1, state_1) == filtered_data_1


# Creating a parameterization and testing function for the filtering function by key "EXECUTED"
@pytest.mark.parametrize(
    "operation_2, state_2, filtered_data_2",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state_2(operation_2: list[dict], state_2: str, filtered_data_2: list[dict]) -> None:
    """A function that tests a data filter by key"""
    assert filter_by_state(operation_2, state_2) == filtered_data_2


def test_sort_by_date(data_date: list[dict]) -> None:
    """A function that tests data sorting by date. Source data is taken from conftest.py"""
    assert sort_by_date(data_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
