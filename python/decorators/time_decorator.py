import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f'Execution time for {func.__name__}: {end} seconds.')
        return result
    return wrapper