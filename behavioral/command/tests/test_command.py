import unittest

from ..commands import AddTopping
from ..order import Order
from ..pizza import Pizza


class TestPizza(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()

    def test_initial_state(self) -> None:
        self.assertEqual(self.pizza.get_toppings(), [])
        self.assertEqual(self.pizza.describe(), "Base Pizza (no toppings)")

    def test_add_topping(self) -> None:
        self.pizza.action("cheese")
        self.assertIn("cheese", self.pizza.get_toppings())

    def test_remove_topping(self) -> None:
        self.pizza.action("cheese")
        self.pizza.reverse_action("cheese")
        self.assertNotIn("cheese", self.pizza.get_toppings())

    def test_describe_with_toppings(self) -> None:
        self.pizza.action("cheese")
        self.pizza.action("bacon")
        self.assertEqual(self.pizza.describe(), "Base Pizza, cheese, bacon")

    def test_get_toppings_returns_copy(self) -> None:
        self.pizza.action("cheese")
        toppings = self.pizza.get_toppings()
        toppings.append("mushroom")
        self.assertEqual(self.pizza.get_toppings(), ["cheese"])


class TestAddToppingCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()

    def test_execute_adds_topping(self) -> None:
        cmd = AddTopping(self.pizza, "cheese")
        cmd.execute()
        self.assertIn("cheese", self.pizza.get_toppings())

    def test_undo_removes_topping(self) -> None:
        cmd = AddTopping(self.pizza, "cheese")
        cmd.execute()
        cmd.undo()
        self.assertNotIn("cheese", self.pizza.get_toppings())

    def test_execute_undo_execute(self) -> None:
        cmd = AddTopping(self.pizza, "cheese")
        cmd.execute()
        cmd.undo()
        cmd.execute()
        self.assertEqual(self.pizza.get_toppings(), ["cheese"])


class TestOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()
        self.order = Order(self.pizza)

    def test_run_adds_topping(self) -> None:
        self.order.run("cheese")
        self.assertIn("cheese", self.pizza.get_toppings())

    def test_multiple_toppings(self) -> None:
        self.order.run("cheese")
        self.order.run("bacon")
        self.order.run("mushroom")
        self.assertEqual(self.pizza.get_toppings(), ["cheese", "bacon", "mushroom"])

    def test_undo_removes_last_topping(self) -> None:
        self.order.run("cheese")
        self.order.run("bacon")
        self.order.undo()
        self.assertEqual(self.pizza.get_toppings(), ["cheese"])

    def test_undo_all(self) -> None:
        self.order.run("cheese")
        self.order.run("bacon")
        self.order.undo()
        self.order.undo()
        self.assertEqual(self.pizza.get_toppings(), [])

    def test_undo_empty_history_is_noop(self) -> None:
        self.order.undo()  # should not raise
        self.assertEqual(self.pizza.get_toppings(), [])

    def test_describe_delegates_to_pizza(self) -> None:
        self.order.run("cheese")
        self.assertEqual(self.order.describe(), "Base Pizza, cheese")

    def test_describe_empty(self) -> None:
        self.assertEqual(self.order.describe(), "Base Pizza (no toppings)")

    def test_undo_does_not_exceed_history(self) -> None:
        self.order.run("cheese")
        self.order.undo()
        self.order.undo()  # extra undo — should not raise
        self.assertEqual(self.pizza.get_toppings(), [])


if __name__ == "__main__":
    unittest.main()
