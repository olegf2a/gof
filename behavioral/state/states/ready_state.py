from __future__ import annotations

from typing import TYPE_CHECKING

from ..oven_state import OvenState

if TYPE_CHECKING:
    from ..pizza_oven import PizzaOven


class ReadyState(OvenState):
    def heat_up(self, context: PizzaOven) -> None:
        from .overheated_state import OverheatedState

        context.change_state(OverheatedState())
        print("[Oven] Overheating — temperature exceeded safe limit.")

    def cool_down(self, context: PizzaOven) -> None:
        from .cold_state import ColdState

        context.change_state(ColdState())
        print("[Oven] Cooling down — oven is cold.")

    def bake(self, context: PizzaOven, pizza: str) -> None:
        print(f"[Oven] Baking '{pizza}' — perfect temperature!")

    def name(self) -> str:
        return "Ready"
