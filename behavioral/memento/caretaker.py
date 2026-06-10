from .memento import Memento
from .originator import Originator


class VersionHistory:
    def __init__(self) -> None:
        self._history: list[Memento] = []

    def save(self, editor: Originator) -> None:
        self._history.append(editor.save())

    def restore(self, editor: Originator, version: int) -> None:
        try:
            editor.restore(self._history[version])
        except IndexError:
            raise RuntimeError(f"Version {version} does not exist")

    def history(self) -> list[Memento]:
        return list(self._history)
