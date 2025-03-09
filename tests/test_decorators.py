import pytest
from src.functions import my_function_success, my_function_error

def test_my_function_success(caplog):
    with caplog.at_level('INFO'):  # Уровень записи логов
        my_function_success(1, 2)  # Вызываем функцию
    assert "my_function_success ok" in caplog.text  # Проверяем, что вывод содержит "my_function_success ok"

def test_my_function_error(caplog):
    with caplog.at_level('ERROR'):  # Уровень записи логов
        with pytest.raises(ZeroDivisionError):
            my_function_error(1, 0)  # Вызываем функцию с ошибкой

    assert "my_function_error error: ZeroDivisionError" in caplog.text  # Проверяем сообщение об ошибке