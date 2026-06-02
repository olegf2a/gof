from ..book_interface import BookInterface
from ..iterator import Iterator


class YearIterator(Iterator):
    def _sort_key(self, book: BookInterface) -> int:
        return book.year
