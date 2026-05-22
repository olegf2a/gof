"""Abstract factory interface for cuisine kitchens"""

from abc import ABC, abstractmethod
from ..dishes import MainDish, SideDish, Dessert, Drink

class CuisineFactory(ABC):
    """Abstract factory for creating complete meals from different cuisines"""

    @abstractmethod
    def create_main_dish(self) -> MainDish:
        """Create a traditional main dish"""
        pass

    @abstractmethod
    def create_side_dish(self) -> SideDish:
        """Create a traditional side dish"""
        pass

    @abstractmethod
    def create_dessert(self) -> Dessert:
        """Create a traditional dessert"""
        pass

    @abstractmethod
    def create_drink(self) -> Drink:
        """Create a traditional drink"""
        pass

    def create_complete_meal(self) -> dict:
        """Create a complete meal with all components"""
        return {
            'main_dish': self.create_main_dish(),
            'side_dish': self.create_side_dish(),
            'dessert': self.create_dessert(),
            'drink': self.create_drink()
        }

    @abstractmethod
    def get_cuisine_name(self) -> str:
        """Get the name of this cuisine"""
        pass