from .calculator_facade import CalculatorFacade


def demo() -> None:

    print("=== Facade demo — SOAP Calculator ===\n")
    calc = CalculatorFacade()

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
