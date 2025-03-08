import logging
from functools import wraps


def log(filename=None):

    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f'Start executing function: {func.__name__} with arguments: {args}, {kwargs}')
            try:
                result = func(*args, **kwargs)

                logging.info(f'{func.__name__} ok')
                return result
            except Exception as e:

                logging.error(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}')
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)

@log(filename="mylog.txt")
def my_function_error(x, y):
    return x / y

my_function_error(1, 0)
