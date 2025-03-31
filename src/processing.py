def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """A function that filters the list of operations by the value of the 'state' key"""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """A function that sorts a list of transactions by date"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)


# # Examples of input data
# data_state = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2019-01-22T10:15:00.511233"},
# ]
# data_date = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# # Filter by status
# filtered_data = filter_by_state(data_state, state="CANCELED")
# print(f"Отфильтрованные данные: {filtered_data}")
#
# # Sort by date
# sorted_data = sort_by_date(data_date, reverse=True)
# print(f"Отсортированные данные: {sorted_data}")
