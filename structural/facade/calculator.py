from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self, a: int, b: int) -> int: ...

    @abstractmethod
    def subtract(self, a: int, b: int) -> int: ...

    @abstractmethod
    def multiply(self, a: int, b: int) -> int: ...

    @abstractmethod
    def divide(self, a: int, b: int) -> int: ...
