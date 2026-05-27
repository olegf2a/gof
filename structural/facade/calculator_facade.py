from .soap.client import SoapClient
from .soap.request_builder import RequestBuilder
from .soap.response_parser import ResponseParser


class CalculatorFacade:
    def __init__(self) -> None:
        self._client = SoapClient()
        self._builder = RequestBuilder()
        self._parser = ResponseParser()

    def _call(self, operation: str, a: int, b: int) -> int:
        envelope = self._builder.build(operation, a, b)
        xml = self._client.call(envelope, operation)
        return self._parser.parse(operation, xml)

    def add(self, a: int, b: int) -> int:
        return self._call("Add", a, b)

    def subtract(self, a: int, b: int) -> int:
        return self._call("Subtract", a, b)

    def multiply(self, a: int, b: int) -> int:
        return self._call("Multiply", a, b)

    def divide(self, a: int, b: int) -> int:
        return self._call("Divide", a, b)
