"""Demo script for factory_method module"""

from creational.factory_method.oven import Oven


def main() -> None:
    """Demonstrate the Factory Method pattern with ovens"""
    print("=== Factory Method Pattern Demo ===\n")

    # Create instances
    print("\nCreating Oven ...")
    oven = Oven()

    # Scenario 1: Basic usage
    print("1. Basic Usage:")
    pizza = oven.cook_dish("pizza")
    print(pizza)

    # Scenario 2: Multiple dishes
    print("2. Cooking Multiple Dishes:")
    dish_types = ["pizza", "lasagna", "cookies"]
    for dish_type in dish_types:
        dish = oven.cook_dish(dish_type)
        print(dish)
        print("-" * 40)


if __name__ == "__main__":
    main()
