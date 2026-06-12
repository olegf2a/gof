from .memento import Memento
from .originator import Originator
from .text_snapshot import TextSnapshot


class TextEditor(Originator):
    def __init__(self) -> None:
        self._content = ""

    @property
    def content(self) -> str:
        return self._content

    def write(self, text: str) -> None:
        self._content = text

    def save(self) -> Memento:
        return TextSnapshot(self._content)

    def restore(self, memento: Memento) -> None:
        if not isinstance(memento, TextSnapshot):
            raise TypeError("Memento must be of type TextSnapshot")
        self._content = memento.get_state()
