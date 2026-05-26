"""PizzaBuilder class implementing Builder pattern"""

from typing import Optional

from .pizza import Pizza


class PizzaBuilder:
    """
    Builder class for creating custom pizzas.

    The builder has the build() method inside the class itself,
    allowing for method chaining and step-by-step pizza construction.
    """

    def __init__(self) -> None:
        self._pizza: Pizza = Pizza()
        self.reset()

    def reset(self) -> "PizzaBuilder":
        """Reset builder to create a new pizza"""
        self._pizza = Pizza()
        return self

    # Size and crust methods
    def set_size(self, size: str) -> "PizzaBuilder":
        """Set pizza size (small, medium, large)"""
        if self._pizza:
            self._pizza.set_size(size)
        return self

    def set_crust(self, crust: str) -> "PizzaBuilder":
        """Set pizza crust type (thin, regular, thick)"""
        if self._pizza:
            self._pizza.set_crust(crust)
        return self

    # Topping methods (according to the task requirements)
    def add_cheese(self, cheese_type: str = "mozzarella") -> "PizzaBuilder":
        """Add cheese topping"""
        if self._pizza:
            self._pizza.add_topping(f"{cheese_type} cheese")
        return self

    def add_bacon(self) -> "PizzaBuilder":
        """Add bacon topping"""
        if self._pizza:
            self._pizza.add_topping("bacon")
        return self

    def add_pineapple(self) -> "PizzaBuilder":
        """Add pineapple topping"""
        if self._pizza:
            self._pizza.add_topping("pineapple")
        return self

    def add_mushrooms(self, mushroom_type: str = "button mushrooms") -> "PizzaBuilder":
        """Add mushrooms topping"""
        if self._pizza:
            self._pizza.add_topping(mushroom_type)
        return self

    def add_seafood(self, seafood_type: str = "shrimp") -> "PizzaBuilder":
        """Add seafood topping"""
        if self._pizza:
            self._pizza.add_topping(seafood_type)
        return self

    # Additional popular toppings
    def add_pepperoni(self) -> "PizzaBuilder":
        """Add pepperoni"""
        if self._pizza:
            self._pizza.add_topping("pepperoni")
        return self

    def add_vegetables(self, vegetable: str) -> "PizzaBuilder":
        """Add vegetables (bell peppers, onions, tomatoes, etc.)"""
        if self._pizza:
            self._pizza.add_topping(vegetable)
        return self

    def add_custom_topping(self, topping: str) -> "PizzaBuilder":
        """Add any custom topping"""
        if self._pizza:
            self._pizza.add_topping(topping)
        return self

    def build(self) -> Pizza:
        """
        Build and return the final pizza.

        This is the build method that exists within the builder class itself,
        as requested in the task description.
        """
        if self._pizza is None:
            raise ValueError("Cannot build pizza: builder has not been initialized")

        # Get the final pizza
        result = self._pizza

        # Reset for next pizza (optional)
        self.reset()

        return result

    def get_current_pizza_info(self) -> str:
        """Get information about the pizza being built (for preview)"""
        if self._pizza:
            return self._pizza.get_description()
        return "No pizza is being built"
