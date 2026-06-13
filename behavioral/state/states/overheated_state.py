from __future__ import annotations

from typing import TYPE_CHECKING

from ..oven_state import OvenState

if TYPE_CHECKING:
    from ..pizza_oven import PizzaOven


class OverheatedState(OvenState):
    def heat_up(self, context: PizzaOven) -> None:
        raise RuntimeError("Cannot heat up — oven is already overheated.")

    def cool_down(self, context: PizzaOven) -> None:
        from .ready_state import ReadyState

        context.change_state(ReadyState())
        print("[Oven] Cooling down — oven is ready to bake.")

    def bake(self, context: PizzaOven, pizza: str) -> None:
        raise RuntimeError("Cannot bake — oven is overheated. Cool it down first.")

    def name(self) -> str:
        return "Overheated"
