"""Client demonstration of the Limited Singleton pattern"""

from singleton import DatabaseConnection


def main():
    print("Limited Singleton Client Demo")
    print("=" * 40)

    DatabaseConnection.reset_pool()

    # Create a pool of connections
    pool = []
    for i in range(5):
        conn = DatabaseConnection("prod.db.com", 5432, f"shard_{i}")
        conn.connect()
        pool.append(conn)

    print(f"Pool size: {DatabaseConnection.get_instance_count()}")

    # Use connections
    for conn in pool:
        print(conn.execute_query(f"SELECT * FROM {conn.database}.users"))

    # Try to exceed the 10-instance limit
    print("\nCreating 5 more to hit the limit...")
    for i in range(5, 10):
        conn = DatabaseConnection("prod.db.com", 5432, f"shard_{i}")
        conn.connect()
        pool.append(conn)

    print(f"Pool size: {DatabaseConnection.get_instance_count()}")

    print("\nAttempting 11th connection...")
    try:
        DatabaseConnection("prod.db.com", 5432, "shard_overflow")
    except RuntimeError as e:
        print(f"Failed as expected: {e}")

    # Cleanup
    for conn in pool:
        conn.close()

    print(f"After cleanup: {DatabaseConnection.get_instance_count()} instances")


if __name__ == "__main__":
    main()
