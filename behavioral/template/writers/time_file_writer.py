from datetime import datetime

from ..file_writer import FileWriter


class TimeFileWriter(FileWriter):
    def _write_content(self) -> None:
        self._file.write("=== Time Report ===\n")
        self._file.write(f"Time: {datetime.now().strftime('%H:%M:%S')}\n")
