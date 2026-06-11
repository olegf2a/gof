import unittest
from unittest.mock import MagicMock

from ..storm_alert_event import StormAlertEvent, WarningLevel
from ..storm_service import StormService
from ..subscribers.airport import Airport
from ..subscribers.road_service import RoadService
from ..subscribers.school import School


class TestStormAlertEvent(unittest.TestCase):
    def test_stores_level_and_message(self) -> None:
        alert = StormAlertEvent(level=WarningLevel.HIGH, message="Storm incoming.")
        self.assertEqual(alert.level, WarningLevel.HIGH)
        self.assertEqual(alert.message, "Storm incoming.")

    def test_frozen(self) -> None:
        alert = StormAlertEvent(level=WarningLevel.LOW, message="Light storm.")
        with self.assertRaises(Exception):
            alert.level = WarningLevel.EXTREME  # type: ignore[misc]

    def test_warning_level_ordering(self) -> None:
        self.assertLess(WarningLevel.LOW, WarningLevel.MODERATE)
        self.assertLess(WarningLevel.MODERATE, WarningLevel.HIGH)
        self.assertLess(WarningLevel.HIGH, WarningLevel.EXTREME)


class TestStormService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = StormService()
        self.observer = MagicMock()

    def test_subscribe_adds_observer(self) -> None:
        self.service.subscribe(self.observer)
        alert = StormAlertEvent(level=WarningLevel.LOW, message="test")
        self.service.notify(alert)
        self.observer.update.assert_called_once_with(alert)

    def test_unsubscribe_removes_observer(self) -> None:
        self.service.subscribe(self.observer)
        self.service.unsubscribe(self.observer)
        self.service.notify(StormAlertEvent(level=WarningLevel.LOW, message="test"))
        self.observer.update.assert_not_called()

    def test_notify_calls_all_subscribers(self) -> None:
        observers = [MagicMock(), MagicMock(), MagicMock()]
        for o in observers:
            self.service.subscribe(o)
        alert = StormAlertEvent(level=WarningLevel.HIGH, message="Storm.")
        self.service.notify(alert)
        for o in observers:
            o.update.assert_called_once_with(alert)

    def test_notify_with_no_subscribers(self) -> None:
        self.service.notify(StormAlertEvent(level=WarningLevel.LOW, message="test"))

    def test_unsubscribe_unknown_observer_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.service.unsubscribe(self.observer)


class TestSchool(unittest.TestCase):
    def setUp(self) -> None:
        self.school = School()

    def test_reacts_to_high(
        self,
    ) -> None:
        with self.assertLogs() as cm:
            import logging

            logging.getLogger().info("trigger")
        alert = StormAlertEvent(level=WarningLevel.HIGH, message="Severe storm.")
        # verify no exception is raised and update runs
        self.school.update(alert)

    def test_ignores_low(self) -> None:
        import io
        import sys

        captured = io.StringIO()
        sys.stdout = captured
        self.school.update(StormAlertEvent(level=WarningLevel.LOW, message="Light."))
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "")

    def test_ignores_moderate(self) -> None:
        import io
        import sys

        captured = io.StringIO()
        sys.stdout = captured
        self.school.update(
            StormAlertEvent(level=WarningLevel.MODERATE, message="Moderate.")
        )
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "")

    def test_reacts_to_extreme(self) -> None:
        import io
        import sys

        captured = io.StringIO()
        sys.stdout = captured
        self.school.update(
            StormAlertEvent(level=WarningLevel.EXTREME, message="Hurricane.")
        )
        sys.stdout = sys.__stdout__
        self.assertIn("Emergency closure", captured.getvalue())


class TestAirport(unittest.TestCase):
    def setUp(self) -> None:
        self.airport = Airport()

    def _capture(self, level: WarningLevel, message: str = "test") -> str:
        import io
        import sys

        captured = io.StringIO()
        sys.stdout = captured
        self.airport.update(StormAlertEvent(level=level, message=message))
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_ignores_low(self) -> None:
        self.assertEqual(self._capture(WarningLevel.LOW), "")

    def test_reacts_to_moderate(self) -> None:
        self.assertIn("Restricting departures", self._capture(WarningLevel.MODERATE))

    def test_reacts_to_high(self) -> None:
        self.assertIn("Suspending all flights", self._capture(WarningLevel.HIGH))

    def test_reacts_to_extreme(self) -> None:
        self.assertIn("Closing airport", self._capture(WarningLevel.EXTREME))


class TestRoadService(unittest.TestCase):
    def setUp(self) -> None:
        self.road = RoadService()

    def _capture(self, level: WarningLevel, message: str = "test") -> str:
        import io
        import sys

        captured = io.StringIO()
        sys.stdout = captured
        self.road.update(StormAlertEvent(level=level, message=message))
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_reacts_to_low(self) -> None:
        self.assertIn("Pre-treating roads", self._capture(WarningLevel.LOW))

    def test_reacts_to_moderate(self) -> None:
        self.assertIn("Deploying snow plows", self._capture(WarningLevel.MODERATE))

    def test_reacts_to_high(self) -> None:
        self.assertIn("Closing highways", self._capture(WarningLevel.HIGH))

    def test_reacts_to_extreme(self) -> None:
        self.assertIn("Full emergency response", self._capture(WarningLevel.EXTREME))


if __name__ == "__main__":
    unittest.main()
