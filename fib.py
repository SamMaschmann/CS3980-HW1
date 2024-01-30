#fib.py
import functools
from time import time

def timer(func):
    def wrapper_function(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f"Finished in {(t2-t1)}: f{args} -> {result}")
        return result

    return wrapper_function



@functools.lru_cache
@timer
def fib(n: int) -> int:
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(100)