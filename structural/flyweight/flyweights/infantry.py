from .base import UnitFlyweight


class Infantry(UnitFlyweight):
    @property
    def texture(self) -> str:
        return "infantry.png"

    @property
    def sounds(self) -> list[str]:
        return ["march.wav", "rifle.wav"]
