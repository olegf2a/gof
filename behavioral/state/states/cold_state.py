from __future__ import annotations

from typing import TYPE_CHECKING

from ..oven_state import OvenState

if TYPE_CHECKING:
    from ..pizza_oven import PizzaOven


class ColdState(OvenState):
    def heat_up(self, context: PizzaOven) -> None:
        from .ready_state import ReadyState

        context.change_state(ReadyState())
        print("[Oven] Heating up — oven is ready to bake.")

    def cool_down(self, context: PizzaOven) -> None:
        raise RuntimeError("Oven is already cold.")

    def bake(self, context: PizzaOven, pizza: str) -> None:
        raise RuntimeError("Cannot bake — oven is cold. Heat it up first.")

    def name(self) -> str:
        return "Cold"
