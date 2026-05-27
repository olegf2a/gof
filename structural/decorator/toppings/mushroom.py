from ..pizza.decorator import Decorator


class Mushroom(Decorator):
    def _get_topping_name(self) -> str:
        return "mushroom"

    def _get_topping_price(self) -> float:
        return 1.5
