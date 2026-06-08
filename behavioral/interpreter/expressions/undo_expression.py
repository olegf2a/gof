from ..context import Context
from ..expression import AbstractExpression


class UndoExpression(AbstractExpression):
    """Terminal expression"""

    def interpret(self, context: Context) -> None:
        context.undo()
