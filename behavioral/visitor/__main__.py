from .ingredients.bacon import Bacon
from .ingredients.cheese import Cheese
from .ingredients.mushroom import Mushroom
from .ingredients.pineapple import Pineapple
from .ingredients.seafood import Seafood
from .pizza import Pizza
from .visitors.cook_visitor import CookVisitor
from .visitors.price_visitor import PriceVisitor


def demo() -> None:
    print("=== Visitor Pattern — Custom Pizza Recipe ===\n")

    pizza = Pizza()
    pizza.add(Cheese())
    pizza.add(Bacon())
    pizza.add(Pineapple())
    pizza.add(Mushroom())
    pizza.add(Seafood())

    print("--- Recipe ---")
    price = PriceVisitor()
    pizza.accept(price)
    for ingredient in [Cheese(), Bacon(), Pineapple(), Mushroom(), Seafood()]:
        print(f"  {ingredient.name:<12} ${ingredient.price:.2f}")
    print(f"  {'Total':<12} ${price.total:.2f}")

    print("\n--- Cooking ---")
    pizza.accept(CookVisitor())


if __name__ == "__main__":
    demo()
