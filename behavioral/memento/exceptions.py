class MementoException(Exception): ...


class VersionNotFoundException(MementoException):
    def __init__(self, version: str) -> None:
        super().__init__(f"Version '{version}' not found.")
