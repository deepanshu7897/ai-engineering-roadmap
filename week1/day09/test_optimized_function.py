from optimized_function import (
    fibonacci_slow,
    fibonacci_fast,
)


def test_fibonacci_slow():
    assert fibonacci_slow(10) == 55


def test_fibonacci_fast():
    assert fibonacci_fast(10) == 55


def test_same_result():
    assert (
        fibonacci_slow(15)
        == fibonacci_fast(15)
    )