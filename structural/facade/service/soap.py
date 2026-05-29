from ..soap import RequestBuilder, ResponseParser
from ..transport import Transport
from .service import Service


class SoapService(Service):
    def __init__(
        self,
        transport: Transport,
        request_builder: RequestBuilder,
        response_parser: ResponseParser,
    ) -> None:
        self._transport = transport
        self._request_builder = request_builder
        self._response_parser = response_parser

    def calculate(self, operation: str, a: int, b: int) -> int:
        envelope = self._request_builder.build(operation, a, b)
        xml = self._transport.post(envelope, operation)
        return self._response_parser.parse(operation, xml)
