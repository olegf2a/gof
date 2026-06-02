from ..context import Context
from ..expression import AbstractExpression


class AddExpression(AbstractExpression):
    """Terminal expression"""

    def __init__(self, topping: str) -> None:
        self._topping = topping

    def interpret(self, context: Context) -> None:
        context.add(self._topping)
