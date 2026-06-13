import os
import tempfile

from .writers.date_file_writer import DateFileWriter
from .writers.time_file_writer import TimeFileWriter


def demo() -> None:
    print("=== Template Method Pattern — File Writer ===\n")

    with tempfile.TemporaryDirectory() as tmp:
        date_path = os.path.join(tmp, "date_report.txt")
        time_path = os.path.join(tmp, "time_report.txt")

        DateFileWriter().write(date_path)
        TimeFileWriter().write(time_path)

        for path in (date_path, time_path):
            print(f"--- {os.path.basename(path)} ---")
            with open(path) as f:
                print(f.read())


if __name__ == "__main__":
    demo()
