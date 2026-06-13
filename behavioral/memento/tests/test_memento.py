import unittest

from ..caretaker import VersionHistory
from ..exceptions import MementoException, VersionNotFoundException
from ..memento import Memento
from ..text_editor import TextEditor
from ..text_snapshot import TextSnapshot


class TestTextSnapshot(unittest.TestCase):
    def test_stores_state(self) -> None:
        snap = TextSnapshot("hello")
        self.assertEqual(snap.get_state(), "hello")

    def test_empty_state(self) -> None:
        snap = TextSnapshot("")
        self.assertEqual(snap.get_state(), "")

    def test_has_version_key(self) -> None:
        snap = TextSnapshot("hello")
        self.assertIsInstance(snap.get_version(), str)
        self.assertTrue(len(snap.get_version()) > 0)

    def test_unique_version_keys(self) -> None:
        a = TextSnapshot("foo")
        b = TextSnapshot("bar")
        self.assertNotEqual(a.get_version(), b.get_version())

    def test_independent_instances(self) -> None:
        a = TextSnapshot("foo")
        b = TextSnapshot("bar")
        self.assertNotEqual(a.get_state(), b.get_state())


class TestTextEditor(unittest.TestCase):
    def setUp(self) -> None:
        self.editor = TextEditor()

    def test_initial_content_is_empty(self) -> None:
        self.assertEqual(self.editor.content, "")

    def test_write_sets_content(self) -> None:
        self.editor.write("hello")
        self.assertEqual(self.editor.content, "hello")

    def test_write_replaces_content(self) -> None:
        self.editor.write("first")
        self.editor.write("second")
        self.assertEqual(self.editor.content, "second")

    def test_save_returns_snapshot_of_current_content(self) -> None:
        self.editor.write("draft")
        snap = self.editor.save()
        self.assertEqual(snap.get_state(), "draft")

    def test_save_is_independent_copy(self) -> None:
        self.editor.write("original")
        snap = self.editor.save()
        self.editor.write("changed")
        self.assertEqual(snap.get_state(), "original")

    def test_restore_sets_content_from_snapshot(self) -> None:
        self.editor.write("saved state")
        snap = self.editor.save()
        self.editor.write("new state")
        self.editor.restore(snap)
        self.assertEqual(self.editor.content, "saved state")

    def test_restore_wrong_type_raises_type_error(self) -> None:
        class FakeMemento(Memento):
            def get_state(self) -> str:
                return "fake"

        with self.assertRaises(TypeError):
            self.editor.restore(FakeMemento())


class TestVersionHistory(unittest.TestCase):
    def setUp(self) -> None:
        self.editor = TextEditor()
        self.history = VersionHistory()

    def _save(self, text: str) -> str:
        self.editor.write(text)
        self.history.save(self.editor)
        return self.history.history()[-1].get_version()

    def test_history_starts_empty(self) -> None:
        self.assertEqual(self.history.history(), [])

    def test_save_appends_snapshot(self) -> None:
        self._save("v1")
        self.assertEqual(len(self.history.history()), 1)

    def test_save_multiple_versions(self) -> None:
        for text in ("v1", "v2", "v3"):
            self._save(text)
        self.assertEqual(len(self.history.history()), 3)

    def test_restore_by_version_key(self) -> None:
        key1 = self._save("first")
        key2 = self._save("second")

        self.history.restore(self.editor, key1)
        self.assertEqual(self.editor.content, "first")

        self.history.restore(self.editor, key2)
        self.assertEqual(self.editor.content, "second")

    def test_restore_invalid_version_raises_version_not_found(self) -> None:
        self._save("v1")
        with self.assertRaises(VersionNotFoundException):
            self.history.restore(self.editor, "2000-01-01 00:00:00.000000")

    def test_version_not_found_is_memento_exception(self) -> None:
        self._save("v1")
        with self.assertRaises(MementoException):
            self.history.restore(self.editor, "2000-01-01 00:00:00.000000")

    def test_version_not_found_message_contains_version(self) -> None:
        self._save("v1")
        bad_version = "2000-01-01 00:00:00.000000"
        with self.assertRaises(VersionNotFoundException) as cm:
            self.history.restore(self.editor, bad_version)
        self.assertIn(bad_version, str(cm.exception))

    def test_history_returns_copy(self) -> None:
        self._save("v1")
        snapshot = self.history.history()
        snapshot.clear()
        self.assertEqual(len(self.history.history()), 1)

    def test_snapshot_in_history_is_independent_of_editor(self) -> None:
        key = self._save("saved")
        self.editor.write("changed")
        snap = next(s for s in self.history.history() if s.get_version() == key)
        self.assertEqual(snap.get_state(), "saved")

    def test_version_keys_are_unique(self) -> None:
        for text in ("v1", "v2", "v3"):
            self._save(text)
        keys = [s.get_version() for s in self.history.history()]
        self.assertEqual(len(keys), len(set(keys)))


class TestExceptions(unittest.TestCase):
    def test_version_not_found_is_subclass_of_memento_exception(self) -> None:
        self.assertTrue(issubclass(VersionNotFoundException, MementoException))

    def test_memento_exception_is_subclass_of_exception(self) -> None:
        self.assertTrue(issubclass(MementoException, Exception))

    def test_version_not_found_message(self) -> None:
        exc = VersionNotFoundException("2000-01-01")
        self.assertIn("2000-01-01", str(exc))


if __name__ == "__main__":
    unittest.main()
