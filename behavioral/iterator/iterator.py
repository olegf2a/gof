from abc import ABC, abstractmethod
from typing import Any

from .book_interface import BookInterface


class Iterator(ABC):
    def __init__(self, books: list[BookInterface]) -> None:
        self._books = sorted(books, key=self._sort_key)
        self._index = 0

    @abstractmethod
    def _sort_key(self, book: BookInterface) -> Any: ...

    def __iter__(self) -> "Iterator":
        return self

    def __next__(self) -> BookInterface:
        if not self.has_next():
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book

    def has_next(self) -> bool:
        return self._index < len(self._books)
