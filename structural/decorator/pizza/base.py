from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str: ...

    @abstractmethod
    def get_price(self) -> float: ...
