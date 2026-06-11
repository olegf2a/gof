from abc import ABC

from .mediator import Mediator


class MediatorElement(ABC):
    def __init__(self) -> None:
        self._mediator: "Mediator | None" = None

    def set_mediator(self, mediator: "Mediator") -> None:
        self._mediator = mediator
