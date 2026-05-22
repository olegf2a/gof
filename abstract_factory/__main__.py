"""Demo script for International Cafe - Abstract Factory Pattern"""

from .cafe import Cafe
from .factories import AmericanKitchen, JapaneseKitchen, UkrainianKitchen


def main() -> None:
    """Demonstrate the Abstract Factory pattern with international cuisine"""
    print("🌍 International Cafe - Abstract Factory Pattern Demo")
    print("=" * 60)

    # Create different kitchen factories
    kitchens = [JapaneseKitchen(), AmericanKitchen(), UkrainianKitchen()]

    # Create cafe instance
    cafe = Cafe(kitchens[0])  # Start with Japanese

    # Demonstrate serving meals from each cuisine
    for kitchen in kitchens:
        cafe.change_kitchen(kitchen)

        # Show menu
        print(f"\n{cafe.get_menu_info()}")

        # Serve complete meal
        meal_details = cafe.serve_complete_meal()
        print(meal_details)

        print("\n" + "🔄" * 20 + "\n")

    # Demonstrate dynamic kitchen switching
    print("🎯 Demonstration: Customer requests different cuisines")
    print("=" * 55)

    customer_requests = [
        ("Japanese", JapaneseKitchen()),
        ("American", AmericanKitchen()),
        ("Ukrainian", UkrainianKitchen()),
        ("Japanese", JapaneseKitchen()),  # Switch back
    ]

    for cuisine_name, kitchen in customer_requests:
        print(f"\nCustomer: 'I'd like {cuisine_name} food, please!'")
        cafe.change_kitchen(kitchen)
        print(cafe.get_menu_info())
        print()


if __name__ == "__main__":
    main()
