from dataclasses import dataclass

from .book_interface import BookInterface


@dataclass
class Book(BookInterface):
    author: str
    title: str
    year: int

    def __str__(self) -> str:
        return f"{self.author:<20} | {self.title:<35} | {self.year}"
