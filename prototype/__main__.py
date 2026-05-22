"""Demo script for the Car Prototype pattern"""

from .car_factory import CarFactory


def main():
    """Demonstrate the Car Prototype pattern"""
    print("🚗 Car Prototype Pattern Demo")
    print("=" * 50)

    # Show available prototypes
    CarFactory.show_prototypes()

    print("\n\n🔧 Creating Custom Cars:")
    print("=" * 50)

    # Create different cars with customizations
    cars = [
        CarFactory.create_sedan(color="Red", license_plate="FAST-01"),
        CarFactory.create_truck(color="White", license_plate="WORK-22"),
        CarFactory.create_minivan(license_plate="FAMILY"),  # Keep default blue color
        CarFactory.create_car("sedan", color="Black"),       # Using generic method
    ]

    for i, car in enumerate(cars, 1):
        print(f"\n{i}. {car}")
        specs = car.get_specifications()
        print("   Key Specifications:")
        for key in ['Type', 'Engine', 'Max Speed', 'Color', 'License Plate']:
            print(f"   {key}: {specs[key]}")

    # Demonstrate that immutable fields cannot be changed
    print("\n\n🔒 Demonstrating Immutable Fields:")
    print("=" * 50)

    sedan = CarFactory.create_sedan(color="Yellow", license_plate="TEST-123")
    print(f"Created: {sedan}")

    # This works - changing mutable field
    sedan.color = "Purple"
    print(f"After color change: {sedan}")

    # This will raise an error - trying to change immutable field
    try:
        sedan.engine_type = "V8"
        print("This shouldn't print - immutable field was changed!")
    except AttributeError as e:
        print(f"✓ Protection working: {e}")

    print(f"Final car: {sedan}")


if __name__ == "__main__":
    main()