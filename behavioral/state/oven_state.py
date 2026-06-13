from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pizza_oven import PizzaOven


class OvenState(ABC):
    @abstractmethod
    def heat_up(self, context: PizzaOven) -> None: ...

    @abstractmethod
    def cool_down(self, context: PizzaOven) -> None: ...

    @abstractmethod
    def bake(self, context: PizzaOven, pizza: str) -> None: ...

    @abstractmethod
    def name(self) -> str: ...
