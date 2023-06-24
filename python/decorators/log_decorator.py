import logging

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Function {func.__name__} called with args {args} and kwargs {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Function {func.__name__} returned {result}')
        return func(*args, **kwargs)
    return wrapper

def print_log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'---------- Function {func.__name__} called with args {args} and kwargs {kwargs} ----------')
        result = func(*args, **kwargs)
        print(f'---------- Function {func.__name__} returned {result} ----------')
        return func(*args, **kwargs)
    return wrapper
