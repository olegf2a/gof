from ..book_interface import BookInterface
from ..iterator import Iterator


class TitleIterator(Iterator):
    def _sort_key(self, book: BookInterface) -> str:
        return book.title
