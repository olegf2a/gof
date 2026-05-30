from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def action(self, context: str) -> None: ...

    @abstractmethod
    def reverse_action(self, context: str) -> None: ...

    @abstractmethod
    def clear_actions(self) -> None: ...

    @abstractmethod
    def get_actions(self) -> list[str]: ...

    @abstractmethod
    def describe(self) -> str: ...
