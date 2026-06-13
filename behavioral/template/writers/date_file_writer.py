from datetime import datetime
from typing import IO

from ..file_writer import FileWriter


class DateFileWriter(FileWriter):
    def _write_content(self, file: IO[str]) -> None:
        file.write("=== Date Report ===\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n")
