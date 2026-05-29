from .order import Order
from .pizza import Pizza


def demo() -> None:
    print("=== Command Pattern — Custom Pizza Order ===\n")

    pizza = Pizza()
    order = Order(pizza)

    print("--- Building the pizza ---")
    for topping in ("cheese", "bacon", "mushroom"):
        order.run(topping)
        print(f"  + {topping:<10}  →  {order.describe()}")

    print("\n--- Undo last topping ---")
    order.undo()
    print(f"  undo         →  {order.describe()}")

    print("\n--- Add pineapple ---")
    order.run("pineapple")
    print(f"  + pineapple  →  {order.describe()}")

    print("\n--- Undo all remaining toppings ---")
    while pizza.get_toppings():
        order.undo()
        print(f"  undo         →  {order.describe()}")

    print("\n--- Undo on empty history is a no-op ---")
    order.undo()
    print(f"  undo         →  {order.describe()}")


if __name__ == "__main__":
    demo()
