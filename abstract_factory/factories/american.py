"""American kitchen factory implementation"""

from .base import CuisineFactory
from ..kitchens.american_dishes import Burger, Fries, ApplePie, Cola

class AmericanKitchen(CuisineFactory):
    """Concrete factory for American cuisine"""

    def create_main_dish(self):
        return Burger()

    def create_side_dish(self):
        return Fries()

    def create_dessert(self):
        return ApplePie()

    def create_drink(self):
        return Cola()

    def get_cuisine_name(self) -> str:
        return "American"