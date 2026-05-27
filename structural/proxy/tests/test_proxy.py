"""Unit tests for Proxy pattern — Caching Calculator"""

import unittest
from unittest.mock import MagicMock

from ...facade.calculator import Calculator  # type: ignore[import-not-found]
from ..calculator_proxy import CalculatorProxy


def _make_subject() -> Calculator:
    mock = MagicMock(spec=Calculator)
    mock.add.return_value = 8
    mock.subtract.return_value = 6
    mock.multiply.return_value = 21
    mock.divide.return_value = 5
    return mock


class TestCalculatorProxyInterface(unittest.TestCase):

    def test_implements_calculator(self) -> None:
        proxy = CalculatorProxy(_make_subject())
        self.assertIsInstance(proxy, Calculator)

    def test_add(self) -> None:
        self.assertEqual(CalculatorProxy(_make_subject()).add(5, 3), 8)

    def test_subtract(self) -> None:
        self.assertEqual(CalculatorProxy(_make_subject()).subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(CalculatorProxy(_make_subject()).multiply(3, 7), 21)

    def test_divide(self) -> None:
        self.assertEqual(CalculatorProxy(_make_subject()).divide(20, 4), 5)


class TestCachingBehaviour(unittest.TestCase):

    def setUp(self) -> None:
        self.subject = _make_subject()
        self.proxy = CalculatorProxy(self.subject)

    def test_first_call_forwarded_to_subject(self) -> None:
        self.proxy.add(5, 3)
        self.subject.add.assert_called_once_with(5, 3)

    def test_repeated_call_not_forwarded(self) -> None:
        self.proxy.add(5, 3)
        self.proxy.add(5, 3)
        self.subject.add.assert_called_once()

    def test_repeated_call_returns_cached_result(self) -> None:
        first = self.proxy.add(5, 3)
        second = self.proxy.add(5, 3)
        self.assertEqual(first, second)

    def test_different_arguments_forwarded(self) -> None:
        self.proxy.add(5, 3)
        self.proxy.add(1, 2)
        self.assertEqual(self.subject.add.call_count, 2)

    def test_different_operations_not_shared(self) -> None:
        self.proxy.add(5, 3)
        self.proxy.subtract(5, 3)
        self.subject.add.assert_called_once()
        self.subject.subtract.assert_called_once()

    def test_cache_grows_with_unique_calls(self) -> None:
        self.proxy.add(1, 2)
        self.proxy.add(3, 4)
        self.proxy.subtract(1, 2)
        self.assertEqual(len(self.proxy._cache), 3)

    def test_cache_does_not_grow_on_repeated_calls(self) -> None:
        self.proxy.add(5, 3)
        self.proxy.add(5, 3)
        self.proxy.add(5, 3)
        self.assertEqual(len(self.proxy._cache), 1)

    def test_all_operations_cached_independently(self) -> None:
        self.proxy.add(5, 3)
        self.proxy.subtract(5, 3)
        self.proxy.multiply(5, 3)
        self.proxy.divide(5, 3)
        self.assertEqual(len(self.proxy._cache), 4)
        self.assertEqual(self.subject.add.call_count, 1)
        self.assertEqual(self.subject.subtract.call_count, 1)
        self.assertEqual(self.subject.multiply.call_count, 1)
        self.assertEqual(self.subject.divide.call_count, 1)

    def test_proxy_accepts_any_calculator(self) -> None:
        inner_proxy = CalculatorProxy(self.subject)
        outer_proxy = CalculatorProxy(inner_proxy)
        outer_proxy.add(5, 3)
        self.subject.add.assert_called_once_with(5, 3)


if __name__ == "__main__":
    unittest.main()
