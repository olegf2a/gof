from .commands import AddTopping, ClearTopping, ItalianCustomToppings, RemoveTopping
from .order import Order
from .pizza import Pizza


def demo() -> None:
    print("=== Command Pattern — Custom Pizza Order ===\n")

    pizza = Pizza()
    order = Order(pizza)

    print("--- Adding toppings ---")
    for topping in ("cheese", "bacon", "mushroom"):
        order.run(AddTopping(pizza, topping))
        print(f"  + {topping:<10}  →  {order.describe()}")

    print("\n--- Remove bacon ---")
    order.run(RemoveTopping(pizza, "bacon"))
    print(f"  - bacon        →  {order.describe()}")

    print("\n--- Undo remove ---")
    order.undo()
    print(f"  undo           →  {order.describe()}")

    print("\n--- Add Italian toppings (batch) ---")
    order.run(ItalianCustomToppings(pizza))
    print(f"  + italian      →  {order.describe()}")

    print("\n--- Undo Italian batch ---")
    order.undo()
    print(f"  undo           →  {order.describe()}")

    print("\n--- Clear all toppings ---")
    order.run(ClearTopping(pizza))
    print(f"  clear          →  {order.describe()}")

    print("\n--- Undo clear ---")
    order.undo()
    print(f"  undo           →  {order.describe()}")

    print("\n--- Undo on empty history is a no-op ---")
    while pizza.get_actions():
        order.undo()
    order.undo()
    print(f"  undo           →  {order.describe()}")


if __name__ == "__main__":
    demo()
