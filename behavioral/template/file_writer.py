from abc import ABC, abstractmethod
from typing import IO


class FileWriter(ABC):
    def write(self, filename: str) -> None:
        with open(filename, "w") as file:
            self._write_content(file)
            self._write_footer(file)

    @abstractmethod
    def _write_content(self, file: IO[str]) -> None: ...

    def _write_footer(self, file: IO[str]) -> None:
        file.write("\n" + "=" * 30 + "\n")
