"""Base dish class - Abstract Product"""

from abc import ABC, abstractmethod

class Dish(ABC):
    """Abstract base class for all dishes"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def prepare(self) -> str:
        """Prepare the dish"""
        pass

    @abstractmethod
    def get_cooking_temp(self) -> int:
        """Get the required cooking temperature in Fahrenheit"""
        pass

    @abstractmethod
    def get_cooking_time(self) -> int:
        """Get the required cooking time in minutes"""
        pass

    def __str__(self):
        return f"{self.name}"