#!/usr/bin/env python3
"""
Extended client demonstration of the Abstract Factory pattern
"""

from .cafe import Cafe
from .factories import JapaneseKitchen, AmericanKitchen, UkrainianKitchen

class CafeManager:
    """Advanced client demonstrating different usage patterns"""

    def __init__(self):
        self.available_kitchens = {
            'japanese': JapaneseKitchen(),
            'american': AmericanKitchen(),
            'ukrainian': UkrainianKitchen()
        }
        self.current_cafe = None

    def open_cafe(self, cuisine_type: str):
        """Open cafe with specific cuisine"""
        if cuisine_type.lower() in self.available_kitchens:
            kitchen = self.available_kitchens[cuisine_type.lower()]
            self.current_cafe = Cafe(kitchen)
            print(f"🎉 Cafe opened with {kitchen.get_cuisine_name()} cuisine!")
            return True
        else:
            print(f"❌ Sorry, {cuisine_type} cuisine is not available")
            return False

    def serve_customer(self, customer_name: str):
        """Serve a customer with current cuisine"""
        if not self.current_cafe:
            print("❌ No cafe is currently open!")
            return

        print(f"\n👨‍🍳 Serving customer: {customer_name}")
        meal_details = self.current_cafe.serve_complete_meal()
        print(meal_details)

    def change_cuisine(self, new_cuisine: str):
        """Change to different cuisine"""
        if new_cuisine.lower() in self.available_kitchens:
            kitchen = self.available_kitchens[new_cuisine.lower()]
            if self.current_cafe:
                self.current_cafe.change_kitchen(kitchen)
                print(f"🔄 Kitchen switched to {kitchen.get_cuisine_name()} cuisine")
            else:
                self.open_cafe(new_cuisine)
            return True
        return False

    def show_available_cuisines(self):
        """Display all available cuisines and their menus"""
        print("\n📋 Available Cuisines:")
        print("=" * 50)

        for cuisine_name, kitchen in self.available_kitchens.items():
            temp_cafe = Cafe(kitchen)
            print(f"\n🍽️  {kitchen.get_cuisine_name().upper()} CUISINE")
            print("-" * 30)
            print(temp_cafe.get_menu_info())

    def daily_special_demo(self):
        """Demonstrate daily specials from different cuisines"""
        print("\n🌟 Today's Daily Specials from Around the World!")
        print("=" * 55)

        daily_specials = [
            ("Monday Special", "japanese"),
            ("Tuesday Special", "american"),
            ("Wednesday Special", "ukrainian")
        ]

        for special_name, cuisine in daily_specials:
            print(f"\n🗓️  {special_name} - {cuisine.title()} Cuisine")
            kitchen = self.available_kitchens[cuisine]
            temp_cafe = Cafe(kitchen)

            # Show just the main dish as special
            meal = kitchen.create_complete_meal()
            main_dish = meal['main_dish']
            print(f"   Featured: {main_dish.get_name()}")
            print(f"   {main_dish.prepare()}")
            print(f"   Calories: {main_dish.get_calories()}")

def main():
    """Demonstrate advanced client usage"""
    print("🌍 International Cafe Management System")
    print("=" * 45)

    manager = CafeManager()

    # Show available cuisines
    manager.show_available_cuisines()

    # Simulate customer interactions
    print("\n" + "🔄" * 25 + "\n")
    print("🎭 Customer Service Simulation")
    print("=" * 35)

    # Customer 1: Japanese food
    manager.open_cafe("japanese")
    manager.serve_customer("Akiko")

    # Customer 2: Wants American food
    print("\n" + "-" * 40)
    print("New customer arrives...")
    manager.change_cuisine("american")
    manager.serve_customer("John")

    # Customer 3: Wants Ukrainian food
    print("\n" + "-" * 40)
    print("Another customer arrives...")
    manager.change_cuisine("ukrainian")
    manager.serve_customer("Oleksandr")

    # Show daily specials
    manager.daily_special_demo()

if __name__ == "__main__":
    main()