from abc import ABC, abstractmethod


class UnitFlyweight(ABC):
    @property
    @abstractmethod
    def texture(self) -> str: ...

    @property
    @abstractmethod
    def sounds(self) -> list[str]: ...

    def render(self, x: int, y: int) -> None:
        print(
            f"  [{self.__class__.__name__}] texture={self.texture} sounds={self.sounds} at ({x}, {y})"
        )
