from .guest import Guest
from .mediator import Mediator
from .mediator_element import MediatorElement
from .services import FlowerDelivery, MasterService, TaxiService


class ConciergeMediator(Mediator):
    def __init__(
        self,
        guest: Guest,
        taxi: TaxiService,
        master: MasterService,
        flowers: FlowerDelivery,
    ) -> None:
        self._guest = guest
        self._taxi = taxi
        self._master = master
        self._flowers = flowers

        for mediator_element in (guest, taxi, master, flowers):
            mediator_element.set_mediator(self)

    def notify(self, mediator_element: MediatorElement, event: str) -> None:
        match event:
            case "taxi":
                self._taxi.handle()
            case "master":
                self._master.handle()
            case "flowers":
                self._flowers.handle()
            case "taxi_done":
                self._guest.receive("Taxi is on its way")
            case "master_done":
                self._guest.receive("Master will arrive shortly")
            case "flowers_done":
                self._guest.receive("Flowers are on their way")
