def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """A function that filters the list of operations by the value of the 'state' key"""
    return [operation for operation in operations if operation.get("state") == state]
