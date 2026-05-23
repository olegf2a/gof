"""Object Pool implementation using metaclass approach"""

import threading
from typing import Any, Dict, List


class ObjectPoolMeta(type):
    """Metaclass that caches instances by constructor arguments.

    A class using ``Multiton`` as its metaclass returns the same instance
    for any given combination of constructor arguments. Calling the class
    with a new argument set produces a new instance; calling it again with
    a previously seen argument set returns the cached object.

    This is the generalization of the Singleton pattern: Singleton caches
    one instance per class, Multiton caches one instance per (class, args)
    key.

    Why a metaclass instead of ``__new__``
    --------------------------------------
    Instance caching can also be implemented by overriding ``__new__`` on
    the target class, but this has a subtle defect: Python always invokes
    ``__init__`` after ``__new__`` returns an instance of the class, even
    when that instance came from a cache. Re-running ``__init__`` resets
    any attributes assigned there, silently destroying state accumulated
    on the cached object.

    The metaclass approach intercepts construction one level higher, at
    ``type.__call__``. On a cache hit, ``Multiton.__call__`` returns the
    cached instance without delegating to ``super().__call__``, so neither
    ``__new__`` nor ``__init__`` runs a second time. ``__init__`` is
    therefore guaranteed to execute exactly once per unique key.

    Thread safety
    -------------
    Concurrent calls are guarded with double-checked locking: a fast,
    lock-free check on the common path, and a second check inside the
    lock on the rare miss path. This prevents two threads from both
    seeing an empty cache and constructing duplicate instances.

    Key generation
    --------------
    Instances are keyed by a string derived from the class, positional
    arguments, and the sorted keyword arguments. The default
    implementation in :meth:`_generate_instance_key` may be inadequate
    for arguments whose ``repr`` is unstable or non-unique (e.g. objects
    without ``__repr__`` overrides, mutable containers). Subclasses can
    override :meth:`_generate_instance_key` to define a domain-specific
    key.

    Caveats
    -------
    - Cached instances live for the lifetime of the metaclass and are
      not garbage collected while the cache holds a strong reference.
      For long-running processes with many distinct keys, consider
      using ``weakref.WeakValueDictionary`` for ``_instances``.
    - Because ``__init__`` runs only on the first call, arguments
      passed to later calls with the same key are silently ignored.
      Callers may reasonably expect the new arguments to take effect;
      document this behavior on classes that use the metaclass.
    - The cache is shared across all classes that use this metaclass.
      The class itself is part of the key, so collisions across
      classes do not occur, but the single ``dict`` is a shared
      resource and a single lock serializes construction of all
      Multiton classes.

    Example
    -------
    ::

        class Database(metaclass=Multiton):
            def __init__(self, host, port):
                self.host = host
                self.port = port

        db1 = Database("localhost", 5432)
        db2 = Database("localhost", 5432)
        db3 = Database("remote", 5432)

        assert db1 is db2       # same args -> same instance
        assert db1 is not db3   # different args -> new instance
    """

    def __init__(cls, name: str, bases: tuple, attrs: dict) -> None:
        super().__init__(name, bases, attrs)
        cls._pool: List[Any] = []
        cls._active_instances: Dict[int, Any] = {}
        cls._lock = threading.Lock()
        cls._max_pool_size = getattr(cls, "_max_pool_size", 5)

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Override instance creation to implement object pool pattern.

        Returns an instance from the pool if available, otherwise creates new one
        up to the maximum pool size limit.
        """
        with cls._lock:
            # Try to get instance from pool
            if cls._pool:
                instance = cls._pool.pop()
                # Re-initialize with new parameters
                instance.__init__(*args, **kwargs)
                cls._active_instances[id(instance)] = instance
                return instance

            # Check if we've reached the maximum number of total instances
            total_instances = len(cls._active_instances) + len(cls._pool)
            if total_instances >= cls._max_pool_size:
                raise RuntimeError(
                    f"Cannot create more instances. "
                    f"Pool limit reached: {cls._max_pool_size} "
                    f"(Active: {len(cls._active_instances)}, "
                    f"Pooled: {len(cls._pool)})"
                )

            # Create new instance
            instance = super(ObjectPoolMeta, cls).__call__(*args, **kwargs)
            cls._active_instances[id(instance)] = instance
            return instance

    def get_pool_stats(cls) -> Dict[str, int]:
        """Get current pool statistics"""
        with cls._lock:
            return {
                "active_instances": len(cls._active_instances),
                "pooled_instances": len(cls._pool),
                "total_instances": len(cls._active_instances) + len(cls._pool),
                "max_pool_size": cls._max_pool_size,
            }

    def clear_pool(cls) -> None:
        """Clear all instances from the pool"""
        with cls._lock:
            cls._pool.clear()
            cls._active_instances.clear()


class DatabaseConnectionMetaclass(metaclass=ObjectPoolMeta):
    """
    Database connection using metaclass-based object pool pattern.

    Instances are automatically managed by the metaclass - when closed,
    they return to the pool for reuse.
    """

    _max_pool_size = 5  # Configure pool size

    def __init__(
        self, host: str = "localhost", port: int = 5432, database: str = "mydb"
    ) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.is_connected = False
        self._pool_id = id(self)

    def connect(self) -> None:
        """Establish connection to the database"""
        self.is_connected = True
        print(f"[Pool] Connected to {self.host}:{self.port}/{self.database}")

    def execute_query(self, query: str) -> str:
        """Execute a query and return the result"""
        if not self.is_connected:
            raise RuntimeError("Not connected to database")
        return f"[Pool] Result of '{query}' on {self.database}"

    def close(self) -> None:
        """Close connection and return instance to pool"""
        self.is_connected = False
        print(f"[Pool] Connection to {self.database} closed, returning to pool")

        with self.__class__._lock:
            # Remove from active instances
            if self._pool_id in self.__class__._active_instances:
                del self.__class__._active_instances[self._pool_id]

            # Return to pool for reuse
            if self not in self.__class__._pool:
                self.__class__._pool.append(self)

    def __str__(self) -> str:
        status = "connected" if self.is_connected else "disconnected"
        return f"DatabaseConnectionMetaclass({self.host}:{self.port}/{self.database}, {status}, pool_id={self._pool_id})"

    @classmethod
    def get_pool_info(cls) -> str:
        """Get formatted pool information"""
        stats = cls.get_pool_stats()
        return (
            f"Pool Stats: "
            f"Active={stats['active_instances']}, "
            f"Pooled={stats['pooled_instances']}, "
            f"Total={stats['total_instances']}, "
            f"Limit={stats['max_pool_size']}"
        )


# Usage example and demonstration
if __name__ == "__main__":
    print("=== Metaclass Object Pool Demo ===")

    # Create instances
    print("\n1. Creating connections...")
    conn1 = DatabaseConnectionMetaclass("db1.example.com", 5432, "users")
    conn2 = DatabaseConnectionMetaclass("db2.example.com", 5432, "orders")

    print(f"Created: {conn1}")
    print(f"Created: {conn2}")
    print(f"Pool info: {DatabaseConnectionMetaclass.get_pool_info()}")

    # Use connections
    print("\n2. Using connections...")
    conn1.connect()
    result = conn1.execute_query("SELECT * FROM users")
    print(f"Query result: {result}")

    # Close and return to pool
    print("\n3. Closing connections...")
    conn1.close()
    print(
        f"Pool info after closing conn1: {DatabaseConnectionMetaclass.get_pool_info()}"
    )

    # Reuse from pool
    print("\n4. Creating new connection (should reuse from pool)...")
    conn3 = DatabaseConnectionMetaclass("db3.example.com", 5432, "products")
    print(f"Reused: {conn3}")
    print(f"Pool info: {DatabaseConnectionMetaclass.get_pool_info()}")
