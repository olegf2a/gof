"""Pizza oven implementation - Concrete Creator"""

from .base import Oven
from ..dishes import Pizza

class PizzaOven(Oven):
    """Concrete creator for pizza dishes"""

    def create_dish(self) -> Pizza:
        """Factory method implementation - creates Pizza"""
        return Pizza()