from .mediator_element import MediatorElement


class Guest(MediatorElement):
    def request(self, service: str) -> None:
        if self._mediator is None:
            raise RuntimeError("Mediator is not set")
        self._mediator.notify(self, service)

    def receive(self, message: str) -> None:
        print(f"Guest :: Received message: {message}")
