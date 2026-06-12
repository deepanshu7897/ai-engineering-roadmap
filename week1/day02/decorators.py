import time
from functools import wraps


# -------------------------
# BASIC DECORATOR
# -------------------------

def log_call(func):
    @wraps(func)
    def wrapper():
        print(f"Calling {func.__name__}")
        return func()

    return wrapper


@log_call
def greet():
    print("Hello")


# -------------------------
# TIMEIT DECORATOR
# -------------------------

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"{func.__name__} took {end - start:.4f} seconds")

        return result

    return wrapper


@timeit
def slow_function():
    time.sleep(1)


# -------------------------
# RETRY DECORATOR
# -------------------------

def retry(max_attempts: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    attempts += 1

                    print(
                        f"Attempt {attempts} failed: {e}"
                    )

            raise Exception(
                f"Failed after {max_attempts} attempts"
            )

        return wrapper

    return decorator


counter = 0


@retry(max_attempts=3)
def unstable_function():
    global counter

    counter += 1

    if counter < 3:
        raise ValueError("Temporary failure")

    return "Success"


# -------------------------
# RUN EXAMPLES
# -------------------------

greet()

slow_function()

print(unstable_function())