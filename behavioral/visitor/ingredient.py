from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .visitor import Visitor


class Ingredient(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def price(self) -> float: ...

    @abstractmethod
    def accept(self, visitor: Visitor) -> None: ...
