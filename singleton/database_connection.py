"""Limited Singleton pattern — DatabaseConnection with max 10 instances"""

import threading


class DatabaseConnection:
    """
    Limited Singleton that allows at most 10 instances.

    Uses __new__ with a threading lock to enforce the instance cap,
    even in multi-threaded environments.
    """

    _instances: list["DatabaseConnection"] = []
    _lock = threading.Lock()
    _max_instances = 10

    def __new__(cls, host: str = "localhost", port: int = 5432, database: str = "mydb"):
        with cls._lock:
            if len(cls._instances) >= cls._max_instances:
                raise RuntimeError(
                    f"Cannot create more than {cls._max_instances} instances "
                    f"(current: {len(cls._instances)})"
                )
            instance = super().__new__(cls)
            cls._instances.append(instance)
            return instance

    def __init__(self, host: str = "localhost", port: int = 5432, database: str = "mydb"):
        if hasattr(self, "_initialized"):
            return
        self._initialized = True
        self.host = host
        self.port = port
        self.database = database
        self.is_connected = False

    def connect(self) -> None:
        self.is_connected = True
        print(f"Connected to {self.host}:{self.port}/{self.database}")

    def execute_query(self, query: str) -> str:
        if not self.is_connected:
            raise RuntimeError("Not connected to database")
        return f"Result of '{query}' on {self.database}"

    def close(self) -> None:
        self.is_connected = False
        with self._lock:
            if self in self._instances:
                self._instances.remove(self)
        print(f"Connection to {self.database} closed")

    @classmethod
    def get_instance_count(cls) -> int:
        with cls._lock:
            return len(cls._instances)

    @classmethod
    def reset_pool(cls) -> None:
        with cls._lock:
            cls._instances.clear()

    def __str__(self) -> str:
        status = "connected" if self.is_connected else "disconnected"
        return f"DatabaseConnection({self.host}:{self.port}/{self.database}, {status})"
