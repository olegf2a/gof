"""Adapter Pattern - Weather service

This module implements the Adapter pattern for fetching weather data.
"""

from .pogoda_pl import PogodaPL
from .weather import Weather
from .weather_adapter_Pl import WeatherAdapterPl

__all__ = ["PogodaPL", "Weather", "WeatherAdapterPl"]
