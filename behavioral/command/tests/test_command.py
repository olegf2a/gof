import unittest

from ..commands import AddTopping, ClearTopping, ItalianCustomToppings, RemoveTopping
from ..order import Order
from ..pizza import Pizza


class TestPizza(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()

    def test_initial_state(self) -> None:
        self.assertEqual(self.pizza.get_actions(), [])
        self.assertEqual(self.pizza.describe(), "Base Pizza (no toppings)")

    def test_action_adds_topping(self) -> None:
        self.pizza.action("cheese")
        self.assertIn("cheese", self.pizza.get_actions())

    def test_reverse_action_removes_topping(self) -> None:
        self.pizza.action("cheese")
        self.pizza.reverse_action("cheese")
        self.assertNotIn("cheese", self.pizza.get_actions())

    def test_clear_actions(self) -> None:
        self.pizza.action("cheese")
        self.pizza.action("bacon")
        self.pizza.clear_actions()
        self.assertEqual(self.pizza.get_actions(), [])

    def test_describe_with_toppings(self) -> None:
        self.pizza.action("cheese")
        self.pizza.action("bacon")
        self.assertEqual(self.pizza.describe(), "Base Pizza, cheese, bacon")

    def test_get_actions_returns_copy(self) -> None:
        self.pizza.action("cheese")
        toppings = self.pizza.get_actions()
        toppings.append("mushroom")
        self.assertEqual(self.pizza.get_actions(), ["cheese"])


class TestAddTopping(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()

    def test_execute_adds_topping(self) -> None:
        AddTopping(self.pizza, "cheese").execute()
        self.assertIn("cheese", self.pizza.get_actions())

    def test_undo_removes_topping(self) -> None:
        cmd = AddTopping(self.pizza, "cheese")
        cmd.execute()
        cmd.undo()
        self.assertNotIn("cheese", self.pizza.get_actions())


class TestRemoveTopping(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()
        self.pizza.action("cheese")

    def test_execute_removes_topping(self) -> None:
        RemoveTopping(self.pizza, "cheese").execute()
        self.assertNotIn("cheese", self.pizza.get_actions())

    def test_undo_restores_topping(self) -> None:
        cmd = RemoveTopping(self.pizza, "cheese")
        cmd.execute()
        cmd.undo()
        self.assertIn("cheese", self.pizza.get_actions())


class TestClearTopping(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()
        for t in ("cheese", "bacon", "mushroom"):
            self.pizza.action(t)

    def test_execute_clears_all(self) -> None:
        ClearTopping(self.pizza).execute()
        self.assertEqual(self.pizza.get_actions(), [])

    def test_undo_restores_all(self) -> None:
        cmd = ClearTopping(self.pizza)
        cmd.execute()
        cmd.undo()
        self.assertEqual(self.pizza.get_actions(), ["cheese", "bacon", "mushroom"])


class TestItalianCustomToppings(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()

    def test_execute_adds_italian_toppings(self) -> None:
        ItalianCustomToppings(self.pizza).execute()
        self.assertEqual(self.pizza.get_actions(), ["Mozzarella", "Olives", "Tomatoes"])

    def test_undo_removes_italian_toppings(self) -> None:
        cmd = ItalianCustomToppings(self.pizza)
        cmd.execute()
        cmd.undo()
        self.assertEqual(self.pizza.get_actions(), [])


class TestOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = Pizza()
        self.order = Order(self.pizza)

    def test_run_executes_command(self) -> None:
        self.order.run(AddTopping(self.pizza, "cheese"))
        self.assertIn("cheese", self.pizza.get_actions())

    def test_multiple_commands(self) -> None:
        self.order.run(AddTopping(self.pizza, "cheese"))
        self.order.run(AddTopping(self.pizza, "bacon"))
        self.order.run(AddTopping(self.pizza, "mushroom"))
        self.assertEqual(self.pizza.get_actions(), ["cheese", "bacon", "mushroom"])

    def test_undo_reverses_last_command(self) -> None:
        self.order.run(AddTopping(self.pizza, "cheese"))
        self.order.run(AddTopping(self.pizza, "bacon"))
        self.order.undo()
        self.assertEqual(self.pizza.get_actions(), ["cheese"])

    def test_undo_all(self) -> None:
        self.order.run(AddTopping(self.pizza, "cheese"))
        self.order.run(AddTopping(self.pizza, "bacon"))
        self.order.undo()
        self.order.undo()
        self.assertEqual(self.pizza.get_actions(), [])

    def test_undo_empty_history_is_noop(self) -> None:
        self.order.undo()
        self.assertEqual(self.pizza.get_actions(), [])

    def test_undo_clear_topping(self) -> None:
        self.order.run(AddTopping(self.pizza, "cheese"))
        self.order.run(ClearTopping(self.pizza))
        self.order.undo()
        self.assertEqual(self.pizza.get_actions(), ["cheese"])

    def test_undo_italian_batch(self) -> None:
        self.order.run(ItalianCustomToppings(self.pizza))
        self.order.undo()
        self.assertEqual(self.pizza.get_actions(), [])

    def test_describe_delegates_to_pizza(self) -> None:
        self.order.run(AddTopping(self.pizza, "cheese"))
        self.assertEqual(self.order.describe(), "Base Pizza, cheese")


if __name__ == "__main__":
    unittest.main()
