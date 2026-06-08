from collections.abc import Iterable, Iterator
from typing import Any, Callable

from .book_interface import BookInterface


class SortedBookIterator(Iterator):
    """
    Inherits from collections.abc.Iterator.
    Only __next__ is required — __iter__ returning self is inherited.
    """

    def __init__(
        self, books: list[BookInterface], key: Callable[[BookInterface], Any]
    ) -> None:
        self._books = sorted(books, key=key)
        self._index = 0

    def __next__(self) -> BookInterface:
        if self._index >= len(self._books):
            raise StopIteration
        book = self._books[self._index]
        self._index += 1
        return book


class NativeBookCollection(Iterable):
    """
    Inherits from collections.abc.Iterable.
    Only __iter__ is required.
    """

    def __init__(self) -> None:
        self._books: list[BookInterface] = []

    def add(self, book: BookInterface) -> None:
        self._books.append(book)

    def __iter__(self) -> SortedBookIterator:
        return self.by_title()

    def by_author(self) -> SortedBookIterator:
        return SortedBookIterator(self._books, key=lambda b: b.author)

    def by_title(self) -> SortedBookIterator:
        return SortedBookIterator(self._books, key=lambda b: b.title)

    def by_year(self) -> SortedBookIterator:
        return SortedBookIterator(self._books, key=lambda b: b.year)
