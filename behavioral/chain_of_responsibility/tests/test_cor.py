"""Unit tests for Chain of Responsibility — Emergency Dispatcher"""

import unittest

from ..chain import Chain
from ..handler import Handler
from ..handlers import Fire, Medical, Police
from ..request import Request


def _make_chain() -> Chain:
    return Chain([Fire(), Police(), Medical()])


class TestRequest(unittest.TestCase):

    def test_fields(self) -> None:
        r = Request("fire", "Main St", "Building on fire")
        self.assertEqual(r.emergency_type, "fire")
        self.assertEqual(r.location, "Main St")
        self.assertEqual(r.description, "Building on fire")


class TestHandlerInterface(unittest.TestCase):

    def test_handler_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            Handler()  # type: ignore[abstract]

    def test_fire_implements_handler(self) -> None:
        self.assertIsInstance(Fire(), Handler)

    def test_police_implements_handler(self) -> None:
        self.assertIsInstance(Police(), Handler)

    def test_medical_implements_handler(self) -> None:
        self.assertIsInstance(Medical(), Handler)


class TestFireHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = Fire()

    def test_handles_fire(self) -> None:
        result = self.handler.handle(Request("fire", "Main St", "Blaze"))
        self.assertIsNotNone(result)
        self.assertIn("Main St", result)  # type: ignore[arg-type]

    def test_ignores_police(self) -> None:
        self.assertIsNone(self.handler.handle(Request("police", "Main St", "Robbery")))

    def test_ignores_medical(self) -> None:
        self.assertIsNone(self.handler.handle(Request("medical", "Main St", "Injury")))


class TestPoliceHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = Police()

    def test_handles_police(self) -> None:
        result = self.handler.handle(Request("police", "Broadway", "Robbery"))
        self.assertIsNotNone(result)
        self.assertIn("Broadway", result)  # type: ignore[arg-type]

    def test_ignores_fire(self) -> None:
        self.assertIsNone(self.handler.handle(Request("fire", "Broadway", "Blaze")))

    def test_ignores_medical(self) -> None:
        self.assertIsNone(self.handler.handle(Request("medical", "Broadway", "Injury")))


class TestMedicalHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = Medical()

    def test_handles_medical(self) -> None:
        result = self.handler.handle(Request("medical", "Park Ave", "Heart attack"))
        self.assertIsNotNone(result)
        self.assertIn("Park Ave", result)  # type: ignore[arg-type]

    def test_ignores_fire(self) -> None:
        self.assertIsNone(self.handler.handle(Request("fire", "Park Ave", "Blaze")))

    def test_ignores_police(self) -> None:
        self.assertIsNone(self.handler.handle(Request("police", "Park Ave", "Robbery")))


class TestChain(unittest.TestCase):

    def setUp(self) -> None:
        self.chain = _make_chain()

    def test_dispatches_fire(self) -> None:
        result = self.chain.call_service(Request("fire", "Main St", "Blaze"))
        self.assertIn("Main St", result)

    def test_dispatches_police(self) -> None:
        result = self.chain.call_service(Request("police", "Broadway", "Robbery"))
        self.assertIn("Broadway", result)

    def test_dispatches_medical(self) -> None:
        result = self.chain.call_service(Request("medical", "Park Ave", "Heart attack"))
        self.assertIn("Park Ave", result)

    def test_raises_on_unknown_type(self) -> None:
        with self.assertRaises(ValueError):
            self.chain.call_service(Request("unknown", "Somewhere", "Mystery"))

    def test_add_handler_extends_chain(self) -> None:
        chain = Chain([Fire()])
        with self.assertRaises(ValueError):
            chain.call_service(Request("police", "Broadway", "Robbery"))
        chain.add_handler(Police())
        result = chain.call_service(Request("police", "Broadway", "Robbery"))
        self.assertIn("Broadway", result)

    def test_first_matching_handler_wins(self) -> None:
        chain = Chain([Fire(), Fire()])
        result = chain.call_service(Request("fire", "Main St", "Blaze"))
        self.assertIsNotNone(result)

    def test_empty_chain_raises(self) -> None:
        chain = Chain([])
        with self.assertRaises(ValueError):
            chain.call_service(Request("fire", "Main St", "Blaze"))


if __name__ == "__main__":
    unittest.main()
