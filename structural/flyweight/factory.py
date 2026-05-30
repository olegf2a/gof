from threading import Lock

from .flyweights import Infantry, Tank, UnitFlyweight

_REGISTRY: dict[str, type[UnitFlyweight]] = {
    "tank": Tank,
    "infantry": Infantry,
}


class FlyweightFactory:
    def __init__(self) -> None:
        self._cache: dict[str, UnitFlyweight] = {}
        self._lock: Lock = Lock()

    def get(self, unit_type: str) -> UnitFlyweight:
        with self._lock:
            if unit_type not in _REGISTRY:
                raise KeyError(f"{unit_type} is not a valid unit type")
            if unit_type not in self._cache:
                self._cache[unit_type] = _REGISTRY[unit_type]()
            return self._cache[unit_type]
