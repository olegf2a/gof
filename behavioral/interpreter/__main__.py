from ..command.order import Order
from ..command.pizza import Pizza
from .context import Context
from .parser import parse


def demo() -> None:
    print("=== Interpreter Pattern — Custom Pizza Recipe String ===\n")

    recipe_str = "add:cheese, add:bacon, add:mushroom, undo, add:pineapple"
    print(f'Recipe: "{recipe_str}"\n')

    receiver = Pizza()
    ctx = Context(Order(receiver), receiver)
    recipe = parse(recipe_str)

    recipe.interpret(ctx)
    print(f"Result: {ctx.describe()}")


if __name__ == "__main__":
    demo()
