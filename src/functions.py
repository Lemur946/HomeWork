from src.decorators import log

@log()
def my_function_success(x, y):
    return x + y

@log()
def my_function_error(x, y):
    return x / y  # Не вызывайте эту функцию на уровне модуля