from .memento import Memento


class TextSnapshot(Memento):
    def __init__(self, content: str) -> None:
        self._content = content

    def get_content(self) -> str:
        return self._content
