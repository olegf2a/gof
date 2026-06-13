from __future__ import annotations

from typing import TYPE_CHECKING

from ..ingredient import Ingredient

if TYPE_CHECKING:
    from ..visitor import Visitor


class Seafood(Ingredient):
    @property
    def name(self) -> str:
        return "Seafood"

    @property
    def price(self) -> float:
        return 3.50

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_seafood(self)
