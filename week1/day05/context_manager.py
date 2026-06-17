from contextlib import contextmanager
from pathlib import Path
import time


# ----------------------------------
# CUSTOM CONTEXT MANAGER CLASS
# ----------------------------------

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Timer Started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Timer Stopped: {elapsed:.2f}s")


# ----------------------------------
# CONTEXT MANAGER FUNCTION
# ----------------------------------

@contextmanager
def managed_file(filename: str):
    file = open(filename, "w")

    try:
        yield file
    finally:
        file.close()
        print("File Closed")


# ----------------------------------
# FILE HANDLING WITH PATHLIB
# ----------------------------------

path = Path("sample.txt")

with managed_file("sample.txt") as f:
    f.write("Hello from Context Manager")


print(path.read_text())


# ----------------------------------
# TIMER DEMO
# ----------------------------------

with Timer():
    time.sleep(1)