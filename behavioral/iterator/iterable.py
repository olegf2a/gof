from abc import ABC, abstractmethod

from .iterator import Iterator


class Iterable(ABC):
    @abstractmethod
    def create_iterator(self, order: str) -> Iterator: ...
