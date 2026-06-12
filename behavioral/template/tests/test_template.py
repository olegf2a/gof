import os
import tempfile
import unittest

from ..writers.date_file_writer import DateFileWriter
from ..writers.time_file_writer import TimeFileWriter


class TestDateFileWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "date.txt")
        DateFileWriter().write(self.path)
        with open(self.path) as f:
            self.content = f.read()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_file_is_created(self) -> None:
        self.assertTrue(os.path.exists(self.path))

    def test_header_present(self) -> None:
        self.assertIn("Date Report", self.content)

    def test_date_format(self) -> None:
        self.assertRegex(self.content, r"\d{4}-\d{2}-\d{2}")

    def test_footer_present(self) -> None:
        self.assertIn("=" * 30, self.content)

    def test_no_time_in_date_report(self) -> None:
        self.assertNotRegex(self.content, r"\d{2}:\d{2}:\d{2}")


class TestTimeFileWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "time.txt")
        TimeFileWriter().write(self.path)
        with open(self.path) as f:
            self.content = f.read()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_file_is_created(self) -> None:
        self.assertTrue(os.path.exists(self.path))

    def test_header_present(self) -> None:
        self.assertIn("Time Report", self.content)

    def test_time_format(self) -> None:
        self.assertRegex(self.content, r"\d{2}:\d{2}:\d{2}")

    def test_footer_present(self) -> None:
        self.assertIn("=" * 30, self.content)

    def test_no_date_in_time_report(self) -> None:
        self.assertNotRegex(self.content, r"\d{4}-\d{2}-\d{2}")


class TestFileWriterTemplate(unittest.TestCase):
    def test_write_overwrites_existing_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "out.txt")
            DateFileWriter().write(path)
            DateFileWriter().write(path)
            self.assertTrue(os.path.exists(path))

    def test_both_writers_produce_different_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            date_path = os.path.join(tmp, "date.txt")
            time_path = os.path.join(tmp, "time.txt")
            DateFileWriter().write(date_path)
            TimeFileWriter().write(time_path)
            with open(date_path) as d, open(time_path) as t:
                self.assertNotEqual(d.read(), t.read())

    def test_footer_shared_by_both_writers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            date_path = os.path.join(tmp, "date.txt")
            time_path = os.path.join(tmp, "time.txt")
            DateFileWriter().write(date_path)
            TimeFileWriter().write(time_path)
            for path in (date_path, time_path):
                with open(path) as f:
                    self.assertIn("=" * 30, f.read())


if __name__ == "__main__":
    unittest.main()
