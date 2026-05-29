from abc import ABC, abstractmethod


class Cuisine(ABC):
    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def prepare_first(self) -> str: ...

    @abstractmethod
    def prepare_second(self) -> str: ...

    @abstractmethod
    def prepare_third(self) -> str: ...

    @abstractmethod
    def prepare_dessert(self) -> str: ...
