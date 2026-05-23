"""Singleton Pattern Implementation"""

from .database_connection_base import DatabaseConnectionBase
from .database_connection_multiton import DatabaseConnectionMultiton
from .database_connection_object_pool import DatabaseConnectionObjectPool
from .database_connection_singleton import DatabaseConnectionSingleton

__all__ = [
    "DatabaseConnectionObjectPool",
    "DatabaseConnectionSingleton",
    "DatabaseConnectionBase",
    "DatabaseConnectionMultiton",
]
