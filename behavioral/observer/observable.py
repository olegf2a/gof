from abc import ABC, abstractmethod

from .observer import Observer
from .storm_alert_event import StormAlertEvent


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer) -> None: ...

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None: ...

    @abstractmethod
    def notify(self, alert: StormAlertEvent) -> None: ...
