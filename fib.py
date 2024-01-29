#fib.py

@lru_cache
@timer
def fib(n: int) -> int:
    if (n == 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(100)