"""American cuisine dish implementations"""

from ..dishes import Dessert, Drink, MainDish, SideDish


class Burger(MainDish):
    """Classic American main dish"""

    def prepare(self) -> str:
        return "Grilling beef patty and assembling classic cheeseburger"

    def get_name(self) -> str:
        return "Classic Cheeseburger"

    def get_calories(self) -> int:
        return 650


class Fries(SideDish):
    """American side dish"""

    def prepare(self) -> str:
        return "Deep-frying golden crispy french fries"

    def get_name(self) -> str:
        return "French Fries"

    def get_portion_size(self) -> str:
        return "Large portion (200g)"


class ApplePie(Dessert):
    """Traditional American dessert"""

    def prepare(self) -> str:
        return "Baking homemade apple pie with cinnamon and flaky crust"

    def get_name(self) -> str:
        return "Apple Pie"

    def get_sweetness_level(self) -> str:
        return "Sweet with cinnamon"


class Cola(Drink):
    """American beverage"""

    def prepare(self) -> str:
        return "Serving ice-cold cola with fresh ice"

    def get_name(self) -> str:
        return "Classic Cola"

    def get_temperature(self) -> str:
        return "Cold with ice"
