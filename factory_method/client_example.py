#!/usr/bin/env python3
"""
Client example demonstrating the Factory Method pattern
"""
from .dispatcher import get_oven

class Client:
    """Client class that uses the factory method pattern"""

    def main(self):
        """Main method demonstrating different usage scenarios"""
        print("=== Factory Method Pattern Demo ===\n")

        # Scenario 1: Basic usage
        print("1. Basic Usage:")
        self.cook_dish("pizza")
        print()

        # Scenario 2: Multiple dishes
        print("2. Cooking Multiple Dishes:")
        dish_types = ["pizza", "lasagna", "cookies"]
        for dish in dish_types:
            self.cook_dish(dish)
            print("-" * 40)

        # Scenario 3: Error handling
        print("\n3. Error Handling:")
        try:
            self.cook_dish("invalid_dish")
        except ValueError as e:
            print(f"Error: {e}")

    def cook_dish(self, dish_type: str):
        """Cook a specific dish using the appropriate oven"""
        print(f"Client requesting: {dish_type}")

        # Use the factory function to get the right oven
        oven = get_oven(dish_type)
        print(f"Factory returned: {oven.__class__.__name__}")

        # Use the oven to cook (template method)
        result = oven.cook()
        print(result)

if __name__ == "__main__":
    client = Client()
    client.main()