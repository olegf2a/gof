# GRASP Principles

**GRASP** (General Responsibility Assignment Software Patterns) is a set of nine fundamental principles for assigning responsibilities to classes and objects in object-oriented design. Coined by Craig Larman in *Applying UML and Patterns*, GRASP focuses on *why* responsibilities are assigned the way they are, not just *how* code is structured.

## Table of Contents

1. [Information Expert](#1-information-expert)
2. [Creator](#2-creator)
3. [Controller](#3-controller)
4. [Low Coupling](#4-low-coupling)
5. [High Cohesion](#5-high-cohesion)
6. [Polymorphism](#6-polymorphism)
7. [Pure Fabrication](#7-pure-fabrication)
8. [Indirection](#8-indirection)
9. [Protected Variations](#9-protected-variations)
10. [How the Principles Relate](#how-the-principles-relate)
11. [Further Reading](#further-reading)

---

## 1. Information Expert

**Principle:** Assign a responsibility to the class that has the information needed to fulfill it.

**Why:** Keeps behavior close to the data it operates on, reducing the need to expose internal state and improving encapsulation.

### Example

A `ShoppingCart` knows about its items, so it should be responsible for calculating the total — not some external service.

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float

@dataclass
class CartItem:
    product: Product
    quantity: int

    def subtotal(self) -> float:
        # CartItem is the expert on its own subtotal
        return self.product.price * self.quantity

@dataclass
class ShoppingCart:
    items: list[CartItem] = field(default_factory=list)

    def total(self) -> float:
        # ShoppingCart is the expert on its items, so it computes the total
        return sum(item.subtotal() for item in self.items)


cart = ShoppingCart(items=[
    CartItem(Product("Book", 20.0), 2),
    CartItem(Product("Pen", 3.5), 4),
])
print(cart.total())  # 54.0
```

**Anti-pattern:** A `CheckoutService` reaching into `cart.items` and calculating the total externally — that scatters logic and breaks encapsulation.

---

## 2. Creator

**Principle:** Assign class B the responsibility to create instances of class A when one or more of the following is true:
- B contains or aggregates A
- B records A
- B closely uses A
- B has the initializing data for A

**Why:** Encourages cohesive object creation and avoids spreading instantiation logic across the system.

### Example

An `Order` aggregates `OrderLine`s, so the `Order` should create them.

```python
from dataclasses import dataclass, field

@dataclass
class OrderLine:
    product_name: str
    quantity: int
    unit_price: float

@dataclass
class Order:
    lines: list[OrderLine] = field(default_factory=list)

    def add_line(self, product_name: str, quantity: int, unit_price: float) -> OrderLine:
        # Order is the natural creator of OrderLine: it aggregates them
        line = OrderLine(product_name, quantity, unit_price)
        self.lines.append(line)
        return line


order = Order()
order.add_line("Notebook", 3, 5.99)
order.add_line("Pencil", 10, 0.50)
print(order.lines)
```

---

## 3. Controller

**Principle:** Assign the responsibility of handling a system event to a class representing the overall system, a use case, or a session.

**Why:** Decouples the UI/interface layer from domain logic. The controller orchestrates; it doesn't do the work itself.

### Example

A web request or CLI command shouldn't talk directly to entities — a controller mediates.

```python
class OrderRepository:
    def save(self, order): ...
    def find(self, order_id): ...

class PaymentGateway:
    def charge(self, amount: float, token: str) -> bool: ...

class PlaceOrderController:
    """Handles the 'place order' use case."""

    def __init__(self, orders: OrderRepository, payments: PaymentGateway):
        self.orders = orders
        self.payments = payments

    def handle(self, order, payment_token: str) -> dict:
        if self.payments.charge(order.total(), payment_token):
            self.orders.save(order)
            return {"status": "ok", "order_id": order.id}
        return {"status": "payment_failed"}
```

The controller doesn't compute totals or persist data itself — it delegates and coordinates.

---

## 4. Low Coupling

**Principle:** Assign responsibilities so that coupling between classes remains low. Classes should depend on abstractions or as few other classes as possible.

**Why:** Lower coupling makes the system easier to change, test, and reuse.

### Example

Inject dependencies rather than hard-coding them.

```python
from typing import Protocol

class Notifier(Protocol):
    def send(self, message: str) -> None: ...

class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotifier:
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

class OrderService:
    # Depends on the Notifier protocol, not a concrete class
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def confirm(self, order_id: str) -> None:
        self.notifier.send(f"Order {order_id} confirmed")


# Easy to swap implementations — that's the win
service = OrderService(EmailNotifier())
service.confirm("A-100")

service = OrderService(SMSNotifier())
service.confirm("A-100")
```

---

## 5. High Cohesion

**Principle:** Keep each class focused on a single, well-defined purpose. Its methods and data should be closely related.

**Why:** Cohesive classes are easier to understand, maintain, and reuse. Low-cohesion ("god") classes become brittle.

### Example

Split a class that does too much.

```python
# Low cohesion — does persistence, validation, and reporting
class BadUser:
    def __init__(self, name, email): ...
    def save_to_db(self): ...
    def validate_email(self): ...
    def export_to_pdf(self): ...
    def send_welcome_email(self): ...


# High cohesion — each class has one clear job
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str

class UserValidator:
    def is_valid_email(self, user: User) -> bool:
        return "@" in user.email

class UserRepository:
    def save(self, user: User) -> None: ...

class UserReporter:
    def export_pdf(self, user: User) -> bytes: ...
```

---

## 6. Polymorphism

**Principle:** When behavior varies by type, use polymorphic operations instead of conditional logic (`if/elif` chains on type).

**Why:** Adding new types becomes a matter of adding a class, not modifying existing code (Open/Closed Principle).

### Example

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width, self.height = width, height
    def area(self) -> float:
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base, self.height = base, height
    def area(self) -> float:
        return 0.5 * self.base * self.height


shapes: list[Shape] = [Circle(3), Rectangle(2, 4), Triangle(5, 6)]
total = sum(s.area() for s in shapes)  # No if/elif on type!
print(total)
```

**Anti-pattern:** `if isinstance(shape, Circle): ... elif isinstance(shape, Rectangle): ...` — every new shape forces edits to every consumer.

---

## 7. Pure Fabrication

**Principle:** When no existing domain class is a good fit for a responsibility, invent a class that doesn't represent a real-world concept but improves cohesion and lowers coupling.

**Why:** Sometimes the cleanest design needs helper classes (repositories, services, mappers) that don't map to the problem domain.

### Example

Persistence doesn't belong on the domain entity — fabricate a `Repository`.

```python
from dataclasses import dataclass
import sqlite3

@dataclass
class Customer:
    id: int
    name: str
    email: str
    # Notice: no save(), no load() — domain stays clean

class CustomerRepository:
    """Pure fabrication: not a domain concept, but earns its keep."""

    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection

    def save(self, customer: Customer) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO customers VALUES (?, ?, ?)",
            (customer.id, customer.name, customer.email),
        )
        self.conn.commit()

    def find(self, customer_id: int) -> Customer | None:
        row = self.conn.execute(
            "SELECT id, name, email FROM customers WHERE id = ?",
            (customer_id,),
        ).fetchone()
        return Customer(*row) if row else None
```

---

## 8. Indirection

**Principle:** Assign the responsibility of mediating between two components to an intermediate object, so they don't directly depend on each other.

**Why:** Reduces coupling and lets you change one side without breaking the other. Repositories, adapters, and facades all apply this idea.

### Example

A domain service shouldn't know whether weather data comes from an HTTP API, a file, or a cache. An adapter sits in between.

```python
from typing import Protocol

class WeatherSource(Protocol):
    def temperature(self, city: str) -> float: ...

class OpenWeatherAdapter:
    """Indirection layer: hides HTTP details from the rest of the app."""
    def __init__(self, api_key: str):
        self.api_key = api_key

    def temperature(self, city: str) -> float:
        # imagine: requests.get(...).json()["main"]["temp"]
        return 21.5

class CachedWeatherAdapter:
    def __init__(self, source: WeatherSource):
        self.source = source
        self.cache: dict[str, float] = {}

    def temperature(self, city: str) -> float:
        if city not in self.cache:
            self.cache[city] = self.source.temperature(city)
        return self.cache[city]

class TripPlanner:
    def __init__(self, weather: WeatherSource):
        self.weather = weather  # doesn't care which adapter

    def recommend(self, city: str) -> str:
        t = self.weather.temperature(city)
        return "Pack shorts" if t > 20 else "Pack a jacket"


planner = TripPlanner(CachedWeatherAdapter(OpenWeatherAdapter("key")))
print(planner.recommend("Wrocław"))
```

---

## 9. Protected Variations

**Principle:** Identify points of predicted variation or instability, and create stable interfaces around them so changes don't ripple through the system.

**Why:** Insulates the system from foreseeable change. Closely related to the Open/Closed Principle and is the *goal* behind several other GRASP principles (Polymorphism, Indirection).

### Example

Tax rules vary by country and change over time. Protect the rest of the system with a stable interface.

```python
from typing import Protocol

class TaxStrategy(Protocol):
    def calculate(self, amount: float) -> float: ...

class PolandVAT:
    def calculate(self, amount: float) -> float:
        return amount * 0.23

class GermanyVAT:
    def calculate(self, amount: float) -> float:
        return amount * 0.19

class USNoVAT:
    def calculate(self, amount: float) -> float:
        return 0.0

class Invoice:
    def __init__(self, subtotal: float, tax: TaxStrategy):
        self.subtotal = subtotal
        self.tax = tax

    def total(self) -> float:
        return self.subtotal + self.tax.calculate(self.subtotal)


# A new country, a new VAT rate, a tax holiday — none of it touches Invoice.
print(Invoice(100.0, PolandVAT()).total())   # 123.0
print(Invoice(100.0, GermanyVAT()).total())  # 119.0
print(Invoice(100.0, USNoVAT()).total())     # 100.0
```

---

## How the Principles Relate

GRASP principles work together, not in isolation:

- **Low Coupling** and **High Cohesion** are evaluative — every other principle is judged partly by whether it helps these two.
- **Polymorphism**, **Indirection**, and **Pure Fabrication** are tactics that often serve **Protected Variations**.
- **Information Expert** and **Creator** guide where responsibilities naturally belong before you reach for more advanced patterns.

A good rule of thumb: start with **Information Expert** and **Creator**, watch for **High Cohesion** and **Low Coupling** as you go, and reach for **Polymorphism**, **Indirection**, or **Pure Fabrication** when the simple assignment doesn't hold up.

---

## Further Reading

- Craig Larman, *Applying UML and Patterns* (3rd ed.) — the canonical source for GRASP.
- Robert C. Martin, *Clean Architecture* — complementary perspective on dependency direction.
- *Design Patterns* (Gang of Four) — many GoF patterns are concrete realizations of GRASP principles.