from ..pizza.decorator import Decorator


class Pineapple(Decorator):
    def _get_topping_name(self) -> str:
        return "pineapple"

    def _get_topping_price(self) -> float:
        return 1.0
