from .. import Command, Receiver


class ItalianCustomToppings(Command):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver: Receiver = receiver

    def execute(self) -> None:
        self._receiver.action("Mozzarella")
        self._receiver.action("Olives")
        self._receiver.action("Tomatoes")

    def undo(self) -> None:
        self._receiver.reverse_action("Mozzarella")
        self._receiver.reverse_action("Olives")
        self._receiver.reverse_action("Tomatoes")
