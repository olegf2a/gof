"""Japanese kitchen factory implementation"""

from ..dishes import Dessert, Drink, MainDish, SideDish
from ..kitchens.japanese_dishes import GreenTea, Miso, Mochi, Sushi
from .base import CuisineFactory


class JapaneseKitchen(CuisineFactory):
    """Concrete factory for Japanese cuisine"""

    def create_main_dish(self) -> MainDish:
        return Sushi()

    def create_side_dish(self) -> SideDish:
        return Miso()

    def create_dessert(self) -> Dessert:
        return Mochi()

    def create_drink(self) -> Drink:
        return GreenTea()

    def get_cuisine_name(self) -> str:
        return "Japanese"
