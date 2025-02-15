def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """A function that filters the list of operations by the value of the 'state' key"""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """A function that sorts a list of transactions by date"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
