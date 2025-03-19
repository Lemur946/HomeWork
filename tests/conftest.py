# Import pytest and create fixtures for testing some functions
import pytest


@pytest.fixture
def account_number() -> int:
    """Function returning account number"""
    return 73654108430135874305


@pytest.fixture
def filter_by_state() -> list[dict]:
    """Function returning data for testing"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"},
    ]


@pytest.fixture
def date() -> str:
    """Function returning date for testing"""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def data_date() -> list[dict]:
    """Function returning data for testing"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sample_transactions() -> list[dict]:
    """Function returning data for testing"""
    return [
        {
            "description": "Transaction 1",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "USD",
                },
            },
        },
        {
            "description": "Transaction 2",
            "operationAmount": {
                "amount": "50.00",
                "currency": {
                    "code": "EUR",
                },
            },
        },
        {
            "description": "Transaction 3",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "code": "USD",
                },
            },
        },
    ]
