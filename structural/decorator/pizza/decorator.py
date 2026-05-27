from abc import ABC, abstractmethod

from .base import Pizza


class Decorator(Pizza, ABC):
    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza

    @abstractmethod
    def _get_topping_name(self) -> str: ...

    @abstractmethod
    def _get_topping_price(self) -> float: ...

    def get_description(self) -> str:
        return self._pizza.get_description() + ", " + self._get_topping_name()

    def get_price(self) -> float:
        return self._pizza.get_price() + self._get_topping_price()
