from .weather import Weather
from .weather_adapter_Pl import WeatherAdapterPl


def main() -> None:
    def _get_pl_adapter(city: str) -> Weather:
        return WeatherAdapterPl(city)

    def _show_weather(service: Weather) -> None:
        print(
            f"******* Weather in {service.get_city()} ********",
        )
        print(f"Temperature: {service.get_temperature()}")
        print(f"Humidity: {service.get_humidity()}")
        print("**" * 30)

    cities = ("wroclaw", "warsaw", "opole")

    for city in cities:
        _show_weather(_get_pl_adapter(city))


if __name__ == "__main__":
    main()
