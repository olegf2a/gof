from ..pizza.decorator import Decorator


class Bacon(Decorator):
    def _get_topping_name(self) -> str:
        return "bacon"

    def _get_topping_price(self) -> float:
        return 2.0
