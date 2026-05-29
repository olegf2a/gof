from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def action(self, context: str) -> None: ...

    @abstractmethod
    def reverse_action(self, context: str) -> None: ...

    @abstractmethod
    def describe(self) -> str: ...
