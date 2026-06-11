def greet(name: str) -> str:
    return f"Hello, {name}"


def add(a: int, b: int) -> int:
    return a + b


print(greet("Deepanshu"))
print(add(10, 20))
def get_student_names() -> list[str]:
    return ["deep1", "deep2", "deep3"]


def get_scores() -> dict[str, int]:
    return {
        "deep1": 95,
        "deep2": 88,
        "deep3": 91,
    }


print(get_student_names())
print(get_scores())

def find_user(user_id: int) -> str | None:
    users = {
        1: "deep1",
        2: "deep2",
        3: "deep3",
    }

    return users.get(user_id)


print(find_user(1))
print(find_user(99))
def process_input(value: str | int) -> str:
    return str(value)


print(process_input("hello"))
print(process_input(100))
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


user = User(
    id=1,
    name="Deepanshu",
    email="deep@gmail.com"

)

print(user)
from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


print(first([1, 2, 3]))
print(first(["a", "b", "c"]))
from typing import Protocol


class Retriever(Protocol):
    def retrieve(self, query: str) -> list[str]:
        ...


class LocalRetriever:
    def retrieve(self, query: str) -> list[str]:
        return [f"Result for {query}"]


def search_docs(retriever: Retriever, query: str) -> list[str]:
    return retriever.retrieve(query)


local = LocalRetriever()

print(search_docs(local, "python"))