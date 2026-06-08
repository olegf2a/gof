from abc import ABC, abstractmethod


class BookInterface(ABC):
    author: str
    title: str
    year: int

    @abstractmethod
    def __str__(self) -> str: ...
