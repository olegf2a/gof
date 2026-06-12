import unittest

from ..pizza_oven import PizzaOven


class TestColdState(unittest.TestCase):
    def setUp(self) -> None:
        self.oven = PizzaOven()

    def test_initial_state_is_cold(self) -> None:
        self.assertEqual(self.oven.state_name, "Cold")

    def test_heat_up_transitions_to_ready(self) -> None:
        self.oven.heat_up()
        self.assertEqual(self.oven.state_name, "Ready")

    def test_bake_raises_when_cold(self) -> None:
        with self.assertRaises(RuntimeError):
            self.oven.bake("Margherita")

    def test_cool_down_raises_when_cold(self) -> None:
        with self.assertRaises(RuntimeError):
            self.oven.cool_down()


class TestReadyState(unittest.TestCase):
    def setUp(self) -> None:
        self.oven = PizzaOven()
        self.oven.heat_up()

    def test_state_is_ready(self) -> None:
        self.assertEqual(self.oven.state_name, "Ready")

    def test_bake_does_not_raise(self) -> None:
        self.oven.bake("Margherita")

    def test_heat_up_transitions_to_overheated(self) -> None:
        self.oven.heat_up()
        self.assertEqual(self.oven.state_name, "Overheated")

    def test_cool_down_transitions_to_cold(self) -> None:
        self.oven.cool_down()
        self.assertEqual(self.oven.state_name, "Cold")


class TestOverheatedState(unittest.TestCase):
    def setUp(self) -> None:
        self.oven = PizzaOven()
        self.oven.heat_up()
        self.oven.heat_up()

    def test_state_is_overheated(self) -> None:
        self.assertEqual(self.oven.state_name, "Overheated")

    def test_bake_raises_when_overheated(self) -> None:
        with self.assertRaises(RuntimeError):
            self.oven.bake("Margherita")

    def test_heat_up_raises_when_overheated(self) -> None:
        with self.assertRaises(RuntimeError):
            self.oven.heat_up()

    def test_cool_down_transitions_to_ready(self) -> None:
        self.oven.cool_down()
        self.assertEqual(self.oven.state_name, "Ready")


class TestOvenCycles(unittest.TestCase):
    def setUp(self) -> None:
        self.oven = PizzaOven()

    def test_full_bake_cycle(self) -> None:
        self.oven.heat_up()
        self.oven.bake("Margherita")
        self.oven.cool_down()
        self.assertEqual(self.oven.state_name, "Cold")

    def test_overheat_and_recover(self) -> None:
        self.oven.heat_up()
        self.oven.heat_up()
        self.assertEqual(self.oven.state_name, "Overheated")
        self.oven.cool_down()
        self.assertEqual(self.oven.state_name, "Ready")
        self.oven.bake("Pepperoni")

    def test_cold_to_ready_to_cold(self) -> None:
        self.oven.heat_up()
        self.oven.cool_down()
        self.assertEqual(self.oven.state_name, "Cold")

    def test_error_messages_are_descriptive(self) -> None:
        with self.assertRaises(RuntimeError) as cm:
            self.oven.bake("Margherita")
        self.assertIn("cold", str(cm.exception).lower())

        self.oven.heat_up()
        self.oven.heat_up()
        with self.assertRaises(RuntimeError) as cm:
            self.oven.bake("Margherita")
        self.assertIn("overheated", str(cm.exception).lower())


if __name__ == "__main__":
    unittest.main()
