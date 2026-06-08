from ..command.commands.add_topping import AddTopping
from ..command.invoker import Invoker
from ..command.receiver import Receiver


class Context:
    def __init__(self, invoker: Invoker, receiver: Receiver) -> None:
        self._invoker = invoker
        self._receiver = receiver

    def add(self, topping: str) -> None:
        self._invoker.run(AddTopping(self._receiver, topping))

    def undo(self) -> None:
        self._invoker.undo()

    def describe(self) -> str:
        return self._receiver.describe()
