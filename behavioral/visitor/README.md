# Visitor Pattern

An implementation of the Visitor design pattern for a custom pizza recipe — five ingredients (Cheese, Bacon, Pineapple, Mushroom, Seafood) act as elements; two visitors add operations (cooking instructions and price calculation) without modifying any ingredient class.

![visitor_general_uml.png](uml/visitor_general_uml.png)

## Problem and Solution

### The Problem
Without the pattern, adding a new operation (e.g. calorie count) requires editing every ingredient class:

```python
class Cheese:
    def cook(self):   print("Melting cheese...")
    def price(self):  return 1.50
    def calories(self): return 320   # must touch every ingredient to add this
```

### The Solution
Each operation is a visitor class. Ingredients stay untouched — just add a new visitor:

```python
from behavioral.visitor.pizza import Pizza
from behavioral.visitor.ingredients.cheese import Cheese
from behavioral.visitor.ingredients.bacon import Bacon
from behavioral.visitor.visitors.cook_visitor import CookVisitor
from behavioral.visitor.visitors.price_visitor import PriceVisitor

pizza = Pizza()
pizza.add(Cheese())
pizza.add(Bacon())

pizza.accept(CookVisitor())
# → [Cook] Cheese: melting on the base.
# → [Cook] Bacon: frying until crispy.

price = PriceVisitor()
pizza.accept(price)
print(price.total)   # → 3.50
```

## Pattern Overview

- **Ingredient** (`ingredient.py`): ABC — declares `name`, `price` properties and `accept(visitor)`
- **Cheese, Bacon, Pineapple, Mushroom, Seafood** (`ingredients/`): concrete elements — each implements `name`, `price`, and `accept()` which calls the matching `visitor.visit_*()` method
- **Visitor** (`visitor.py`): ABC — one abstract `visit_*()` method per ingredient type
- **CookVisitor** (`visitors/cook_visitor.py`): prints a cooking instruction using `ingredient.name`
- **PriceVisitor** (`visitors/price_visitor.py`): accumulates total using `ingredient.price`; exposes `total` property
- **Pizza** (`pizza.py`): object structure — holds ingredients, iterates them on `accept()`

## Ingredient Prices

| Ingredient | Price |
|---|---|
| Cheese | $1.50 |
| Bacon | $2.00 |
| Pineapple | $0.80 |
| Mushroom | $1.20 |
| Seafood | $3.50 |
| **Full pizza** | **$9.00** |

## Structure

```
behavioral/visitor/
├── __init__.py
├── __main__.py                  ← demo: build pizza → price → cook
├── module_schema.txt
├── ingredient.py                ← Ingredient ABC (name, price, accept)
├── visitor.py                   ← Visitor ABC
├── pizza.py                     ← Pizza (object structure)
├── ingredients/
│   ├── __init__.py
│   ├── cheese.py
│   ├── bacon.py
│   ├── pineapple.py
│   ├── mushroom.py
│   └── seafood.py
├── visitors/
│   ├── __init__.py
│   ├── cook_visitor.py          ← CookVisitor
│   └── price_visitor.py         ← PriceVisitor
├── uml/
│   ├── visitor_general.puml     ← abstract pattern diagram
│   ├── visitor_schema.puml      ← structural class diagram
│   └── visitor_flow.puml        ← sequence diagram
└── tests/
    ├── __init__.py
    └── test_visitor.py
```

## Usage

### Run the demo:
```bash
python -m behavioral.visitor
```

### Run the tests:
```bash
python -m unittest behavioral.visitor.tests.test_visitor -v
```

## Key Components

### Double Dispatch
The core mechanic — two runtime type lookups resolve the correct method:

```python
# First dispatch — ingredient type determines which accept() runs
pizza.accept(visitor)
  → ingredient.accept(visitor)      # Cheese, Bacon, etc.

# Second dispatch — visitor type determines which visit_* runs
  → visitor.visit_cheese(self)      # CookVisitor or PriceVisitor
```

### Ingredient ABC (`ingredient.py`)
`name` and `price` are abstract properties — every ingredient carries its own data, visitors read it:

```python
class Ingredient(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def price(self) -> float: ...

    @abstractmethod
    def accept(self, visitor: Visitor) -> None: ...
```

### CookVisitor uses `ingredient.name`
```python
def visit_cheese(self, ingredient: Cheese) -> None:
    print(f"[Cook] {ingredient.name}: melting on the base.")
```

### PriceVisitor uses `ingredient.price`
```python
def visit_cheese(self, ingredient: Cheese) -> None:
    self._total += ingredient.price
```

## UML Diagrams

### Abstract pattern diagram
![visitor_general_uml.png](uml/visitor_general_uml.png)

### Structural diagram
See `uml/visitor_schema.puml`

### Sequence diagram
See `uml/visitor_flow.puml`

## Difference from Related Patterns

| Pattern | Intent |
|---------|--------|
| **Visitor** | Add new operations to a stable object structure. New visitors = easy; new element types = requires updating all visitors. |
| **Strategy** | Swap one algorithm at runtime on a single object. No object structure traversal. |
| **Iterator** | Traverse a collection. Controls how elements are visited, not what happens to them. |
| **Key trade-off** | Visitor favours adding operations freely. It makes adding new element types expensive — all existing visitors must be updated. |
