from .calculator_facade import CalculatorFacade
from .config import SERVICE_HOST, SERVICE_PATH, SOAP_ACTION_NS
from .service import SoapService
from .soap import RequestBuilder, ResponseParser
from .transport import HttpClient


def demo() -> None:
    print("=== Facade demo — SOAP Calculator ===\n")

    service = SoapService(
        transport=HttpClient(
            host=SERVICE_HOST,
            path=SERVICE_PATH,
            soap_action_ns=SOAP_ACTION_NS,
        ),
        request_builder=RequestBuilder(),
        response_parser=ResponseParser(),
    )
    calc = CalculatorFacade(service=service)

    pairs = [(5, 3), (10, 4), (3, 7), (20, 4)]
    operations = [
        ("add", calc.add),
        ("subtract", calc.subtract),
        ("multiply", calc.multiply),
        ("divide", calc.divide),
    ]

    for (name, fn), (a, b) in zip(operations, pairs):
        result = fn(a, b)
        print(f"  {name}({a}, {b}) = {result}")


if __name__ == "__main__":
    demo()
