from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.mark.parametrize("operation, state, filtered_data", [
    ([
         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"}],
     "CANCELED",
     [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2019-01-22T10:15:00.511233'}])
])
def test_filter_by_state(operation, state, filtered_data):
    assert filter_by_state(operation, state) == filtered_data


def test_sort_by_date(data_date):
    assert sort_by_date(data_date) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
