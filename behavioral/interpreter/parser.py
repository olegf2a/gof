from .expression import AbstractExpression
from .expressions import AddExpression, RecipeExpression, UndoExpression


def parse(text: str) -> RecipeExpression:
    expressions: list[AbstractExpression] = []
    for token in (t.strip() for t in text.split(",")):
        if token.startswith("add:"):
            expressions.append(AddExpression(token[4:]))
        elif token == "undo":
            expressions.append(UndoExpression())
        else:
            raise ValueError(f"Unknown instruction: '{token}'")
    return RecipeExpression(expressions)
