from .base import UnitFlyweight


class Tank(UnitFlyweight):
    @property
    def texture(self) -> str:
        return "tank.png"

    @property
    def sounds(self) -> list[str]:
        return ["engine.wav", "shot.wav"]
