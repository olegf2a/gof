"""International Cafe - Client implementation"""

from .factories.base import CuisineFactory


class Cafe:
    """Client that uses abstract factory to serve meals from different cuisines"""

    def __init__(self, kitchen: CuisineFactory):
        self.kitchen = kitchen
        self.cuisine_name = kitchen.get_cuisine_name()

    def serve_complete_meal(self) -> str:
        """Serve a complete meal using the current kitchen"""
        print(f"\n=== Welcome to {self.cuisine_name} Kitchen ===")

        meal = self.kitchen.create_complete_meal()

        result = []
        result.append(f"🍽️  Complete {self.cuisine_name} Meal:")
        result.append("=" * 40)

        # Prepare main dish
        main = meal["main_dish"]
        result.append(f"🍖 Main Dish: {main.get_name()}")
        result.append(f"   {main.prepare()}")
        result.append(f"   Calories: {main.get_calories()}")

        # Prepare side dish
        side = meal["side_dish"]
        result.append(f"\n🥗 Side Dish: {side.get_name()}")
        result.append(f"   {side.prepare()}")
        result.append(f"   Portion: {side.get_portion_size()}")

        # Prepare dessert
        dessert = meal["dessert"]
        result.append(f"\n🍰 Dessert: {dessert.get_name()}")
        result.append(f"   {dessert.prepare()}")
        result.append(f"   Sweetness: {dessert.get_sweetness_level()}")

        # Prepare drink
        drink = meal["drink"]
        result.append(f"\n🥤 Drink: {drink.get_name()}")
        result.append(f"   {drink.prepare()}")
        result.append(f"   Temperature: {drink.get_temperature()}")

        result.append("\n✅ Your meal is ready! Enjoy!")

        return "\n".join(result)

    def change_kitchen(self, kitchen: CuisineFactory) -> None:
        """Switch to a different cuisine kitchen"""
        self.kitchen = kitchen
        self.cuisine_name = kitchen.get_cuisine_name()
        print(f"Kitchen changed to {self.cuisine_name} cuisine")

    def get_menu_info(self) -> str:
        """Get information about current kitchen's menu"""
        meal = self.kitchen.create_complete_meal()

        info = []
        info.append(f"📋 {self.cuisine_name} Menu:")
        info.append(f"Main Dish: {meal['main_dish'].get_name()}")
        info.append(f"Side Dish: {meal['side_dish'].get_name()}")
        info.append(f"Dessert: {meal['dessert'].get_name()}")
        info.append(f"Drink: {meal['drink'].get_name()}")

        return "\n".join(info)
