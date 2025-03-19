from src.decorators import log


@log()
def my_function_success(x: int, y: int) -> int:
    """Function for adding two integers."""
    return x + y  # Returns the sum of x and y


@log()
def my_function_error(x: float, y: float) -> float:
    """Function for dividing two numbers."""
    return x / y  # Returns the result of dividing x by y
