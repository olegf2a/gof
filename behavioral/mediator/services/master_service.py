from ..mediator_element import MediatorElement


class MasterService(MediatorElement):
    def handle(self) -> None:
        if self._mediator is None:
            raise RuntimeError("Mediator is not set")
        print("MasterService:: Master is dispatched")
        self._mediator.notify(self, "master_done")
