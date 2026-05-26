import threading
from typing import Optional

from .database_connection_base import DatabaseConnectionBase


class DatabaseConnectionSingleton(DatabaseConnectionBase):
    """
    Singleton that allows one instance.

    Uses __new__ with a threading lock to enforce the instance creation,
    even in multi-threaded environments.
    """

    _instance: Optional["DatabaseConnectionSingleton"] = None
    _lock = threading.Lock()

    def __new__(
        cls, host: str = "localhost", port: int = 5432, database: str = "mydb"
    ) -> "DatabaseConnectionSingleton":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    def connect(self) -> None:
        self.is_connected = True
        print(f"Connected to {self.host}:{self.port}/{self.database}")

    def execute_query(self, query: str) -> str:
        if not self.is_connected:
            raise RuntimeError("Not connected to database")
        return f"Result of '{query}' on {self.database}"

    def close(self) -> None:
        self.is_connected = False
