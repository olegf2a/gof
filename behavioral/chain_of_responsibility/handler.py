from abc import ABC, abstractmethod

from .request import Request


class Handler(ABC):
    @abstractmethod
    def handle(self, request: Request) -> str | None: ...
