from __future__ import annotations

from typing import TYPE_CHECKING

from ..ingredient import Ingredient

if TYPE_CHECKING:
    from ..visitor import Visitor


class Cheese(Ingredient):
    @property
    def name(self) -> str:
        return "Cheese"

    @property
    def price(self) -> float:
        return 1.50

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_cheese(self)
