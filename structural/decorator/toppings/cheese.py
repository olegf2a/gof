from ..pizza.decorator import Decorator


class Cheese(Decorator):
    def _get_topping_name(self) -> str:
        return "cheese"

    def _get_topping_price(self) -> float:
        return 1.5
