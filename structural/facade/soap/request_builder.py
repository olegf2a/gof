SOAP_NS = "http://tempuri.org/"
ENVELOPE_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <{operation} xmlns="{ns}">
      <intA>{a}</intA>
      <intB>{b}</intB>
    </{operation}>
  </soap:Body>
</soap:Envelope>"""


class RequestBuilder:
    def build(self, operation: str, a: int, b: int) -> str:
        return ENVELOPE_TEMPLATE.format(operation=operation, ns=SOAP_NS, a=a, b=b)
