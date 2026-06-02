from abc import ABC, abstractmethod

from .context import Context


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context: "Context") -> None: ...
