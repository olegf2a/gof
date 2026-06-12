from abc import ABC, abstractmethod
from typing import IO


class FileWriter(ABC):
    def write(self, filename: str) -> None:
        with open(filename, "w") as file:
            self._file: IO[str] = file
            self._write_content()
            self._write_footer()

    @abstractmethod
    def _write_content(self) -> None: ...

    def _write_footer(self) -> None:
        self._file.write("\n" + "=" * 30 + "\n")
