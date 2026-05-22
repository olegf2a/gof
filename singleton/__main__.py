"""Demo script for the Limited Singleton pattern"""

from .database_connection import DatabaseConnection


def main():
    print("Limited Singleton Pattern Demo (max 10 instances)")
    print("=" * 50)

    DatabaseConnection.reset_pool()

    # Create connections up to the limit
    print("\n1. Creating connections...")
    connections = []
    for i in range(12):
        try:
            conn = DatabaseConnection(f"db{i+1}.example.com", 5432, f"app_db_{i+1}")
            conn.connect()
            connections.append(conn)
        except RuntimeError as e:
            print(f"   Connection {i+1} failed: {e}")

    print(f"\n   Created {len(connections)} / 12 requested")
    print(f"   Active instances: {DatabaseConnection.get_instance_count()}")

    # Execute queries
    print("\n2. Executing queries...")
    for conn in connections[:3]:
        print(f"   {conn.execute_query('SELECT 1')}")

    # Close some and create new ones
    print("\n3. Closing 2 connections and creating new ones...")
    connections[0].close()
    connections[1].close()

    new_conn = DatabaseConnection("new.db.com", 5432, "new_db")
    new_conn.connect()
    print(f"   New connection: {new_conn}")
    print(f"   Active instances: {DatabaseConnection.get_instance_count()}")


if __name__ == "__main__":
    main()
