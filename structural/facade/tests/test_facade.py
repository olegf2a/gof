"""Unit tests for Facade pattern — SOAP Calculator"""

import unittest
from unittest.mock import MagicMock

from ..calculator_facade import CalculatorFacade
from ..service.service import Service
from ..soap.request_builder import RequestBuilder
from ..soap.response_parser import ResponseParser


def _make_response_xml(operation: str, value: int) -> str:
    ns = "http://tempuri.org/"
    return (
        f'<?xml version="1.0" encoding="utf-8"?>'
        f'<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
        f"<soap:Body>"
        f'<{operation}Response xmlns="{ns}">'
        f"<{operation}Result>{value}</{operation}Result>"
        f"</{operation}Response>"
        f"</soap:Body>"
        f"</soap:Envelope>"
    )


class TestRequestBuilder(unittest.TestCase):

    def setUp(self) -> None:
        self.builder = RequestBuilder()

    def test_build_contains_operation(self) -> None:
        envelope = self.builder.build("Add", 5, 3)
        self.assertIn("<Add", envelope)
        self.assertIn("</Add>", envelope)

    def test_build_contains_values(self) -> None:
        envelope = self.builder.build("Add", 5, 3)
        self.assertIn("<intA>5</intA>", envelope)
        self.assertIn("<intB>3</intB>", envelope)

    def test_build_contains_namespace(self) -> None:
        envelope = self.builder.build("Add", 5, 3)
        self.assertIn("http://tempuri.org/", envelope)

    def test_build_is_valid_xml(self) -> None:
        import xml.etree.ElementTree as ET

        envelope = self.builder.build("Multiply", 4, 6)
        ET.fromstring(envelope)  # raises if invalid


class TestResponseParser(unittest.TestCase):

    def setUp(self) -> None:
        self.parser = ResponseParser()

    def test_parse_add_result(self) -> None:
        xml = _make_response_xml("Add", 8)
        self.assertEqual(self.parser.parse("Add", xml), 8)

    def test_parse_subtract_result(self) -> None:
        xml = _make_response_xml("Subtract", 6)
        self.assertEqual(self.parser.parse("Subtract", xml), 6)

    def test_parse_multiply_result(self) -> None:
        xml = _make_response_xml("Multiply", 21)
        self.assertEqual(self.parser.parse("Multiply", xml), 21)

    def test_parse_divide_result(self) -> None:
        xml = _make_response_xml("Divide", 5)
        self.assertEqual(self.parser.parse("Divide", xml), 5)

    def test_parse_raises_on_missing_element(self) -> None:
        with self.assertRaises(ValueError):
            self.parser.parse("Add", "<soap:Envelope/>")


class TestCalculatorFacade(unittest.TestCase):

    def setUp(self) -> None:
        self.service = MagicMock(spec=Service)
        self.facade = CalculatorFacade(service=self.service)

    def test_add(self) -> None:
        self.service.calculate.return_value = 8
        self.assertEqual(self.facade.add(5, 3), 8)
        self.service.calculate.assert_called_once_with("Add", 5, 3)

    def test_subtract(self) -> None:
        self.service.calculate.return_value = 6
        self.assertEqual(self.facade.subtract(10, 4), 6)
        self.service.calculate.assert_called_once_with("Subtract", 10, 4)

    def test_multiply(self) -> None:
        self.service.calculate.return_value = 21
        self.assertEqual(self.facade.multiply(3, 7), 21)
        self.service.calculate.assert_called_once_with("Multiply", 3, 7)

    def test_divide(self) -> None:
        self.service.calculate.return_value = 5
        self.assertEqual(self.facade.divide(20, 4), 5)
        self.service.calculate.assert_called_once_with("Divide", 20, 4)

    def test_hides_soap_complexity(self) -> None:
        self.service.calculate.return_value = 12
        result = self.facade.multiply(3, 4)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
