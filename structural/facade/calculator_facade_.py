from .calculator import Calculator
from .service import Service


class CalculatorFacade(Calculator):
    def __init__(self, service: Service) -> None:
        self._service = service

    def add(self, a: int, b: int) -> int:
        return self._service.calculate("Add", a, b)

    def subtract(self, a: int, b: int) -> int:
        return self._service.calculate("Subtract", a, b)

    def multiply(self, a: int, b: int) -> int:
        return self._service.calculate("Multiply", a, b)

    def divide(self, a: int, b: int) -> int:
        return self._service.calculate("Divide", a, b)
