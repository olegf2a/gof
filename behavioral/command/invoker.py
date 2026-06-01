from abc import ABC, abstractmethod

from .command import Command


class Invoker(ABC):
    @abstractmethod
    def run(self, cmd: Command) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...
