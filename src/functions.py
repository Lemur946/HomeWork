from src.decorators import log

@log()
def my_function(x, y):
    return x + y

@log()
def my_function_error(x, y):

    return x / y