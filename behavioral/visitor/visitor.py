from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ingredients.bacon import Bacon
    from .ingredients.cheese import Cheese
    from .ingredients.mushroom import Mushroom
    from .ingredients.pineapple import Pineapple
    from .ingredients.seafood import Seafood


class Visitor(ABC):
    @abstractmethod
    def visit_cheese(self, ingredient: Cheese) -> None: ...

    @abstractmethod
    def visit_bacon(self, ingredient: Bacon) -> None: ...

    @abstractmethod
    def visit_pineapple(self, ingredient: Pineapple) -> None: ...

    @abstractmethod
    def visit_mushroom(self, ingredient: Mushroom) -> None: ...

    @abstractmethod
    def visit_seafood(self, ingredient: Seafood) -> None: ...
