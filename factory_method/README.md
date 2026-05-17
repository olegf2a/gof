# Factory Method Pattern

An implementation of the Factory Method design pattern using an oven and dish cooking system.

## Pattern Overview

The Factory Method pattern provides an interface for creating objects, but lets subclasses decide which class to instantiate. In this implementation:

- **Products**: Different types of dishes (Pizza, Lasagna, Cookies)
- **Creators**: Different types of ovens that create specific dishes
- **Factory Method**: Each oven implements `create_dish()` to produce its specialized dish

## Structure

```
factory_method/
  __init__.py          � Public API
  __main__.py          � Demo script
  dispatcher.py        � Factory function get_oven()
  dishes/              � Product classes
    base.py            � Abstract Dish
    pizza.py           � Concrete Pizza
    lasagna.py         � Concrete Lasagna
    cookies.py         � Concrete Cookies
  ovens/               � Creator classes
    base.py            � Abstract Oven with template method
    pizza_oven.py      � Concrete PizzaOven
    lasagna_oven.py    � Concrete LasagnaOven
    cookie_oven.py     � Concrete CookieOven
```

## Usage

### As a module:
```python
from factory_method import get_oven

# Get the appropriate oven for your dish
pizza_oven = get_oven('pizza')
result = pizza_oven.cook()
print(result)
```

### Run the demo:
```bash
python -m factory_method
```

## Key Components

1. **Abstract Product** (`Dish`): Defines interface for dishes
2. **Concrete Products** (`Pizza`, `Lasagna`, `Cookies`): Specific dish implementations
3. **Abstract Creator** (`Oven`): Defines factory method and template method for cooking
4. **Concrete Creators** (`PizzaOven`, `LasagnaOven`, `CookieOven`): Implement factory method
5. **Dispatcher**: Factory function that returns appropriate oven based on dish type

## Benefits

- **Extensibility**: Easy to add new dish types and corresponding ovens
- **Separation of Concerns**: Each oven knows how to create its specific dish
- **Template Method**: Common cooking process defined in base oven class
- **Type Safety**: Each oven creates the correct dish type

## Diagram

![img.png](img.png)