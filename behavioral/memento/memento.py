from abc import ABC, abstractmethod
from datetime import datetime


class Memento(ABC):
    def __init__(self) -> None:
        self._version: str = datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")

    @abstractmethod
    def get_state(self) -> str: ...

    def get_version(self) -> str:
        return self._version
