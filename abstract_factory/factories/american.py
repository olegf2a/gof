"""American kitchen factory implementation"""

from ..dishes import Dessert, Drink, MainDish, SideDish
from ..kitchens.american_dishes import ApplePie, Burger, Cola, Fries
from .base import CuisineFactory


class AmericanKitchen(CuisineFactory):
    """Concrete factory for American cuisine"""

    def create_main_dish(self) -> MainDish:
        return Burger()

    def create_side_dish(self) -> SideDish:
        return Fries()

    def create_dessert(self) -> Dessert:
        return ApplePie()

    def create_drink(self) -> Drink:
        return Cola()

    def get_cuisine_name(self) -> str:
        return "American"
