# Builder Pattern - Custom Pizza Builder

A simple implementation of the Builder pattern for creating custom pizzas with various toppings according to user preferences.

## Task Description

Create a program using the Builder pattern:

- ❑ Create custom pizzas
- ❑ Based on user's custom recipe containing different combinations of:
  - ❑ Cheese
  - ❑ Bacon
  - ❑ Pineapple
  - ❑ Mushrooms
  - ❑ Seafood

## Problem and Solution

### The Problem
Creating complex objects with many optional components can lead to:

- **Constructor Overload**: Too many constructor parameters become unmanageable
- **Telescoping Constructor**: Multiple constructors with different parameter combinations
- **Immutable Object Creation**: Difficulty in creating immutable objects step by step
- **Unclear Object Creation**: Complex creation logic scattered throughout the code

For example, without Builder pattern:
```python
# Unclear and error-prone
pizza1 = Pizza("large", "thin", ["cheese", "bacon", "pineapple"])
pizza2 = Pizza("medium", "regular", ["cheese", "mushrooms", "seafood"])
# What if you forget the order of parameters?
```

### The Solution
The Builder pattern solves these problems by:

1. **Step-by-step Construction**: Build objects incrementally using fluent interface
2. **Method Chaining**: Chain method calls for readable object creation
3. **Internal Build Method**: Keep the build logic within the builder class
4. **Flexible Configuration**: Easy to add or modify object properties

With Builder pattern:
```python
# Clear and readable
pizza = (PizzaBuilder()
    .set_size("large")
    .add_cheese("mozzarella")
    .add_bacon()
    .add_pineapple()
    .build())
```

## Pattern Overview

This implementation uses the Builder pattern with the build method inside the builder class itself, allowing for:

- **Pizza**: The product being built with size, crust, and toppings
- **PizzaBuilder**: The builder class with fluent interface and internal build() method
- **Method Chaining**: Each method returns the builder instance for chaining
- **Required Toppings**: All five toppings from the task (cheese, bacon, pineapple, mushrooms, seafood)

## Structure

```
builder/
├── __init__.py          ← Public API
├── __main__.py          ← Demo script with interactive builder
├── pizza.py             ← Pizza product class
├── pizza_builder.py     ← PizzaBuilder with internal build() method
├── tests/               ← Unit tests
│   ├── __init__.py      ← Tests package
│   └── test_pizza_builder.py ← Comprehensive unit tests
├── builder_structure_uml.puml ← Class structure UML diagram
├── builder_flow_uml.puml ← Sequence flow UML diagram
└── README.md            ← This documentation
```

## Usage

### As a module:
```python
from builder import PizzaBuilder

# Create a Hawaiian pizza
hawaiian = (PizzaBuilder()
    .set_size("large")
    .set_crust("thin")
    .add_cheese("mozzarella")
    .add_bacon()
    .add_pineapple()
    .build())

print(hawaiian)  # Large thin crust pizza with: mozzarella cheese, bacon, pineapple
print(f"Price: ${hawaiian.get_price():.2f}")  # Price: $21.49
```

### Run the demo:
```bash
python -m builder
```

This will run several pre-configured examples plus an interactive pizza builder where you can create your own custom pizza.

### Run the tests:
```bash
python -m builder.tests.test_pizza_builder
```

This will run all 38 unit tests covering both Pizza and PizzaBuilder classes with comprehensive test coverage.

## Available Toppings

### Required Toppings (From Task):
- **🧀 Cheese**: `add_cheese(type)` - mozzarella, cheddar, parmesan, goat cheese, etc.
- **🥓 Bacon**: `add_bacon()` - crispy bacon strips
- **🍍 Pineapple**: `add_pineapple()` - sweet pineapple chunks
- **🍄 Mushrooms**: `add_mushrooms(type)` - button, shiitake, portobello, etc.
- **🦐 Seafood**: `add_seafood(type)` - shrimp, mussels, calamari, etc.

### Additional Toppings:
- **🍕 Pepperoni**: `add_pepperoni()` - classic pepperoni slices
- **🥬 Vegetables**: `add_vegetables(type)` - tomatoes, onions, bell peppers, spinach, etc.
- **🎯 Custom**: `add_custom_topping(name)` - any custom topping

## Pizza Configuration

### Sizes:
- **Small**: Base price $8.99
- **Medium**: Base price $12.99
- **Large**: Base price $16.99

### Crust Types:
- **Thin**: Crispy thin crust
- **Regular**: Standard crust
- **Thick**: Deep dish thick crust

### Pricing:
- Base price depends on size
- Each topping adds $1.50

## Key Features

1. **Fluent Interface**: Method chaining for readable code
2. **Internal Build Method**: Build() method exists within the PizzaBuilder class
3. **Reset Capability**: Builder resets after each build for reuse
4. **Type Safety**: Proper type hints throughout
5. **Interactive Demo**: User can build custom pizzas interactively
6. **Price Calculation**: Automatic price calculation based on size and toppings

## Example Combinations

### Hawaiian Pizza:
```python
hawaiian = (PizzaBuilder()
    .set_size("large")
    .add_cheese("mozzarella")
    .add_bacon()
    .add_pineapple()
    .build())
```

### Seafood Deluxe:
```python
seafood = (PizzaBuilder()
    .set_size("medium")
    .add_cheese("parmesan")
    .add_seafood("shrimp")
    .add_seafood("mussels")
    .add_mushrooms("shiitake")
    .build())
```

### Vegetarian Special:
```python
veggie = (PizzaBuilder()
    .set_size("small")
    .add_cheese("goat cheese")
    .add_mushrooms("portobello")
    .add_vegetables("tomatoes")
    .add_vegetables("spinach")
    .build())
```

## Benefits

- **Readable Code**: Fluent interface makes pizza creation clear and intuitive
- **Flexible**: Easy to add new toppings or modify existing ones
- **Reusable**: Builder can be reused to create multiple pizzas
- **Maintainable**: Adding new features doesn't break existing code
- **Self-contained**: Build method is part of the builder class as requested

## UML Diagrams

### Class Structure
See [builder_structure_uml.puml](builder_structure_uml.puml) for the complete class diagram showing the relationship between Pizza, PizzaBuilder, and client code.

### Sequence Flow
See [builder_flow_uml.puml](builder_flow_uml.puml) for the sequence diagram showing the step-by-step flow of pizza construction using the Builder pattern.
