"""Demo script for factory_method module"""

from .dispatcher import get_oven

def main():
    """Demonstrate the Factory Method pattern with ovens"""
    dish_types = ['pizza', 'lasagna', 'cookies']

    print("Factory Method Pattern Demo - Oven Factory")
    print("=" * 50)

    for dish_type in dish_types:
        oven = get_oven(dish_type)
        result = oven.cook()
        print(f"{dish_type.capitalize()}: {result}")
        print()

if __name__ == "__main__":
    main()