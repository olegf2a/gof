"""Car prototype implementation with predefined variants"""

import copy
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Car:
    """
    Car prototype that supports cloning with modification of color and license plate only.

    This class implements the Prototype pattern by maintaining predefined configurations
    and allowing only specific fields (color and license_plate) to be modified.
    """

    # Immutable characteristics (cannot be changed after creation)
    car_type: str
    engine_type: str
    transmission: str
    body_style: str
    wheels: int
    doors: int
    max_speed: int
    fuel_capacity: float

    # Mutable characteristics (can be customized)
    color: str = "White"
    license_plate: str = "TEMP-000"

    def __post_init__(self) -> None:
        """Ensure immutable fields cannot be modified after creation"""
        # Store original values to detect unauthorized changes
        self._original_config = {
            "car_type": self.car_type,
            "engine_type": self.engine_type,
            "transmission": self.transmission,
            "body_style": self.body_style,
            "wheels": self.wheels,
            "doors": self.doors,
            "max_speed": self.max_speed,
            "fuel_capacity": self.fuel_capacity,
        }

    def _clone(self) -> "Car":
        """
        Internal clone method - should not be called directly by client code.
        Creates a deep copy of the current car instance.
        """
        return copy.deepcopy(self)

    def customize(
        self, color: Optional[str] = None, license_plate: Optional[str] = None
    ) -> "Car":
        """
        Create a customized copy of this car with new color and/or license plate.

        Args:
            color: New color for the car (optional)
            license_plate: New license plate for the car (optional)

        Returns:
            New Car instance with specified customizations
        """
        new_car = self._clone()

        if color is not None:
            new_car.color = color
        if license_plate is not None:
            new_car.license_plate = license_plate

        return new_car

    def get_specifications(self) -> Dict[str, Any]:
        """Get complete car specifications"""
        return {
            "Type": self.car_type,
            "Engine": self.engine_type,
            "Transmission": self.transmission,
            "Body Style": self.body_style,
            "Wheels": self.wheels,
            "Doors": self.doors,
            "Max Speed": f"{self.max_speed} km/h",
            "Fuel Capacity": f"{self.fuel_capacity}L",
            "Color": self.color,
            "License Plate": self.license_plate,
        }

    def __str__(self) -> str:
        """String representation of the car"""
        return f"{self.color} {self.car_type} ({self.license_plate})"

    def __setattr__(self, name: str, value: Any) -> None:
        """Override setattr to prevent modification of immutable fields after initialization"""
        # Allow setting during initialization
        if not hasattr(self, "_original_config"):
            super().__setattr__(name, value)
            return

        # Allow modification of mutable fields only
        if name in ["color", "license_plate"]:
            super().__setattr__(name, value)
        elif name in self._original_config:
            raise AttributeError(
                f"Cannot modify immutable field '{name}' after car creation"
            )
        else:
            super().__setattr__(name, value)


# Predefined car prototypes
SEDAN_PROTOTYPE = Car(
    car_type="Sedan",
    engine_type="2.0L Inline-4 Turbo",
    transmission="8-Speed Automatic",
    body_style="4-Door Sedan",
    wheels=4,
    doors=4,
    max_speed=180,
    fuel_capacity=60.0,
    color="Silver",
    license_plate="SED-001",
)

TRUCK_PROTOTYPE = Car(
    car_type="Pickup Truck",
    engine_type="3.5L V6 Twin-Turbo",
    transmission="10-Speed Automatic",
    body_style="Crew Cab Pickup",
    wheels=4,
    doors=4,
    max_speed=160,
    fuel_capacity=90.0,
    color="Black",
    license_plate="TRK-001",
)

MINIVAN_PROTOTYPE = Car(
    car_type="Minivan",
    engine_type="3.6L V6",
    transmission="9-Speed Automatic",
    body_style="Passenger Van",
    wheels=4,
    doors=5,
    max_speed=170,
    fuel_capacity=75.0,
    color="Blue",
    license_plate="VAN-001",
)
