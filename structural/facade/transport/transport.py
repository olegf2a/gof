from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def post(self, envelope: str, operation: str) -> str: ...
