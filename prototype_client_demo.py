"""Client demonstration of the Car Prototype pattern"""

from prototype.car_factory import CarFactory


def demonstrate_car_dealership() -> None:
    """Simulate a car dealership using the prototype pattern"""
    print("🏢 Car Dealership Simulation")
    print("=" * 40)

    # Customer 1: Wants a red sedan
    print("\n👤 Customer 1: 'I want a red sedan with plate ABC-123'")
    car1 = CarFactory.create_sedan(color="Red", license_plate="ABC-123")
    print(f"   Created: {car1}")

    # Customer 2: Wants a default truck but with custom plate
    print("\n👤 Customer 2: 'I'll take a standard truck but with my custom plate'")
    car2 = CarFactory.create_truck(license_plate="HAUL-ME")
    print(f"   Created: {car2}")

    # Customer 3: Wants to see available options first
    print("\n👤 Customer 3: 'What types do you have?'")
    available = CarFactory.get_available_types()
    print(f"   Available: {', '.join(available)}")
    print("   Customer: 'I'll take a blue minivan'")
    car3 = CarFactory.create_minivan(color="Navy Blue", license_plate="KIDZ-VAN")
    print(f"   Created: {car3}")

    # Show all created cars
    print(f"\n📋 Today's Sales Summary:")
    cars_sold = [car1, car2, car3]
    for i, car in enumerate(cars_sold, 1):
        print(f"   {i}. {car}")

    # Demonstrate that each car is independent
    print(f"\n🔧 Demonstrating Independence:")
    print(f"   Car1: {car1}")
    print(f"   Changing car1 color to Green...")
    car1.color = "Green"
    print(f"   Car1: {car1}")
    print(f"   Car2: {car2} (unchanged)")
    print(f"   Car3: {car3} (unchanged)")


if __name__ == "__main__":
    demonstrate_car_dealership()
