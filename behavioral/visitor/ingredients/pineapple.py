from __future__ import annotations

from typing import TYPE_CHECKING

from ..ingredient import Ingredient

if TYPE_CHECKING:
    from ..visitor import Visitor


class Pineapple(Ingredient):
    @property
    def name(self) -> str:
        return "Pineapple"

    @property
    def price(self) -> float:
        return 0.80

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_pineapple(self)
