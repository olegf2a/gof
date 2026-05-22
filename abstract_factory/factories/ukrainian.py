"""Ukrainian kitchen factory implementation"""

from ..dishes import Dessert, Drink, MainDish, SideDish
from ..kitchens.ukrainian_dishes import Borscht, Kompot, Syrniki, Varenyky
from .base import CuisineFactory


class UkrainianKitchen(CuisineFactory):
    """Concrete factory for Ukrainian cuisine"""

    def create_main_dish(self) -> MainDish:
        return Borscht()

    def create_side_dish(self) -> SideDish:
        return Varenyky()

    def create_dessert(self) -> Dessert:
        return Syrniki()

    def create_drink(self) -> Drink:
        return Kompot()

    def get_cuisine_name(self) -> str:
        return "Ukrainian"
