from ..book_interface import BookInterface
from ..iterator import Iterator


class AuthorIterator(Iterator):
    def _sort_key(self, book: BookInterface) -> str:
        return book.author
