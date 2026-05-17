"""Japanese kitchen factory implementation"""

from .base import CuisineFactory
from ..kitchens.japanese_dishes import Sushi, Miso, Mochi, GreenTea

class JapaneseKitchen(CuisineFactory):
    """Concrete factory for Japanese cuisine"""

    def create_main_dish(self):
        return Sushi()

    def create_side_dish(self):
        return Miso()

    def create_dessert(self):
        return Mochi()

    def create_drink(self):
        return GreenTea()

    def get_cuisine_name(self) -> str:
        return "Japanese"