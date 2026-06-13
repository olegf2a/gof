from __future__ import annotations

from typing import TYPE_CHECKING

from ..ingredient import Ingredient

if TYPE_CHECKING:
    from ..visitor import Visitor


class Mushroom(Ingredient):
    @property
    def name(self) -> str:
        return "Mushroom"

    @property
    def price(self) -> float:
        return 1.20

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_mushroom(self)
