from abc import ABC, abstractmethod
from typing import List


class TreeElement(ABC):
    """Abstract class for a tree element."""

    @abstractmethod
    def get_children(self) -> List["TreeElement"]: ...

    @abstractmethod
    def get_value(self) -> int: ...

    @abstractmethod
    def increment(self) -> int: ...

    @abstractmethod
    def decrement(self) -> int: ...
