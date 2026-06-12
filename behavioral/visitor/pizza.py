from .ingredient import Ingredient
from .visitor import Visitor


class Pizza:
    def __init__(self) -> None:
        self._ingredients: list[Ingredient] = []

    def add(self, ingredient: Ingredient) -> None:
        self._ingredients.append(ingredient)

    def accept(self, visitor: Visitor) -> None:
        for ingredient in self._ingredients:
            ingredient.accept(visitor)
