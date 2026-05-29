from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def calculate(self, operation: str, a: int, b: int) -> int: ...
