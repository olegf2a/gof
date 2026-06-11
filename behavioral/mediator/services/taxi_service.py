from ..mediator_element import MediatorElement


class TaxiService(MediatorElement):
    def handle(self) -> None:
        if self._mediator is None:
            raise RuntimeError("Mediator is not set")
        print("TaxiService:: taxi is ready")
        self._mediator.notify(self, "taxi_done")
