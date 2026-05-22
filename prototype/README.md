# Prototype Pattern

An implementation of the Prototype design pattern using a car manufacturing system with predefined vehicle variants.

## Problem and Solution

### The Problem
When building applications that need to create complex objects with predefined configurations, you often face these challenges:

- **Expensive Object Creation**: Creating complex objects from scratch is costly in terms of performance and resources
- **Configuration Complexity**: Objects have many parameters, making direct instantiation error-prone and verbose
- **Inflexible Variations**: Need multiple similar objects with slight variations, but creating separate classes for each variant is impractical
- **Inconsistent State Management**: Mixing mutable and immutable properties without proper controls leads to unexpected modifications

For example, imagine a car manufacturing system that needs to produce different vehicle types. Without proper abstraction, you might end up with code like:
```python
# Expensive and error-prone object creation
sedan = Car(
    car_type="Sedan",
    engine_type="2.0L Inline-4 Turbo",
    transmission="8-Speed Automatic",
    body_style="4-Door Sedan",
    wheels=4,
    doors=4,
    max_speed=180,
    fuel_capacity=60.0,
    color="Red",  # Customer choice
    license_plate="ABC-123"  # Customer choice
)

# Risk: accidentally changing immutable properties
sedan.engine_type = "V8"  # Should not be allowed!
```

### The Solution
The Prototype pattern solves these problems by:

1. **Predefined Object Templates**: Create prototype instances with all complex configurations already set
2. **Efficient Cloning**: Copy existing objects instead of creating from scratch
3. **Controlled Customization**: Allow modification of only specific fields (color, license plate) while protecting others
4. **Encapsulated Creation**: Hide the cloning mechanism behind convenient factory methods

In our car manufacturing example:
```python
# Simple, efficient, and safe car creation
sedan = CarFactory.create_sedan(color="Red", license_plate="ABC-123")

# Only customizable fields can be changed
sedan.color = "Blue"  # ✓ Allowed
sedan.engine_type = "V8"  # ✗ Raises AttributeError
```

## Pattern Overview

The Prototype pattern creates new objects by cloning existing prototype instances, allowing for efficient object creation with predefined configurations. In this implementation:

- **Prototype Class**: `Car` class with immutable base configuration and customizable properties
- **Predefined Prototypes**: Three car variants (Sedan, Truck, Minivan) with complete specifications
- **Factory Interface**: `CarFactory` provides convenient methods without exposing clone operations
- **Protected Cloning**: Internal `_clone()` method ensures clients use proper factory methods

## Structure

```
prototype/
├── __init__.py          ← Public API
├── __main__.py          ← Demo script
├── client_demo.py       ← Client usage example
├── cars.py              ← Car prototype class and predefined variants
└── car_factory.py       ← Factory methods for creating car instances
```

## Usage

### As a module:
```python
from prototype import CarFactory

# Create different car types with customizations
sedan = CarFactory.create_sedan(color="Red", license_plate="FAST-01")
truck = CarFactory.create_truck(color="White", license_plate="WORK-22")
minivan = CarFactory.create_minivan(license_plate="FAMILY")

print(sedan)  # Red Sedan (FAST-01)
```

### Run the demo:
```bash
python -m prototype
```

### Run client example:
```bash
python [prototype_client_demo.py](../prototype_client_demo.py)
```

## Key Components

1. **Prototype Class** (`Car`): Defines the structure with both immutable and customizable properties
2. **Predefined Prototypes**: Three configured car instances (SEDAN_PROTOTYPE, TRUCK_PROTOTYPE, MINIVAN_PROTOTYPE)
3. **Factory Class** (`CarFactory`): Provides convenient creation methods without exposing clone operation
4. **Protection Mechanism**: `__setattr__` override prevents modification of immutable fields after creation

## Car Variants

### 🚗 Sedan
- **Engine**: 2.0L Inline-4 Turbo
- **Transmission**: 8-Speed Automatic
- **Body**: 4-Door Sedan
- **Max Speed**: 180 km/h
- **Fuel Capacity**: 60L
- **Default Color**: Silver

### 🚚 Pickup Truck
- **Engine**: 3.5L V6 Twin-Turbo
- **Transmission**: 10-Speed Automatic
- **Body**: Crew Cab Pickup
- **Max Speed**: 160 km/h
- **Fuel Capacity**: 90L
- **Default Color**: Black

### 🚐 Minivan
- **Engine**: 3.6L V6
- **Transmission**: 9-Speed Automatic
- **Body**: Passenger Van
- **Max Speed**: 170 km/h
- **Fuel Capacity**: 75L
- **Default Color**: Blue

## Benefits

- **Performance**: Cloning existing objects is faster than creating from scratch
- **Consistency**: Predefined prototypes ensure correct configurations
- **Flexibility**: Easy customization of specific properties (color, license plate)
- **Protection**: Immutable fields cannot be accidentally modified after creation
- **Simplicity**: Clean factory interface hides complexity from clients
- **Extensibility**: Easy to add new car variants by creating new prototypes

## Advanced Features

### Field Protection
```python
car = CarFactory.create_sedan()
car.color = "Green"  # ✓ Allowed - mutable field
car.engine_type = "V8"  # ✗ Raises AttributeError - immutable field
```

### Generic Creation
```python
# Create any type using string identifier
car = CarFactory.create_car("sedan", color="Blue", license_plate="TEST-123")
```

### Prototype Information
```python
# Display all available prototypes
CarFactory.show_prototypes()

# Get available car types
types = CarFactory.get_available_types()  # ["sedan", "truck", "minivan"]
```

## UML Diagrams

### Pattern Structure
![Prototype UML](prototype_uml.png)

### Creation Flow
![Prototype Flow](prototype_flow.png)
