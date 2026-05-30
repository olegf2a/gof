from .. import Command, Receiver


class ClearTopping(Command):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver: Receiver = receiver
        self._actions: list[str] = []

    def execute(self) -> None:
        self._actions = self._receiver.get_actions()
        self._receiver.clear_actions()

    def undo(self) -> None:
        for action in self._actions:
            self._receiver.action(action)
        self._actions.clear()
