from ..ingredients.bacon import Bacon
from ..ingredients.cheese import Cheese
from ..ingredients.mushroom import Mushroom
from ..ingredients.pineapple import Pineapple
from ..ingredients.seafood import Seafood
from ..visitor import Visitor


class PriceVisitor(Visitor):
    def __init__(self) -> None:
        self._total: float = 0.0

    @property
    def total(self) -> float:
        return self._total

    def visit_cheese(self, ingredient: Cheese) -> None:
        self._total += ingredient.price

    def visit_bacon(self, ingredient: Bacon) -> None:
        self._total += ingredient.price

    def visit_pineapple(self, ingredient: Pineapple) -> None:
        self._total += ingredient.price

    def visit_mushroom(self, ingredient: Mushroom) -> None:
        self._total += ingredient.price

    def visit_seafood(self, ingredient: Seafood) -> None:
        self._total += ingredient.price
