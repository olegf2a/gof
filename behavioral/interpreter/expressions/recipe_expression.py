from ..context import Context
from ..expression import AbstractExpression


class RecipeExpression(AbstractExpression):
    """Compound expression (Non-terminal)"""

    def __init__(self, expressions: list[AbstractExpression]) -> None:
        self._expressions = expressions

    def interpret(self, context: Context) -> None:
        for expression in self._expressions:
            expression.interpret(context)
