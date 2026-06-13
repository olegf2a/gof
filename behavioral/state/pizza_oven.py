from .oven_state import OvenState
from .states.cold_state import ColdState


class PizzaOven:
    def __init__(self) -> None:
        self._state: OvenState = ColdState()

    @property
    def state_name(self) -> str:
        return self._state.name()

    def change_state(self, new_state: OvenState) -> None:
        self._state = new_state

    def heat_up(self) -> None:
        self._state.heat_up(self)

    def cool_down(self) -> None:
        self._state.cool_down(self)

    def bake(self, pizza: str) -> None:
        self._state.bake(self, pizza)
