from . import Command, Invoker, Receiver
from .commands import AddTopping


class Order(Invoker):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver: Receiver = receiver
        self._history: list[Command] = []

    def run(self, action: str) -> None:
        cmd = AddTopping(self._receiver, action)
        cmd.execute()
        self._history.append(cmd)

    def undo(self) -> None:
        if self._history:
            cmd = self._history.pop()
            cmd.undo()

    def describe(self) -> str:
        return self._receiver.describe()
