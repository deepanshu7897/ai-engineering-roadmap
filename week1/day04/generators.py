from typing import Iterator


# ----------------------------------
# GENERATOR FUNCTION
# ----------------------------------

def count_up_to(limit: int) -> Iterator[int]:
    for i in range(1, limit + 1):
        yield i


# ----------------------------------
# GENERATOR EXPRESSION
# ----------------------------------

squares = (x * x for x in range(5))


# ----------------------------------
# CUSTOM ITERATOR
# ----------------------------------

class NumberIterator:
    def __init__(self, max_num: int):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


# ----------------------------------
# LARGE DATA GENERATOR
# ----------------------------------

def process_large_dataset(
    size: int,
) -> Iterator[int]:
    for i in range(size):
        yield i * 2


# ----------------------------------
# RUN EXAMPLES
# ----------------------------------

print("Generator Function")

for num in count_up_to(5):
    print(num)

print("\nGenerator Expression")

for value in squares:
    print(value)

print("\nCustom Iterator")

for value in NumberIterator(5):
    print(value)

print("\nLarge Dataset")

for value in process_large_dataset(5):
    print(value)