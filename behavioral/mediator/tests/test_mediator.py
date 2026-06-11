import unittest
from unittest.mock import MagicMock, call, patch

from ..concierge_mediator import ConciergeMediator
from ..guest import Guest
from ..services import FlowerDelivery, MasterService, TaxiService


def _make_mediator() -> (
    tuple[ConciergeMediator, Guest, TaxiService, MasterService, FlowerDelivery]
):
    guest = Guest()
    taxi = TaxiService()
    master = MasterService()
    flowers = FlowerDelivery()
    mediator = ConciergeMediator(guest=guest, taxi=taxi, master=master, flowers=flowers)
    return mediator, guest, taxi, master, flowers


class TestConciergeMediator(unittest.TestCase):
    def test_mediator_set_on_all_elements(self) -> None:
        mediator, guest, taxi, master, flowers = _make_mediator()
        for element in (guest, taxi, master, flowers):
            self.assertIs(element._mediator, mediator)

    def test_taxi_request_calls_taxi_handle(self) -> None:
        mediator, guest, taxi, *_ = _make_mediator()
        with patch.object(taxi, "handle") as mock_handle:
            mediator.notify(guest, "taxi")
        mock_handle.assert_called_once()

    def test_master_request_calls_master_handle(self) -> None:
        mediator, guest, _, master, _ = _make_mediator()
        with patch.object(master, "handle") as mock_handle:
            mediator.notify(guest, "master")
        mock_handle.assert_called_once()

    def test_flowers_request_calls_flowers_handle(self) -> None:
        mediator, guest, _, _, flowers = _make_mediator()
        with patch.object(flowers, "handle") as mock_handle:
            mediator.notify(guest, "flowers")
        mock_handle.assert_called_once()

    def test_taxi_done_notifies_guest(self) -> None:
        mediator, guest, taxi, *_ = _make_mediator()
        with patch.object(guest, "receive") as mock_receive:
            mediator.notify(taxi, "taxi_done")
        mock_receive.assert_called_once_with("Taxi is on its way")

    def test_master_done_notifies_guest(self) -> None:
        mediator, guest, _, master, _ = _make_mediator()
        with patch.object(guest, "receive") as mock_receive:
            mediator.notify(master, "master_done")
        mock_receive.assert_called_once_with("Master will arrive shortly")

    def test_flowers_done_notifies_guest(self) -> None:
        mediator, guest, _, _, flowers = _make_mediator()
        with patch.object(guest, "receive") as mock_receive:
            mediator.notify(flowers, "flowers_done")
        mock_receive.assert_called_once_with("Flowers are on their way")

    def test_unknown_event_does_nothing(self) -> None:
        mediator, guest, *_ = _make_mediator()
        mediator.notify(guest, "unknown_event")


class TestGuest(unittest.TestCase):
    def test_request_calls_mediator_notify(self) -> None:
        guest = Guest()
        mock_mediator = MagicMock()
        guest.set_mediator(mock_mediator)
        guest.request("taxi")
        mock_mediator.notify.assert_called_once_with(guest, "taxi")

    def test_request_without_mediator_raises(self) -> None:
        guest = Guest()
        with self.assertRaises(RuntimeError):
            guest.request("taxi")

    def test_receive_prints_message(self) -> None:
        guest = Guest()
        with patch("builtins.print") as mock_print:
            guest.receive("Taxi is on its way")
        mock_print.assert_called_once()
        self.assertIn("Taxi is on its way", mock_print.call_args.args[0])


class TestServices(unittest.TestCase):
    def test_taxi_handle_notifies_mediator(self) -> None:
        taxi = TaxiService()
        mock_mediator = MagicMock()
        taxi.set_mediator(mock_mediator)
        taxi.handle()
        mock_mediator.notify.assert_called_once_with(taxi, "taxi_done")

    def test_master_handle_notifies_mediator(self) -> None:
        master = MasterService()
        mock_mediator = MagicMock()
        master.set_mediator(mock_mediator)
        master.handle()
        mock_mediator.notify.assert_called_once_with(master, "master_done")

    def test_flowers_handle_notifies_mediator(self) -> None:
        flowers = FlowerDelivery()
        mock_mediator = MagicMock()
        flowers.set_mediator(mock_mediator)
        flowers.handle()
        mock_mediator.notify.assert_called_once_with(flowers, "flowers_done")


class TestEndToEnd(unittest.TestCase):
    def test_full_taxi_flow(self) -> None:
        mediator, guest, *_ = _make_mediator()
        with patch.object(guest, "receive") as mock_receive:
            guest.request("taxi")
        mock_receive.assert_called_once_with("Taxi is on its way")

    def test_full_master_flow(self) -> None:
        mediator, guest, *_ = _make_mediator()
        with patch.object(guest, "receive") as mock_receive:
            guest.request("master")
        mock_receive.assert_called_once_with("Master will arrive shortly")

    def test_full_flowers_flow(self) -> None:
        mediator, guest, *_ = _make_mediator()
        with patch.object(guest, "receive") as mock_receive:
            guest.request("flowers")
        mock_receive.assert_called_once_with("Flowers are on their way")

    def test_services_do_not_know_each_other(self) -> None:
        _, guest, taxi, master, flowers = _make_mediator()
        self.assertFalse(hasattr(taxi, "_guest"))
        self.assertFalse(hasattr(taxi, "_master"))
        self.assertFalse(hasattr(master, "_taxi"))
        self.assertFalse(hasattr(flowers, "_guest"))


if __name__ == "__main__":
    unittest.main()
