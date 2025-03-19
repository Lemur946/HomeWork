import logging
from functools import wraps
from typing import Any, Callable, Optional, TypeVar

# Define TypeVar for function types
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """Decorator for logging function execution."""
    # Setting up basic logging configuration
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def decorator(func: F) -> F:
        """A decorator that wraps a function to add logging"""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            A function wrapper that performs logging before and after a function call, as well as exception handling.
            """
            logging.info(f"Start executing function: {func.__name__} with arguments: {args}, {kwargs}")
            try:
                # Call a function
                result = func(*args, **kwargs)

                logging.info(f"{func.__name__} ok")  # Logging successful completion
                return result
            except Exception as e:
                # Logging the error and rethrowing the exception
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
