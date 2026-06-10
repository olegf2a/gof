from abc import ABC, abstractmethod

from .memento import Memento


class Originator(ABC):
    @abstractmethod
    def save(self) -> Memento: ...

    @abstractmethod
    def restore(self, memento: Memento) -> None: ...
