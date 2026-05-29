from typing import Callable

from .pizza import Pizza, PizzaBase
from .toppings import Bacon, Cheese, Mushroom, Pineapple, Seafood

TOPPINGS: dict[str, Callable[[Pizza], Pizza]] = {
    "cheese": Cheese,
    "bacon": Bacon,
    "pineapple": Pineapple,
    "mushroom": Mushroom,
    "seafood": Seafood,
}


def show(pizza: Pizza) -> None:
    print(f"  {pizza.get_description()}")
    print(f"  Price: ${pizza.get_price():.2f}")


def demo() -> None:
    print("=== Decorator demo ===\n")

    pizza: Pizza = PizzaBase()
    print("Base:")
    show(pizza)

    pizza = Cheese(pizza)
    print("\n+ Cheese:")
    show(pizza)

    pizza = Bacon(pizza)
    print("\n+ Bacon:")
    show(pizza)

    pizza = Pineapple(pizza)
    print("\n+ Pineapple:")
    show(pizza)


def interactive() -> None:
    print("\n=== Build your pizza ===")
    print(f"Available toppings: {', '.join(TOPPINGS)}\n")

    pizza: Pizza = PizzaBase()

    while True:
        choice = input("Add topping (or 'done'): ").strip().lower()
        if choice == "done":
            break
        if choice in TOPPINGS:
            pizza = TOPPINGS[choice](pizza)
            print(f"  -> {pizza.get_description()}  ${pizza.get_price():.2f}")
        else:
            print(f"  Unknown topping. Choose from: {', '.join(TOPPINGS)}")

    print("\n=== Your pizza ===")
    show(pizza)


def main() -> None:
    demo()
    interactive()


if __name__ == "__main__":
    main()
