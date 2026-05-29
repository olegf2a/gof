from .base import Pizza


class PizzaBase(Pizza):
    def get_description(self) -> str:
        return "Base Pizza"

    def get_price(self) -> float:
        return 5.0
