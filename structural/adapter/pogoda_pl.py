"""Polish weather service — the adaptee with non-English interface"""


class PogodaPL:
    """Third-party Polish weather service with Polish method names"""

    def __init__(self, miasto: str) -> None:
        self._miasto = miasto
        self._dane = {
            "wroclaw": (22.3, 69),
            "warsaw": (21.5, 73),
            "opole": (21, 50),
        }

    def pobierz_temperatura(self) -> float:
        tmp, _ = self._dane.get(self._miasto, (22, 60))
        return tmp

    def pobierz_wilgotnosc(self) -> int:
        _, wol = self._dane.get(self._miasto, (22, 60))
        return wol

    def pobierz_miasto(self) -> str:
        return self._miasto
