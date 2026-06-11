from .storm_alert_event import StormAlertEvent, WarningLevel
from .storm_service import StormService
from .subscribers.airport import Airport
from .subscribers.road_service import RoadService
from .subscribers.school import School


def demo() -> None:
    print("=== Observer Pattern — Storm Warning Service ===\n")

    service = StormService()
    school = School()
    airport = Airport()
    road_service = RoadService()

    service.subscribe(school)
    service.subscribe(airport)
    service.subscribe(road_service)

    print("--- LOW alert ---")
    service.notify(
        StormAlertEvent(level=WarningLevel.LOW, message="Light storm expected.")
    )

    print("\n--- MODERATE alert ---")
    service.notify(
        StormAlertEvent(level=WarningLevel.MODERATE, message="Moderate storm incoming.")
    )

    print("\n--- HIGH alert ---")
    service.notify(
        StormAlertEvent(level=WarningLevel.HIGH, message="Severe storm approaching.")
    )

    print("\n--- EXTREME alert ---")
    service.notify(
        StormAlertEvent(level=WarningLevel.EXTREME, message="Hurricane warning issued.")
    )

    print("\n--- School unsubscribes, EXTREME alert ---")
    service.unsubscribe(school)
    service.notify(
        StormAlertEvent(level=WarningLevel.EXTREME, message="Hurricane warning issued.")
    )


if __name__ == "__main__":
    demo()
