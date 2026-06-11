from ..observer import Observer
from ..storm_alert_event import StormAlertEvent, WarningLevel


class RoadService(Observer):
    def update(self, alert: StormAlertEvent) -> None:
        match alert.level:
            case WarningLevel.LOW:
                print(f"[RoadService] Pre-treating roads — {alert.message}")
            case WarningLevel.MODERATE:
                print(f"[RoadService] Deploying snow plows — {alert.message}")
            case WarningLevel.HIGH:
                print(f"[RoadService] Closing highways — {alert.message}")
            case WarningLevel.EXTREME:
                print(f"[RoadService] Full emergency response — {alert.message}")
