from .base import Cuisine


class Italian(Cuisine):
    def get_name(self) -> str:
        return "Italian"

    def prepare_first(self) -> str:
        return "Minestrone soup"

    def prepare_second(self) -> str:
        return "Spaghetti Carbonara"

    def prepare_third(self) -> str:
        return "Patate al forno"

    def prepare_dessert(self) -> str:
        return "Panna Cotta"
