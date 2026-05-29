from http.client import HTTPConnection

from .transport import Transport


class HttpClient(Transport):
    def __init__(self, host: str, path: str, soap_action_ns: str) -> None:
        self._host = host
        self._path = path
        self._soap_action_ns = soap_action_ns
        self._conn: HTTPConnection | None = None

    def _init(self) -> None:
        if self._conn is None:
            self._conn = HTTPConnection(self._host, 80, timeout=15)

    def post(self, envelope: str, operation: str) -> str:
        self._init()
        body = envelope.encode("utf-8")
        try:
            self._conn.request(  # type: ignore[union-attr]
                "POST",
                self._path,
                body=body,
                headers={
                    "Host": self._host,
                    "User-Agent": "curl/8.7.1",
                    "Accept": "*/*",
                    "Content-Type": "text/xml; charset=utf-8",
                    "SOAPAction": f'"{self._soap_action_ns}/{operation}"',
                    "Content-Length": str(len(body)),
                },
            )
            resp = self._conn.getresponse()  # type: ignore[union-attr]
            text = resp.read().decode("utf-8")
            if resp.status != 200:
                raise RuntimeError(
                    f"SOAP call failed: {resp.status} {resp.reason}\n{text}"
                )
            return text
        finally:
            self._conn.close()  # type: ignore[union-attr]
            self._conn = None
