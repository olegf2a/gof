"""Abstract base class for database connection patterns"""

from abc import ABC, abstractmethod


class DatabaseConnectionBase(ABC):
    """
    Abstract base class defining the common interface for all database connections.

    This class provides the contract that all concrete database connection
    implementations (singleton, limited pool, etc.) must follow.
    """

    def __init__(
        self, host: str = "localhost", port: int = 5432, database: str = "mydb"
    ) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.is_connected = False

    @abstractmethod
    def connect(self) -> None:
        """Establish connection to the database"""
        pass

    @abstractmethod
    def execute_query(self, query: str) -> str:
        """Execute a query and return the result"""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the database connection"""
        pass

    def __str__(self) -> str:
        status = "connected" if self.is_connected else "disconnected"
        return f"{self.__class__.__name__}({self.host}:{self.port}/{self.database}, {status})"
