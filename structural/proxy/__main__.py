from unittest.mock import MagicMock

from ..facade.calculator import Calculator  # type: ignore[import-not-found]
from .calculator_proxy import CalculatorProxy


def _make_facade_mock() -> MagicMock:
    mock = MagicMock(spec=Calculator)
    mock.add.return_value = 8
    mock.subtract.return_value = 6
    mock.multiply.return_value = 21
    mock.divide.return_value = 5
    return mock


def demo() -> None:
    print("=== Proxy demo — Caching Calculator ===\n")

    facade = _make_facade_mock()
    proxy = CalculatorProxy(facade)

    print("--- First calls (cache miss → forwarded to facade) ---")
    print(f"  add(5, 3)       = {proxy.add(5, 3)}")
    print(f"  subtract(10, 4) = {proxy.subtract(10, 4)}")
    print(f"  multiply(3, 7)  = {proxy.multiply(3, 7)}")
    print(f"  divide(20, 4)   = {proxy.divide(20, 4)}")
    print(
        f"\n  Facade calls made: {facade.add.call_count + facade.subtract.call_count + facade.multiply.call_count + facade.divide.call_count}"
    )

    print("\n--- Repeated calls (cache hit → facade NOT called) ---")
    print(f"  add(5, 3)       = {proxy.add(5, 3)}")
    print(f"  subtract(10, 4) = {proxy.subtract(10, 4)}")
    print(f"  multiply(3, 7)  = {proxy.multiply(3, 7)}")
    print(f"  divide(20, 4)   = {proxy.divide(20, 4)}")
    print(
        f"\n  Facade calls made: {facade.add.call_count + facade.subtract.call_count + facade.multiply.call_count + facade.divide.call_count} (unchanged)"
    )

    print("\n--- Different arguments (cache miss → forwarded again) ---")
    facade.add.return_value = 12
    print(f"  add(10, 2)      = {proxy.add(10, 2)}")
    print(f"\n  Facade add calls total: {facade.add.call_count}")
    print(f"  Cache size: {len(proxy._cache)} entries")


if __name__ == "__main__":
    demo()
