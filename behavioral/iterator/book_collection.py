from .book import BookInterface
from .iterable import Iterable
from .iterator import Iterator
from .iterators import AuthorIterator, TitleIterator, YearIterator


class BookCollection(Iterable):
    def __init__(self) -> None:
        self._books: list[BookInterface] = []

    def add(self, book: BookInterface) -> None:
        self._books.append(book)

    def create_iterator(self, order: str) -> Iterator:
        match order:
            case "author":
                return AuthorIterator(self._books)
            case "title":
                return TitleIterator(self._books)
            case "year":
                return YearIterator(self._books)
            case _:
                raise ValueError(f"Unknown order: '{order}'")
