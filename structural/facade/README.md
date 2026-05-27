# Facade Pattern

An implementation of the Facade design pattern that hides the complexity of a SOAP web service behind a simple Python interface.

## Problem and Solution

### The Problem
Calling a SOAP web service requires the client to know low-level details: XML envelope format, HTTP headers, namespace URIs, and XML parsing:

```python
# Without Facade — client must know all SOAP details:
ns = "http://www.dneonline.com/calculator.asmx"
envelope = f"""<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Add xmlns="{ns}">
      <intA>5</intA><intB>3</intB>
    </Add>
  </soap:Body>
</soap:Envelope>"""
headers = {"Content-Type": "text/xml", "SOAPAction": f'"{ns}/Add"'}
response = requests.post(url, data=envelope, headers=headers)
tree = ET.fromstring(response.text)
result = int(tree.find(f".//{{{ns}}}AddResult").text)
```

### The Solution
The Facade wraps three subsystems and exposes only four clean methods:

```python
# With Facade — client sees only this:
calc = CalculatorFacade()
calc.add(5, 3)        # → 8
calc.subtract(10, 4)  # → 6
calc.multiply(3, 7)   # → 21
calc.divide(20, 4)    # → 5
```

## Pattern Overview

- **Facade** (`CalculatorFacade`): single entry point — coordinates all subsystems
- **RequestBuilder**: builds SOAP XML envelopes for each operation
- **SoapClient**: sends HTTP POST requests and returns raw XML
- **ResponseParser**: extracts the integer result from XML

## Structure

```
structural/facade/
├── __init__.py
├── __main__.py              ← demo
├── calculator_facade.py     ← CalculatorFacade (public interface)
├── requirements.txt         ← requests>=2.28.0
├── soap/
│   ├── __init__.py
│   ├── client.py            ← SoapClient (HTTP POST)
│   ├── request_builder.py   ← builds SOAP XML envelope
│   └── response_parser.py   ← parses XML response → int
├── uml/
│   ├── facade_schema.puml   ← structural class diagram
│   └── facade_flow.puml     ← sequence / call flow diagram
└── tests/
    └── test_facade.py
```

## Usage

### As a module:
```python
from structural.facade import CalculatorFacade

calc = CalculatorFacade()
print(calc.add(5, 3))       # 8
print(calc.multiply(3, 7))  # 21
```

### Run the demo:
```bash
python -m structural.facade
```

### Run the tests:
```bash
python -m unittest structural.facade.tests.test_facade -v
```

## Key Components

### CalculatorFacade (`calculator_facade.py`)
Coordinates the three subsystems. Exposes `add()`, `subtract()`, `multiply()`, `divide()`.
All four delegate through a shared `_call(operation, a, b)` method.

### RequestBuilder (`soap/request_builder.py`)
Builds a SOAP 1.1 XML envelope string for a given operation and two integer arguments.

### SoapClient (`soap/client.py`)
Performs HTTP POST to `http://www.dneonline.com/calculator.asmx` with the correct
`Content-Type` and `SOAPAction` headers.

### ResponseParser (`soap/response_parser.py`)
Parses the XML response with `xml.etree.ElementTree` and extracts the integer `<OperationResult>` value.
Raises `ValueError` for malformed XML or missing result elements.

## Call Flow

```
Client → CalculatorFacade.add(5, 3)
           → RequestBuilder.build("Add", 5, 3)  → SOAP XML envelope
           → SoapClient.call(envelope, "Add")    → raw XML response
           → ResponseParser.parse("Add", xml)    → 8
           ← return 8
```

## Facade vs Adapter

Both patterns introduce an indirection layer, but they serve different goals:

| Aspect       | Facade                                     | Adapter                                      |
|--------------|--------------------------------------------|----------------------------------------------|
| **Purpose**  | Simplify a complex subsystem               | Convert one interface into another           |
| **Wraps**    | Multiple subsystem classes                 | One existing class                           |
| **Interface**| Defines a new, simpler interface           | Conforms to an existing expected interface   |
| **Problem**  | Client knows too many details              | Client expects an interface the class lacks  |
| **Example**  | `calc.add(5, 3)` hides SOAP machinery      | `weather.get_temperature()` wraps `pobierz_temperatura()` |

In short: **Adapter** makes incompatible code work together; **Facade** reduces complexity.

A Facade can also act as an Adapter if the simplified interface happens to match a required contract,
but the motivation is different — simplification vs. translation.

## Benefits

- **Reduced coupling**: client depends on one class, not on HTTP/XML libraries
- **Single entry point**: subsystems can be swapped without changing client code
- **Testable**: subsystems are independently testable; facade tested via mocks
