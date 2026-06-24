import time
from functools import lru_cache


# ----------------------------
# BEFORE OPTIMIZATION
# ----------------------------

def fibonacci_slow(n: int) -> int:
    if n <= 1:
        return n

    return (
        fibonacci_slow(n - 1)
        + fibonacci_slow(n - 2)
    )


# ----------------------------
# AFTER OPTIMIZATION
# ----------------------------

@lru_cache(maxsize=None)
def fibonacci_fast(n: int) -> int:
    if n <= 1:
        return n

    return (
        fibonacci_fast(n - 1)
        + fibonacci_fast(n - 2)
    )


def benchmark() -> None:
    n = 35

    start = time.perf_counter()
    fibonacci_slow(n)
    slow_time = (
        time.perf_counter() - start
    )

    start = time.perf_counter()
    fibonacci_fast(n)
    fast_time = (
        time.perf_counter() - start
    )

    print(f"Slow: {slow_time:.4f}s")
    print(f"Fast: {fast_time:.4f}s")

    print(
        f"Speedup: {slow_time / fast_time:.2f}x"
    )


if __name__ == "__main__":
    benchmark()