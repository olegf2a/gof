from abc import ABC, abstractmethod

from .storm_alert_event import StormAlertEvent


class Observer(ABC):
    @abstractmethod
    def update(self, alert: StormAlertEvent) -> None: ...
