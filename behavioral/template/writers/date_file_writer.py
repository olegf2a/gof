from datetime import datetime

from ..file_writer import FileWriter


class DateFileWriter(FileWriter):
    def _write_content(self) -> None:
        self._file.write("=== Date Report ===\n")
        self._file.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n")
