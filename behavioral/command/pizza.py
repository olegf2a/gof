from .receiver import Receiver


class Pizza(Receiver):
    def __init__(self) -> None:
        self._toppings: list[str] = []

    def action(self, context: str) -> None:
        self._toppings.append(context)

    def reverse_action(self, context: str) -> None:
        self._toppings.remove(context)

    def get_toppings(self) -> list[str]:
        return list(self._toppings)

    def describe(self) -> str:
        if not self._toppings:
            return "Base Pizza (no toppings)"
        return "Base Pizza, " + ", ".join(self._toppings)
