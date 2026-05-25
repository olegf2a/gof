"""Pizza class for Builder pattern implementation"""

from typing import List


class Pizza:
    """
    Pizza product class that represents a custom pizza with various toppings.

    This is the product being built by the PizzaBuilder.
    """

    def __init__(self) -> None:
        self.size: str = "medium"
        self.crust: str = "regular"
        self.toppings: List[str] = []

    def add_topping(self, topping: str) -> None:
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def set_size(self, size: str) -> None:
        """Set pizza size"""
        self.size = size

    def set_crust(self, crust: str) -> None:
        """Set pizza crust type"""
        self.crust = crust

    def get_description(self) -> str:
        """Get detailed description of the pizza"""
        if not self.toppings:
            return f"{self.size.capitalize()} {self.crust} crust pizza with no toppings (just cheese)"

        toppings_str = ", ".join(self.toppings)
        return f"{self.size.capitalize()} {self.crust} crust pizza with: {toppings_str}"

    def get_price(self) -> float:
        """Calculate pizza price based on size and toppings"""
        base_prices = {"small": 8.99, "medium": 12.99, "large": 16.99}
        base_price = base_prices.get(self.size, 12.99)

        # Each topping costs extra
        topping_price = len(self.toppings) * 1.50

        return base_price + topping_price

    def __str__(self) -> str:
        return self.get_description()

    def __repr__(self) -> str:
        return (
            f"Pizza(size='{self.size}', crust='{self.crust}', toppings={self.toppings})"
        )
