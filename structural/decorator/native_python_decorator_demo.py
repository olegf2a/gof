"""
Native Python decorator implementation of the pizza topping example.

Python's @decorator syntax wraps a function/class at definition time.
This is conceptually similar to the GoF Decorator pattern but operates
on callables rather than objects sharing an interface.

Key difference from the GoF version:

  ┌─────────┬──────────────────────────────┬─────────────────────────────────────────┐
  │         │     GoF Decorator (OOP)      │            Python @decorator            │
  ├─────────┼──────────────────────────────┼─────────────────────────────────────────┤
  │ Wraps   │ objects sharing an interface │ callables                               │
  ├─────────┼──────────────────────────────┼─────────────────────────────────────────┤
  │ Applied │ at runtime, dynamically      │ at definition time (static) or manually │
  ├─────────┼──────────────────────────────┼─────────────────────────────────────────┤
  │ Order   │ outer wraps inner            │ bottom decorator applies first          │
  ├─────────┼──────────────────────────────┼─────────────────────────────────────────┤
  │ State   │ each wrapper is an object    │ closures                                │
  └─────────┴──────────────────────────────┴─────────────────────────────────────────┘
"""

from functools import wraps
from typing import Callable

PizzaFunc = Callable[[], tuple[str, float]]
Topping = Callable[[PizzaFunc], PizzaFunc]


def cheese(func: PizzaFunc) -> PizzaFunc:
    @wraps(func)
    def wrapper() -> tuple[str, float]:
        description, price = func()
        return description + ", cheese", price + 1.5

    return wrapper


def bacon(func: PizzaFunc) -> PizzaFunc:
    @wraps(func)
    def wrapper() -> tuple[str, float]:
        description, price = func()
        return description + ", bacon", price + 2.0

    return wrapper


def pineapple(func: PizzaFunc) -> PizzaFunc:
    @wraps(func)
    def wrapper() -> tuple[str, float]:
        description, price = func()
        return description + ", pineapple", price + 1.0

    return wrapper


def mushroom(func: PizzaFunc) -> PizzaFunc:
    @wraps(func)
    def wrapper() -> tuple[str, float]:
        description, price = func()
        return description + ", mushroom", price + 1.5

    return wrapper


def seafood(func: PizzaFunc) -> PizzaFunc:
    @wraps(func)
    def wrapper() -> tuple[str, float]:
        description, price = func()
        return description + ", seafood", price + 2.5

    return wrapper


# ── applying decorators statically at definition time ──────────────────


@cheese
@bacon
@pineapple
def hawaiian_pizza() -> tuple[str, float]:
    return "Base Pizza", 5.0


@cheese
@mushroom
@seafood
def seafood_pizza() -> tuple[str, float]:
    return "Base Pizza", 5.0


# ── applying decorators dynamically at runtime ──────────────────────────


def make_pizza(*toppings: str) -> PizzaFunc:
    """Build a pizza by applying topping decorators dynamically."""
    available: dict[str, Topping] = {
        "cheese": cheese,
        "bacon": bacon,
        "pineapple": pineapple,
        "mushroom": mushroom,
        "seafood": seafood,
    }

    def base() -> tuple[str, float]:
        return "Base Pizza", 5.0

    pizza = base
    for topping in toppings:
        pizza = available[topping](pizza)
    return pizza


if __name__ == "__main__":
    print("=== Static decorators ===")
    desc, price = hawaiian_pizza()
    print(f"  {desc}  ${price:.2f}")

    desc, price = seafood_pizza()
    print(f"  {desc}  ${price:.2f}")

    print("\n=== Dynamic decorators ===")
    custom = make_pizza("cheese", "bacon", "pineapple")
    desc, price = custom()
    print(f"  {desc}  ${price:.2f}")
