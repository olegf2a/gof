from ..mediator_element import MediatorElement


class FlowerDelivery(MediatorElement):
    def handle(self) -> None:
        if self._mediator is None:
            raise RuntimeError("Mediator is not set")
        print("FlowerDelivery:: Flowers are prepared")
        self._mediator.notify(self, "flowers_done")
