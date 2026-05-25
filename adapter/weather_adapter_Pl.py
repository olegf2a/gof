"""Adapter for Polish weather service"""

from .pogoda_pl import PogodaPL
from .weather import Weather


class WeatherAdapterPl(Weather):
    """Adapter for Polish weather service"""

    def __init__(self, city: str) -> None:
        self._service = PogodaPL(city)

    def get_temperature(self) -> float:
        return self._service.pobierz_temperatura()

    def get_humidity(self) -> int:
        return self._service.pobierz_wilgotnosc()

    def get_city(self) -> str:
        return self._service.pobierz_miasto()
