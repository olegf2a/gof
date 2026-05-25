from .dishes import Cookies, Lasagna, Pizza

DishType = type[Pizza] | type[Lasagna] | type[Cookies]


class Oven:

    def _create_dish(self, dish_type: str) -> Pizza | Lasagna | Cookies:
        """Factory method to get concrete dish according to the dish type"""

        dish_map: dict[str, DishType] = {
            "pizza": Pizza,
            "lasagna": Lasagna,
            "cookies": Cookies,
        }

        dish_type = dish_type.lower()
        if dish_type not in dish_map:
            raise ValueError(f"Unknown dish type: {dish_type}")

        return dish_map[dish_type]()

    def cook_dish(self, dish_type: str) -> str:
        """Template method that defines the cooking process"""
        dish = self._create_dish(dish_type)

        preparation = dish.prepare()
        temp = dish.get_cooking_temp()
        time = dish.get_cooking_time()

        return (
            f"Cooking {dish.name}:\n"
            f"  1. {preparation}\n"
            f"  2. Preheating oven to {temp}°F\n"
            f"  3. Cooking for {time} minutes\n"
            f"  4. Done! Your {dish.name} is ready!"
        )
