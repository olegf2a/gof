from .concierge_mediator import ConciergeMediator
from .guest import Guest
from .services import FlowerDelivery, MasterService, TaxiService


def demo() -> None:
    print("=== Mediator Pattern — Concierge Service ===\n")

    guest = Guest()
    mediator = ConciergeMediator(
        guest=guest,
        taxi=TaxiService(),
        master=MasterService(),
        flowers=FlowerDelivery(),
    )

    guest.request("taxi")
    guest.request("master")
    guest.request("flowers")


if __name__ == "__main__":
    demo()
