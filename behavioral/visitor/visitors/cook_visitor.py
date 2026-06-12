from ..ingredients.bacon import Bacon
from ..ingredients.cheese import Cheese
from ..ingredients.mushroom import Mushroom
from ..ingredients.pineapple import Pineapple
from ..ingredients.seafood import Seafood
from ..visitor import Visitor


class CookVisitor(Visitor):
    def visit_cheese(self, ingredient: Cheese) -> None:
        print(f"[Cook] {ingredient.name}: melting on the base.")

    def visit_bacon(self, ingredient: Bacon) -> None:
        print(f"[Cook] {ingredient.name}: frying until crispy.")

    def visit_pineapple(self, ingredient: Pineapple) -> None:
        print(f"[Cook] {ingredient.name}: adding fresh chunks.")

    def visit_mushroom(self, ingredient: Mushroom) -> None:
        print(f"[Cook] {ingredient.name}: sautéing.")

    def visit_seafood(self, ingredient: Seafood) -> None:
        print(f"[Cook] {ingredient.name}: grilling.")
