"""Base oven class - Abstract Creator with template method"""

from abc import ABC, abstractmethod

class Oven(ABC):
    """Abstract base class for all ovens - implements Factory Method pattern"""

    def cook(self) -> str:
        """Template method that defines the cooking process"""
        dish = self.create_dish()

        preparation = dish.prepare()
        temp = dish.get_cooking_temp()
        time = dish.get_cooking_time()

        return (
            f"Cooking {dish.name}:\n"
            f"  1. {preparation}\n"
            f"  2. Preheating oven to {temp}°F\n"
            f"  3. Cooking for {time} minutes\n"
            f"  4. Done! Your {dish.name} is ready!"
        )

    @abstractmethod
    def create_dish(self):
        """Factory method - subclasses must implement this"""
        pass