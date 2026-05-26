"""Unit tests for Adapter pattern — Weather service"""

import unittest

from ..pogoda_pl import PogodaPL
from ..weather import Weather
from ..weather_adapter_Pl import WeatherAdapterPl


class TestPogodaPL(unittest.TestCase):
    """Tests for the adaptee (Polish weather service)"""

    def setUp(self) -> None:
        self.service = PogodaPL("wroclaw")

    def test_returns_temperature_for_known_city(self) -> None:
        self.assertEqual(self.service.pobierz_temperatura(), 22.3)

    def test_returns_humidity_for_known_city(self) -> None:
        self.assertEqual(self.service.pobierz_wilgotnosc(), 69)

    def test_returns_city_name(self) -> None:
        self.assertEqual(self.service.pobierz_miasto(), "wroclaw")

    def test_returns_defaults_for_unknown_city(self) -> None:
        unknown = PogodaPL("berlin")
        self.assertEqual(unknown.pobierz_temperatura(), 22)
        self.assertEqual(unknown.pobierz_wilgotnosc(), 60)


class TestWeatherAdapterPl(unittest.TestCase):
    """Tests for the adapter"""

    def setUp(self) -> None:
        self.adapter = WeatherAdapterPl("warsaw")

    def test_implements_weather_interface(self) -> None:
        self.assertIsInstance(self.adapter, Weather)

    def test_get_temperature_delegates_to_adaptee(self) -> None:
        self.assertEqual(self.adapter.get_temperature(), 21.5)

    def test_get_humidity_delegates_to_adaptee(self) -> None:
        self.assertEqual(self.adapter.get_humidity(), 73)

    def test_get_city_delegates_to_adaptee(self) -> None:
        self.assertEqual(self.adapter.get_city(), "warsaw")

    def test_all_known_cities(self) -> None:
        expected = {
            "wroclaw": (22.3, 69),
            "warsaw": (21.5, 73),
            "opole": (21, 50),
        }
        for city, (temp, humidity) in expected.items():
            adapter = WeatherAdapterPl(city)
            self.assertEqual(adapter.get_temperature(), temp)
            self.assertEqual(adapter.get_humidity(), humidity)

    def test_unknown_city_uses_defaults(self) -> None:
        adapter = WeatherAdapterPl("london")
        self.assertEqual(adapter.get_temperature(), 22)
        self.assertEqual(adapter.get_humidity(), 60)


if __name__ == "__main__":
    unittest.main()
