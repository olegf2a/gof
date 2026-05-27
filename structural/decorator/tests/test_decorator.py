"""Unit tests for Decorator pattern — Custom Pizza"""

import unittest

from ..pizza.base import Pizza
from ..pizza.base_pizza import PizzaBase
from ..pizza.decorator import Decorator
from ..toppings import Bacon, Cheese, Mushroom, Pineapple, Seafood


class TestPizzaBase(unittest.TestCase):

    def setUp(self) -> None:
        self.pizza = PizzaBase()

    def test_implements_interface(self) -> None:
        self.assertIsInstance(self.pizza, Pizza)

    def test_description(self) -> None:
        self.assertEqual(self.pizza.get_description(), "Base Pizza")

    def test_price(self) -> None:
        self.assertEqual(self.pizza.get_price(), 5.0)

    def test_pizza_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            Pizza()  # type: ignore[abstract]


class TestToppings(unittest.TestCase):

    def setUp(self) -> None:
        self.base = PizzaBase()

    def test_all_toppings_implement_interface(self) -> None:
        for cls in [Cheese, Bacon, Pineapple, Mushroom, Seafood]:
            self.assertIsInstance(cls(self.base), Pizza)  # type: ignore[abstract]

    def test_all_toppings_are_decorators(self) -> None:
        for cls in [Cheese, Bacon, Pineapple, Mushroom, Seafood]:
            self.assertIsInstance(cls(self.base), Decorator)  # type: ignore[abstract]

    def test_cheese_description(self) -> None:
        self.assertEqual(Cheese(self.base).get_description(), "Base Pizza, cheese")

    def test_bacon_description(self) -> None:
        self.assertEqual(Bacon(self.base).get_description(), "Base Pizza, bacon")

    def test_pineapple_description(self) -> None:
        self.assertEqual(
            Pineapple(self.base).get_description(), "Base Pizza, pineapple"
        )

    def test_mushroom_description(self) -> None:
        self.assertEqual(Mushroom(self.base).get_description(), "Base Pizza, mushroom")

    def test_seafood_description(self) -> None:
        self.assertEqual(Seafood(self.base).get_description(), "Base Pizza, seafood")

    def test_cheese_price(self) -> None:
        self.assertAlmostEqual(Cheese(self.base).get_price(), 6.5)

    def test_bacon_price(self) -> None:
        self.assertAlmostEqual(Bacon(self.base).get_price(), 7.0)

    def test_pineapple_price(self) -> None:
        self.assertAlmostEqual(Pineapple(self.base).get_price(), 6.0)

    def test_mushroom_price(self) -> None:
        self.assertAlmostEqual(Mushroom(self.base).get_price(), 6.5)

    def test_seafood_price(self) -> None:
        self.assertAlmostEqual(Seafood(self.base).get_price(), 7.5)


class TestDecoratorChaining(unittest.TestCase):

    def test_two_toppings_description(self) -> None:
        pizza = Bacon(Cheese(PizzaBase()))
        self.assertEqual(pizza.get_description(), "Base Pizza, cheese, bacon")

    def test_two_toppings_price(self) -> None:
        pizza = Bacon(Cheese(PizzaBase()))
        self.assertAlmostEqual(pizza.get_price(), 8.5)

    def test_all_toppings_chained(self) -> None:
        pizza = Seafood(Mushroom(Pineapple(Bacon(Cheese(PizzaBase())))))
        self.assertEqual(
            pizza.get_description(),
            "Base Pizza, cheese, bacon, pineapple, mushroom, seafood",
        )
        self.assertAlmostEqual(pizza.get_price(), 13.5)

    def test_same_topping_twice(self) -> None:
        pizza = Cheese(Cheese(PizzaBase()))
        self.assertEqual(pizza.get_description(), "Base Pizza, cheese, cheese")
        self.assertAlmostEqual(pizza.get_price(), 8.0)

    def test_order_affects_description(self) -> None:
        pizza_ab = Bacon(Cheese(PizzaBase()))
        pizza_ba = Cheese(Bacon(PizzaBase()))
        self.assertNotEqual(pizza_ab.get_description(), pizza_ba.get_description())


if __name__ == "__main__":
    unittest.main()
