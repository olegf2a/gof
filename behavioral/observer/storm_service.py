from .observable import Observable
from .observer import Observer
from .storm_alert_event import StormAlertEvent


class StormService(Observable):
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, alert: StormAlertEvent) -> None:
        for observer in self._observers:
            observer.update(alert)
