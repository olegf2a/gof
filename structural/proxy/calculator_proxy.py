from ..facade.calculator import Calculator  # type: ignore[import-not-found]


class CalculatorProxy(Calculator):
    def __init__(self, calculator: Calculator) -> None:
        self._calculator = calculator
        self._cache: dict[tuple[str, int, int], int] = {}

    def _call(self, operation: str, a: int, b: int) -> int:
        key = (operation, a, b)
        if key not in self._cache:
            self._cache[key] = getattr(self._calculator, operation)(a, b)
        return self._cache[key]

    def add(self, a: int, b: int) -> int:
        return self._call("add", a, b)

    def subtract(self, a: int, b: int) -> int:
        return self._call("subtract", a, b)

    def multiply(self, a: int, b: int) -> int:
        return self._call("multiply", a, b)

    def divide(self, a: int, b: int) -> int:
        return self._call("divide", a, b)
