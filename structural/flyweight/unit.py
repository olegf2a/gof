from .flyweights import UnitFlyweight


class Unit:
    def __init__(self, x: int, y: int, flyweight: UnitFlyweight):
        self._x = x
        self._y = y
        self._flyweight = flyweight

    def move(self, dx: int, dy: int) -> None:
        self._x += dx
        self._y += dy

    def render(self) -> None:
        self._flyweight.render(self._x, self._y)
