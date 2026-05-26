"""Weather service — English interface"""

from abc import ABC, abstractmethod


class Weather(ABC):
    @abstractmethod
    def get_temperature(self) -> float: ...

    @abstractmethod
    def get_humidity(self) -> int: ...

    @abstractmethod
    def get_city(self) -> str: ...
