"""Pizza dish implementation"""

from .base import Dish


class Pizza(Dish):
    """Concrete Pizza product"""

    def __init__(self, toppings: str = "margherita") -> None:
        super().__init__(f"{toppings.capitalize()} Pizza")
        self.toppings = toppings

    def prepare(self) -> str:
        return f"Rolling dough and adding {self.toppings} toppings"

    def get_cooking_temp(self) -> int:
        return 450

    def get_cooking_time(self) -> int:
        return 12
