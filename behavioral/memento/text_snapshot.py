from .memento import Memento


class TextSnapshot(Memento):
    def __init__(self, content: str) -> None:
        self._state = content
        super().__init__()

    def get_state(self) -> str:
        return self._state
