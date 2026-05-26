"""Car Factory that provides convenient methods for creating car prototypes"""

from typing import Optional

from .cars import MINIVAN_PROTOTYPE, SEDAN_PROTOTYPE, TRUCK_PROTOTYPE, Car


class CarFactory:
    """
    Factory class that provides convenient methods for creating different car types.

    This factory encapsulates the prototype pattern implementation and provides
    a clean interface for clients to create cars without directly accessing
    the clone method.
    """

    @staticmethod
    def create_sedan(
        color: Optional[str] = None, license_plate: Optional[str] = None
    ) -> Car:
        """
        Create a sedan car with optional customizations.

        Args:
            color: Custom color (defaults to Silver)
            license_plate: Custom license plate (defaults to SED-001)

        Returns:
            Customized sedan car instance
        """
        return SEDAN_PROTOTYPE.customize(color=color, license_plate=license_plate)

    @staticmethod
    def create_truck(
        color: Optional[str] = None, license_plate: Optional[str] = None
    ) -> Car:
        """
        Create a pickup truck with optional customizations.

        Args:
            color: Custom color (defaults to Black)
            license_plate: Custom license plate (defaults to TRK-001)

        Returns:
            Customized pickup truck instance
        """
        return TRUCK_PROTOTYPE.customize(color=color, license_plate=license_plate)

    @staticmethod
    def create_minivan(
        color: Optional[str] = None, license_plate: Optional[str] = None
    ) -> Car:
        """
        Create a minivan with optional customizations.

        Args:
            color: Custom color (defaults to Blue)
            license_plate: Custom license plate (defaults to VAN-001)

        Returns:
            Customized minivan instance
        """
        return MINIVAN_PROTOTYPE.customize(color=color, license_plate=license_plate)

    @staticmethod
    def get_available_types() -> list[str]:
        """
        Get list of available car types.

        Returns:
            List of available car type names
        """
        return ["sedan", "truck", "minivan"]

    @staticmethod
    def create_car(
        car_type: str, color: Optional[str] = None, license_plate: Optional[str] = None
    ) -> Car:
        """
        Create a car of the specified type with optional customizations.

        Args:
            car_type: Type of car to create (sedan, truck, minivan)
            color: Custom color (optional)
            license_plate: Custom license plate (optional)

        Returns:
            Customized car instance

        Raises:
            ValueError: If car_type is not supported
        """
        car_type_lower = car_type.lower()

        if car_type_lower == "sedan":
            return CarFactory.create_sedan(color, license_plate)
        elif car_type_lower == "truck":
            return CarFactory.create_truck(color, license_plate)
        elif car_type_lower == "minivan":
            return CarFactory.create_minivan(color, license_plate)
        else:
            available = ", ".join(CarFactory.get_available_types())
            raise ValueError(
                f"Unsupported car type '{car_type}'. Available types: {available}"
            )

    @staticmethod
    def show_prototypes() -> None:
        """Display information about all available car prototypes"""
        print("🚗 Available Car Prototypes:")
        print("=" * 50)

        prototypes = [
            ("Sedan", SEDAN_PROTOTYPE),
            ("Pickup Truck", TRUCK_PROTOTYPE),
            ("Minivan", MINIVAN_PROTOTYPE),
        ]

        for name, prototype in prototypes:
            print(f"\n{name}:")
            specs = prototype.get_specifications()
            for key, value in specs.items():
                if key not in ["Color", "License Plate"]:  # Skip customizable fields
                    print(f"  {key}: {value}")
            print(f"  Default Color: {prototype.color}")
            print(f"  Default License: {prototype.license_plate}")
