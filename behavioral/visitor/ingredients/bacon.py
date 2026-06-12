from __future__ import annotations

from typing import TYPE_CHECKING

from ..ingredient import Ingredient

if TYPE_CHECKING:
    from ..visitor import Visitor


class Bacon(Ingredient):
    @property
    def name(self) -> str:
        return "Bacon"

    @property
    def price(self) -> float:
        return 2.00

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_bacon(self)
