"""Abstract product interfaces for dishes"""

from abc import ABC, abstractmethod

class MainDish(ABC):
    """Abstract main dish product"""

    @abstractmethod
    def prepare(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_calories(self) -> int:
        pass

class SideDish(ABC):
    """Abstract side dish product"""

    @abstractmethod
    def prepare(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_portion_size(self) -> str:
        pass

class Dessert(ABC):
    """Abstract dessert product"""

    @abstractmethod
    def prepare(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_sweetness_level(self) -> str:
        pass

class Drink(ABC):
    """Abstract drink product"""

    @abstractmethod
    def prepare(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_temperature(self) -> str:
        pass