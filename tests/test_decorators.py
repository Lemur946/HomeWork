import pytest

from src.functions import my_function_error, my_function_success


def test_my_function_success(caplog: pytest.LogCaptureFixture) -> None:
    """A test to check if the function my_function_success has successfully executed.
    This test calls the function my_function_success with arguments 1 and 2.
    It then checks that a message is written to the logs confirming the successful execution."""
    with caplog.at_level("INFO"):
        my_function_success(1, 2)  # Calling a function with test arguments
    # Check for a success message in the logs
    assert "my_function_success ok" in caplog.text


def test_my_function_error(caplog: pytest.LogCaptureFixture) -> None:
    """
    A test to check how the my_function_error function handles ZeroDivisionError.
    This test calls the my_function_error function with arguments 1 and 0 and expects
    that a ZeroDivisionError exception will be raised. It also checks that the error message is written to the logs.
    """
    with caplog.at_level("ERROR"):
        # Check for ZeroDivisionError when dividing by zero
        with pytest.raises(ZeroDivisionError):
            my_function_error(1, 0)  # Calling a function with arguments that cause an error

    # Check for error message in logs
    assert "my_function_error error: ZeroDivisionError" in caplog.text
