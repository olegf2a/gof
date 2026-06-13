from datetime import datetime
from typing import IO

from ..file_writer import FileWriter


class TimeFileWriter(FileWriter):
    def _write_content(self, file: IO[str]) -> None:
        file.write("=== Time Report ===\n")
        file.write(f"Time: {datetime.now().strftime('%H:%M:%S')}\n")
