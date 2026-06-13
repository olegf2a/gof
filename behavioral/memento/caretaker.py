from .exceptions import VersionNotFoundException
from .memento import Memento
from .originator import Originator


class VersionHistory:
    def __init__(self) -> None:
        self._history: dict[str, Memento] = {}

    def save(self, editor: Originator) -> None:
        memento: Memento = editor.save()
        self._history[memento.get_version()] = memento

    def restore(self, editor: Originator, version: str) -> None:
        try:
            editor.restore(self._history[version])
        except KeyError:
            raise VersionNotFoundException(version)

    def history(self) -> list[Memento]:
        return list(self._history.values())
