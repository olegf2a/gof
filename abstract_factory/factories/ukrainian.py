"""Ukrainian kitchen factory implementation"""

from .base import CuisineFactory
from ..kitchens.ukrainian_dishes import Borscht, Varenyky, Syrniki, Kompot

class UkrainianKitchen(CuisineFactory):
    """Concrete factory for Ukrainian cuisine"""

    def create_main_dish(self):
        return Borscht()

    def create_side_dish(self):
        return Varenyky()

    def create_dessert(self):
        return Syrniki()

    def create_drink(self):
        return Kompot()

    def get_cuisine_name(self) -> str:
        return "Ukrainian"