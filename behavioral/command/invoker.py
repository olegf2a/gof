from abc import ABC, abstractmethod


class Invoker(ABC):
    @abstractmethod
    def run(self, action: str) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...
