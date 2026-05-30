from .unit import Unit


class Army:
    def __init__(self) -> None:
        self._units: list[Unit] = []

    def add(self, unit: Unit) -> None:
        self._units.append(unit)

    def move_all(self, dx: int, dy: int) -> None:
        for unit in self._units:
            unit.move(dx, dy)

    def render_all(self) -> None:
        for unit in self._units:
            unit.render()
