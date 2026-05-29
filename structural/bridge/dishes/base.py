from abc import ABC, abstractmethod

from ..cuisine.base import Cuisine


class Dish(ABC):
    def __init__(self, cuisine: Cuisine):
        self._cuisine = cuisine

    @abstractmethod
    def get_course_name(self) -> str: ...

    @abstractmethod
    def serve(self) -> str: ...
