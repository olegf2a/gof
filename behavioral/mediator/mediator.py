from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .mediator_element import MediatorElement


class Mediator(ABC):
    @abstractmethod
    def notify(self, mediator_element: "MediatorElement", event: str) -> None: ...
