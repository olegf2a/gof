import io
import sys
import unittest

from ..ingredient import Ingredient
from ..ingredients.bacon import Bacon
from ..ingredients.cheese import Cheese
from ..ingredients.mushroom import Mushroom
from ..ingredients.pineapple import Pineapple
from ..ingredients.seafood import Seafood
from ..pizza import Pizza
from ..visitors.cook_visitor import CookVisitor
from ..visitors.price_visitor import PriceVisitor


class TestIngredients(unittest.TestCase):
    def test_cheese_name_and_price(self) -> None:
        i = Cheese()
        self.assertEqual(i.name, "Cheese")
        self.assertEqual(i.price, 1.50)

    def test_bacon_name_and_price(self) -> None:
        i = Bacon()
        self.assertEqual(i.name, "Bacon")
        self.assertEqual(i.price, 2.00)

    def test_pineapple_name_and_price(self) -> None:
        i = Pineapple()
        self.assertEqual(i.name, "Pineapple")
        self.assertEqual(i.price, 0.80)

    def test_mushroom_name_and_price(self) -> None:
        i = Mushroom()
        self.assertEqual(i.name, "Mushroom")
        self.assertEqual(i.price, 1.20)

    def test_seafood_name_and_price(self) -> None:
        i = Seafood()
        self.assertEqual(i.name, "Seafood")
        self.assertEqual(i.price, 3.50)


class TestPriceVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()
        self.visitor = PriceVisitor()

    def test_empty_pizza_total_is_zero(self) -> None:
        self.pizza.accept(self.visitor)
        self.assertAlmostEqual(self.visitor.total, 0.0)

    def test_single_ingredient_price(self) -> None:
        self.pizza.add(Cheese())
        self.pizza.accept(self.visitor)
        self.assertAlmostEqual(self.visitor.total, 1.50)

    def test_full_pizza_total(self) -> None:
        for ingredient in [Cheese(), Bacon(), Pineapple(), Mushroom(), Seafood()]:
            self.pizza.add(ingredient)
        self.pizza.accept(self.visitor)
        self.assertAlmostEqual(self.visitor.total, 9.00)

    def test_price_accumulates_across_calls(self) -> None:
        self.pizza.add(Cheese())
        self.pizza.accept(self.visitor)
        self.pizza.accept(self.visitor)
        self.assertAlmostEqual(self.visitor.total, 3.00)


class TestCookVisitor(unittest.TestCase):
    def _capture(self, *ingredients: Ingredient) -> str:
        pizza = Pizza()
        for i in ingredients:
            pizza.add(i)
        captured = io.StringIO()
        sys.stdout = captured
        pizza.accept(CookVisitor())
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_cheese_uses_name(self) -> None:
        self.assertIn("Cheese", self._capture(Cheese()))

    def test_bacon_uses_name(self) -> None:
        self.assertIn("Bacon", self._capture(Bacon()))

    def test_pineapple_uses_name(self) -> None:
        self.assertIn("Pineapple", self._capture(Pineapple()))

    def test_mushroom_uses_name(self) -> None:
        self.assertIn("Mushroom", self._capture(Mushroom()))

    def test_seafood_uses_name(self) -> None:
        self.assertIn("Seafood", self._capture(Seafood()))

    def test_cook_prefix_present(self) -> None:
        self.assertIn("[Cook]", self._capture(Cheese()))

    def test_order_preserved(self) -> None:
        output = self._capture(Cheese(), Bacon(), Seafood())
        self.assertLess(output.index("Cheese"), output.index("Bacon"))
        self.assertLess(output.index("Bacon"), output.index("Seafood"))


class TestPizza(unittest.TestCase):
    def test_accept_dispatches_to_all_ingredients(self) -> None:
        pizza = Pizza()
        for ingredient in [Cheese(), Bacon(), Pineapple(), Mushroom(), Seafood()]:
            pizza.add(ingredient)
        visitor = PriceVisitor()
        pizza.accept(visitor)
        self.assertAlmostEqual(visitor.total, 9.00)

    def test_empty_pizza_accept_is_noop(self) -> None:
        pizza = Pizza()
        visitor = PriceVisitor()
        pizza.accept(visitor)
        self.assertAlmostEqual(visitor.total, 0.0)


if __name__ == "__main__":
    unittest.main()
