"""Cookies dish implementation"""

from .base import Dish

class Cookies(Dish):
    """Concrete Cookies product"""

    def __init__(self, cookie_type="chocolate chip", batch_size=24):
        super().__init__(f"{cookie_type.title()} Cookies")
        self.cookie_type = cookie_type
        self.batch_size = batch_size

    def prepare(self) -> str:
        return f"Mixing dough and forming {self.batch_size} {self.cookie_type} cookies"

    def get_cooking_temp(self) -> int:
        return 350

    def get_cooking_time(self) -> int:
        return 15