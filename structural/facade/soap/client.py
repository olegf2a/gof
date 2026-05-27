import http.client

SERVICE_HOST = "www.dneonline.com"
SERVICE_PATH = "/calculator.asmx"


class SoapClient:
    def call(self, envelope: str, operation: str) -> str:
        body = envelope.encode("utf-8")
        conn = http.client.HTTPConnection(SERVICE_HOST, 80, timeout=15)
        try:
            conn.request(
                "POST",
                SERVICE_PATH,
                body=body,
                headers={
                    "Host": SERVICE_HOST,
                    "User-Agent": "curl/8.7.1",
                    "Accept": "*/*",
                    "Content-Type": "text/xml; charset=utf-8",
                    "SOAPAction": f'"http://tempuri.org/{operation}"',
                    "Content-Length": str(len(body)),
                },
            )
            resp = conn.getresponse()
            text = resp.read().decode("utf-8")
            if resp.status != 200:
                raise RuntimeError(
                    f"SOAP call failed: {resp.status} {resp.reason}\n{text}"
                )
            return text
        finally:
            conn.close()
