import unittest

from ...command.order import Order
from ...command.pizza import Pizza
from ..context import Context
from ..expressions import AddExpression, RecipeExpression, UndoExpression
from ..parser import parse


def _make_ctx() -> Context:
    pizza = Pizza()
    return Context(Order(pizza), pizza)


class TestAddExpression(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = _make_ctx()

    def test_adds_topping(self) -> None:
        AddExpression("cheese").interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza, cheese")

    def test_adds_multiple_toppings(self) -> None:
        AddExpression("cheese").interpret(self.ctx)
        AddExpression("bacon").interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza, cheese, bacon")


class TestUndoExpression(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = _make_ctx()

    def test_removes_last_topping(self) -> None:
        AddExpression("cheese").interpret(self.ctx)
        AddExpression("bacon").interpret(self.ctx)
        UndoExpression().interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza, cheese")

    def test_undo_on_empty_is_noop(self) -> None:
        UndoExpression().interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza (no toppings)")


class TestRecipeExpression(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = _make_ctx()

    def test_sequence_of_expressions(self) -> None:
        recipe = RecipeExpression(
            [
                AddExpression("cheese"),
                AddExpression("bacon"),
                UndoExpression(),
                AddExpression("mushroom"),
            ]
        )
        recipe.interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza, cheese, mushroom")

    def test_empty_recipe(self) -> None:
        RecipeExpression([]).interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza (no toppings)")


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = _make_ctx()

    def test_parse_single_add(self) -> None:
        parse("add:cheese").interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza, cheese")

    def test_parse_add_and_undo(self) -> None:
        parse("add:cheese, add:bacon, undo, add:mushroom").interpret(self.ctx)
        self.assertEqual(self.ctx.describe(), "Base Pizza, cheese, mushroom")

    def test_parse_unknown_token_raises(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown instruction"):
            parse("add:cheese, remove:bacon")

    def test_parse_returns_recipe_expression(self) -> None:
        result = parse("add:cheese, undo")
        self.assertIsInstance(result, RecipeExpression)


if __name__ == "__main__":
    unittest.main()
