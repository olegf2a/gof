from ..observer import Observer
from ..storm_alert_event import StormAlertEvent, WarningLevel


class Airport(Observer):
    def update(self, alert: StormAlertEvent) -> None:
        match alert.level:
            case WarningLevel.MODERATE:
                print(f"[Airport] Restricting departures — {alert.message}")
            case WarningLevel.HIGH:
                print(f"[Airport] Suspending all flights — {alert.message}")
            case WarningLevel.EXTREME:
                print(f"[Airport] Closing airport — {alert.message}")
