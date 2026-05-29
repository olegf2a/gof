from ..pizza.decorator import Decorator


class Seafood(Decorator):
    def _get_topping_name(self) -> str:
        return "seafood"

    def _get_topping_price(self) -> float:
        return 2.5
