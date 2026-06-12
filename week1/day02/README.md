# Day 02 — Decorators & Metaclasses

## Objectives

- Understand functions as first-class objects
- Learn closures and nested functions
- Build custom decorators
- Use `functools.wraps`
- Create decorator factories
- Implement practical decorators for logging, timing, and retries

---

## Concepts Covered

### Functions as Objects

```python
def greet():
    print("Hello")

say_hi = greet
say_hi()
```

### Closures

```python
def outer():
    def inner():
        print("Inside inner")

    return inner
```

### Basic Decorator

```python
@log_call
def greet():
    print("Hello")
```

### Decorator Factory

```python
@retry(max_attempts=3)
def unstable_function():
    ...
```

### functools.wraps

```python
from functools import wraps
```

Used to preserve the original function's metadata when wrapping functions.

---

## Deliverables

### Logging Decorator

```python
@log_call
```

Logs function calls before execution.

### Timing Decorator

```python
@timeit
```

Measures function execution time.

### Retry Decorator

```python
@retry(max_attempts=3)
```

Retries a function automatically when an exception occurs.

---

## Example Output

```text
Calling greet
Hello

slow_function took 1.0051 seconds

Attempt 1 failed: Temporary failure
Attempt 2 failed: Temporary failure

Success
```

---

## Testing

Run:

```bash
pytest
```

Expected:

```text
1 passed
```

---

## Key Takeaways

- Functions can be assigned to variables.
- Functions can be passed as arguments.
- Functions can be returned from other functions.
- Decorators are built using closures.
- `@decorator` syntax is shorthand for:

```python
function = decorator(function)
```

- Decorator factories allow configuration:

```python
@retry(max_attempts=3)
```

is equivalent to:

```python
unstable_function = retry(3)(unstable_function)
```

---

## Files

```text
day02/
├── decorators.py
├── test_decorators.py
└── README.md
```

---

## Validation

```bash
python decorators.py
pytest
```

Result:

```text
All examples executed successfully.
Tests passed.
```