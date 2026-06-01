from .. import Command, Receiver


class AddTopping(Command):
    def __init__(self, receiver: Receiver, context: str) -> None:
        self._receiver = receiver
        self._context = context

    def execute(self) -> None:
        self._receiver.action(self._context)

    def undo(self) -> None:
        self._receiver.reverse_action(self._context)
