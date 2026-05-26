"""Unit tests for Pizza and PizzaBuilder classes"""

import unittest

from ..pizza import Pizza
from ..pizza_builder import PizzaBuilder


class TestPizza(unittest.TestCase):
    """Test cases for Pizza class"""

    def setUp(self) -> None:
        """Set up test fixtures before each test method"""
        self.pizza = Pizza()

    def test_pizza_initialization(self) -> None:
        """Test pizza initialization with default values"""
        self.assertEqual(self.pizza.size, "medium")
        self.assertEqual(self.pizza.crust, "regular")
        self.assertEqual(self.pizza.toppings, [])

    def test_add_topping(self) -> None:
        """Test adding toppings to pizza"""
        self.pizza.add_topping("pepperoni")
        self.assertIn("pepperoni", self.pizza.toppings)
        self.assertEqual(len(self.pizza.toppings), 1)

    def test_add_duplicate_topping(self) -> None:
        """Test that duplicate toppings are not added"""
        self.pizza.add_topping("cheese")
        self.pizza.add_topping("cheese")
        self.assertEqual(len(self.pizza.toppings), 1)
        self.assertEqual(self.pizza.toppings.count("cheese"), 1)

    def test_set_size(self) -> None:
        """Test setting pizza size"""
        self.pizza.set_size("large")
        self.assertEqual(self.pizza.size, "large")

    def test_set_crust(self) -> None:
        """Test setting pizza crust"""
        self.pizza.set_crust("thin")
        self.assertEqual(self.pizza.crust, "thin")

    def test_get_description_no_toppings(self) -> None:
        """Test description for pizza with no toppings"""
        description = self.pizza.get_description()
        expected = "Medium regular crust pizza with no toppings (just cheese)"
        self.assertEqual(description, expected)

    def test_get_description_with_toppings(self) -> None:
        """Test description for pizza with toppings"""
        self.pizza.add_topping("pepperoni")
        self.pizza.add_topping("mushrooms")
        description = self.pizza.get_description()
        expected = "Medium regular crust pizza with: pepperoni, mushrooms"
        self.assertEqual(description, expected)

    def test_get_price_base(self) -> None:
        """Test base price calculation for different sizes"""
        # Small pizza
        self.pizza.set_size("small")
        self.assertEqual(self.pizza.get_price(), 8.99)

        # Medium pizza
        self.pizza.set_size("medium")
        self.assertEqual(self.pizza.get_price(), 12.99)

        # Large pizza
        self.pizza.set_size("large")
        self.assertEqual(self.pizza.get_price(), 16.99)

    def test_get_price_with_toppings(self) -> None:
        """Test price calculation with toppings"""
        self.pizza.set_size("medium")  # Base: $12.99
        self.pizza.add_topping("pepperoni")  # +$1.50
        self.pizza.add_topping("cheese")  # +$1.50
        expected_price = 12.99 + (2 * 1.50)  # $15.99
        self.assertEqual(self.pizza.get_price(), expected_price)

    def test_get_price_invalid_size(self) -> None:
        """Test price calculation with invalid size defaults to medium"""
        self.pizza.set_size("invalid")
        self.assertEqual(self.pizza.get_price(), 12.99)  # Should default to medium

    def test_str_method(self) -> None:
        """Test __str__ method"""
        self.pizza.add_topping("cheese")
        str_output = str(self.pizza)
        expected = "Medium regular crust pizza with: cheese"
        self.assertEqual(str_output, expected)

    def test_repr_method(self) -> None:
        """Test __repr__ method"""
        self.pizza.add_topping("cheese")
        repr_output = repr(self.pizza)
        expected = "Pizza(size='medium', crust='regular', toppings=['cheese'])"
        self.assertEqual(repr_output, expected)


class TestPizzaBuilder(unittest.TestCase):
    """Test cases for PizzaBuilder class"""

    def setUp(self) -> None:
        """Set up test fixtures before each test method"""
        self.builder = PizzaBuilder()

    def test_builder_initialization(self) -> None:
        """Test builder initialization"""
        self.assertIsNotNone(self.builder._pizza)
        self.assertIsInstance(self.builder._pizza, Pizza)

    def test_reset(self) -> None:
        """Test builder reset functionality"""
        # Add some configuration
        self.builder.set_size("large").add_bacon()
        old_pizza = self.builder._pizza

        # Reset builder
        result = self.builder.reset()

        # Check that reset returns self and creates new pizza
        self.assertIs(result, self.builder)
        self.assertIsNot(self.builder._pizza, old_pizza)
        self.assertIsNotNone(self.builder._pizza)
        assert self.builder._pizza is not None  # Type guard for mypy
        self.assertEqual(self.builder._pizza.size, "medium")
        self.assertEqual(len(self.builder._pizza.toppings), 0)

    def test_set_size_chaining(self) -> None:
        """Test set_size method and chaining"""
        result = self.builder.set_size("large")
        self.assertIs(result, self.builder)  # Should return self for chaining
        assert self.builder._pizza is not None
        self.assertEqual(self.builder._pizza.size, "large")

    def test_set_crust_chaining(self) -> None:
        """Test set_crust method and chaining"""
        result = self.builder.set_crust("thin")
        self.assertIs(result, self.builder)  # Should return self for chaining
        self.assertIsNotNone(self.builder._pizza)
        self.assertEqual(self.builder._pizza.crust, "thin")

    def test_add_cheese(self) -> None:
        """Test add_cheese method"""
        result = self.builder.add_cheese("mozzarella")
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("mozzarella cheese", self.builder._pizza.toppings)

    def test_add_cheese_default(self) -> None:
        """Test add_cheese with default parameter"""
        self.builder.add_cheese()
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("mozzarella cheese", self.builder._pizza.toppings)

    def test_add_bacon(self) -> None:
        """Test add_bacon method"""
        result = self.builder.add_bacon()
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("bacon", self.builder._pizza.toppings)

    def test_add_pineapple(self) -> None:
        """Test add_pineapple method"""
        result = self.builder.add_pineapple()
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("pineapple", self.builder._pizza.toppings)

    def test_add_mushrooms(self) -> None:
        """Test add_mushrooms method"""
        result = self.builder.add_mushrooms("shiitake")
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("shiitake", self.builder._pizza.toppings)

    def test_add_mushrooms_default(self) -> None:
        """Test add_mushrooms with default parameter"""
        self.builder.add_mushrooms()
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("button mushrooms", self.builder._pizza.toppings)

    def test_add_seafood(self) -> None:
        """Test add_seafood method"""
        result = self.builder.add_seafood("salmon")
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("salmon", self.builder._pizza.toppings)

    def test_add_seafood_default(self) -> None:
        """Test add_seafood with default parameter"""
        self.builder.add_seafood()
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("shrimp", self.builder._pizza.toppings)

    def test_add_pepperoni(self) -> None:
        """Test add_pepperoni method"""
        result = self.builder.add_pepperoni()
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("pepperoni", self.builder._pizza.toppings)

    def test_add_vegetables(self) -> None:
        """Test add_vegetables method"""
        result = self.builder.add_vegetables("tomatoes")
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("tomatoes", self.builder._pizza.toppings)

    def test_add_custom_topping(self) -> None:
        """Test add_custom_topping method"""
        result = self.builder.add_custom_topping("olives")
        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertIn("olives", self.builder._pizza.toppings)

    def test_method_chaining(self) -> None:
        """Test that all methods can be chained together"""
        result = (
            self.builder.set_size("large")
            .set_crust("thin")
            .add_cheese("cheddar")
            .add_bacon()
            .add_pineapple()
            .add_mushrooms("portobello")
            .add_seafood("shrimp")
        )

        self.assertIs(result, self.builder)
        self.assertIsNotNone(self.builder._pizza)
        self.assertEqual(self.builder._pizza.size, "large")
        self.assertEqual(self.builder._pizza.crust, "thin")
        expected_toppings = [
            "cheddar cheese",
            "bacon",
            "pineapple",
            "portobello",
            "shrimp",
        ]
        for topping in expected_toppings:
            self.assertIn(topping, self.builder._pizza.toppings)

    def test_build_method(self) -> None:
        """Test build method returns pizza and resets builder"""
        # Configure pizza
        self.builder.set_size("large").add_bacon().add_cheese("mozzarella")

        # Build pizza
        pizza = self.builder.build()

        # Check returned pizza
        self.assertIsInstance(pizza, Pizza)
        self.assertEqual(pizza.size, "large")
        self.assertIn("bacon", pizza.toppings)
        self.assertIn("mozzarella cheese", pizza.toppings)

        # Check builder was reset
        self.assertIsNotNone(self.builder._pizza)
        self.assertEqual(self.builder._pizza.size, "medium")  # Default after reset
        self.assertEqual(
            len(self.builder._pizza.toppings), 0
        )  # No toppings after reset

    def test_get_current_pizza_info(self) -> None:
        """Test get_current_pizza_info method"""
        self.builder.set_size("large").add_bacon()
        info = self.builder.get_current_pizza_info()
        expected = "Large regular crust pizza with: bacon"
        self.assertEqual(info, expected)

    def test_builder_reuse(self) -> None:
        """Test that builder can be reused to create multiple pizzas"""
        # Build first pizza
        pizza1 = self.builder.set_size("small").add_cheese("mozzarella").build()

        # Build second pizza
        pizza2 = self.builder.set_size("large").add_bacon().add_pineapple().build()

        # Check that pizzas are different instances with different configurations
        self.assertIsNot(pizza1, pizza2)
        self.assertEqual(pizza1.size, "small")
        self.assertEqual(pizza2.size, "large")
        self.assertIn("mozzarella cheese", pizza1.toppings)
        self.assertNotIn("bacon", pizza1.toppings)
        self.assertIn("bacon", pizza2.toppings)
        self.assertNotIn("mozzarella cheese", pizza2.toppings)

    def test_complex_pizza_creation(self) -> None:
        """Test creating a complex pizza with multiple toppings"""
        pizza = (
            self.builder.set_size("large")
            .set_crust("thick")
            .add_cheese("parmesan")
            .add_cheese("mozzarella")
            .add_bacon()
            .add_pepperoni()
            .add_mushrooms("portobello")
            .add_vegetables("bell peppers")
            .add_vegetables("onions")
            .add_seafood("shrimp")
            .add_custom_topping("olives")
            .build()
        )

        self.assertEqual(pizza.size, "large")
        self.assertEqual(pizza.crust, "thick")

        # Should have multiple toppings
        self.assertGreaterEqual(len(pizza.toppings), 8)

        # Check some specific toppings
        self.assertIn("parmesan cheese", pizza.toppings)
        self.assertIn("bacon", pizza.toppings)
        self.assertIn("shrimp", pizza.toppings)
        self.assertIn("olives", pizza.toppings)

        # Check price calculation
        expected_price = 16.99 + (len(pizza.toppings) * 1.50)
        self.assertEqual(pizza.get_price(), expected_price)


class TestIntegration(unittest.TestCase):
    """Integration tests for Pizza and PizzaBuilder working together"""

    def test_hawaiian_pizza_creation(self) -> None:
        """Test creating a Hawaiian pizza (bacon and pineapple)"""
        builder = PizzaBuilder()
        hawaiian = (
            builder.set_size("large")
            .set_crust("thin")
            .add_cheese("mozzarella")
            .add_bacon()
            .add_pineapple()
            .build()
        )

        self.assertEqual(hawaiian.size, "large")
        self.assertEqual(hawaiian.crust, "thin")
        self.assertIn("mozzarella cheese", hawaiian.toppings)
        self.assertIn("bacon", hawaiian.toppings)
        self.assertIn("pineapple", hawaiian.toppings)

        # Check description
        description = hawaiian.get_description()
        self.assertIn("Large thin crust pizza with:", description)
        self.assertIn("bacon", description)
        self.assertIn("pineapple", description)

    def test_vegetarian_pizza_creation(self) -> None:
        """Test creating a vegetarian pizza"""
        builder = PizzaBuilder()
        veggie = (
            builder.set_size("medium")
            .add_cheese("goat cheese")
            .add_mushrooms("portobello")
            .add_vegetables("tomatoes")
            .add_vegetables("spinach")
            .build()
        )

        self.assertEqual(veggie.size, "medium")
        self.assertIn("goat cheese cheese", veggie.toppings)
        self.assertIn("portobello", veggie.toppings)
        self.assertIn("tomatoes", veggie.toppings)
        self.assertIn("spinach", veggie.toppings)

    def test_seafood_pizza_creation(self) -> None:
        """Test creating a seafood pizza"""
        builder = PizzaBuilder()
        seafood = (
            builder.set_size("large")
            .add_seafood("shrimp")
            .add_seafood("mussels")
            .add_mushrooms("shiitake")
            .add_cheese("parmesan")
            .build()
        )

        self.assertEqual(seafood.size, "large")
        self.assertIn("shrimp", seafood.toppings)
        self.assertIn("mussels", seafood.toppings)
        self.assertIn("shiitake", seafood.toppings)
        self.assertIn("parmesan cheese", seafood.toppings)


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)
