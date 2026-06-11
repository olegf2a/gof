from ..observer import Observer
from ..storm_alert_event import StormAlertEvent, WarningLevel


class School(Observer):
    def update(self, alert: StormAlertEvent) -> None:
        match alert.level:
            case WarningLevel.HIGH:
                print(f"[School] Cancelling classes — {alert.message}")
            case WarningLevel.EXTREME:
                print(f"[School] Emergency closure — {alert.message}")
