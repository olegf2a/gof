import xml.etree.ElementTree as ET

_RESULT_SUFFIX = "Result"
_NS = "http://tempuri.org/"


class ResponseParser:
    def parse(self, operation: str, xml: str) -> int:
        try:
            root = ET.fromstring(xml)
        except ET.ParseError as exc:
            raise ValueError(f"Invalid XML response: {exc}") from exc
        tag = f"{{{_NS}}}{operation}{_RESULT_SUFFIX}"
        element = root.find(f".//{tag}")
        if element is None or element.text is None:
            raise ValueError(f"Result element not found for operation '{operation}'")
        return int(element.text)
