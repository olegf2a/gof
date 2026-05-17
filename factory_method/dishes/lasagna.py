"""Lasagna dish implementation"""

from .base import Dish

class Lasagna(Dish):
    """Concrete Lasagna product"""

    def __init__(self, layers=6):
        super().__init__(f"{layers}-Layer Lasagna")
        self.layers = layers

    def prepare(self) -> str:
        return f"Layering pasta, sauce, cheese, and meat ({self.layers} layers)"

    def get_cooking_temp(self) -> int:
        return 375

    def get_cooking_time(self) -> int:
        return 45