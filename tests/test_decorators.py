import pytest
from src.decorators import log


def test_my_function_success(capsys):
    @log()
    def my_function_success(x, y):
        return x + y

    my_function_success(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_my_function_error(capsys):
    @log()
    def my_function_error(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function_error(1, 0)
    captured = capsys.readouterr()
    assert "my_function_error error: ZeroDivisionError" in captured.out


