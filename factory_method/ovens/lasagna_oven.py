"""Lasagna oven implementation - Concrete Creator"""

from .base import Oven
from ..dishes import Lasagna

class LasagnaOven(Oven):
    """Concrete creator for lasagna dishes"""

    def create_dish(self) -> Lasagna:
        """Factory method implementation - creates Lasagna"""
        return Lasagna()