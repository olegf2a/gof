"""Unit tests for Bridge pattern — Cafe dishes and cuisines"""

import unittest

from ..cuisine import Cuisine, Italian, Japanese, Ukrainian
from ..dishes import Dessert, Dish, FirstCourse, SecondCourse, ThirdCourse


class TestCuisines(unittest.TestCase):

    def setUp(self) -> None:
        self.cuisines = [Italian(), Japanese(), Ukrainian()]

    def test_all_cuisines_implement_interface(self) -> None:
        for cuisine in self.cuisines:
            self.assertIsInstance(cuisine, Cuisine)

    def test_all_cuisines_have_name(self) -> None:
        names = [c.get_name() for c in self.cuisines]
        self.assertEqual(names, ["Italian", "Japanese", "Ukrainian"])

    def test_all_cuisines_implement_all_courses(self) -> None:
        for cuisine in self.cuisines:
            self.assertIsInstance(cuisine.prepare_first(), str)
            self.assertIsInstance(cuisine.prepare_second(), str)
            self.assertIsInstance(cuisine.prepare_third(), str)
            self.assertIsInstance(cuisine.prepare_dessert(), str)

    def test_cuisine_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            Cuisine()  # type: ignore


class TestDishes(unittest.TestCase):

    def setUp(self) -> None:
        self.italian = Italian()

    def test_all_dishes_implement_interface(self) -> None:
        for dish in [
            FirstCourse(self.italian),
            SecondCourse(self.italian),
            ThirdCourse(self.italian),
            Dessert(self.italian),
        ]:
            self.assertIsInstance(dish, Dish)

    def test_dish_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            Dish(self.italian)  # type: ignore

    def test_course_names(self) -> None:
        expected = ["First Course", "Second Course", "Third Course", "Dessert"]
        dishes = [
            FirstCourse(self.italian),
            SecondCourse(self.italian),
            ThirdCourse(self.italian),
            Dessert(self.italian),
        ]
        self.assertEqual([d.get_course_name() for d in dishes], expected)

    def test_serve_contains_cuisine_name(self) -> None:
        for dish in [
            FirstCourse(self.italian),
            SecondCourse(self.italian),
            ThirdCourse(self.italian),
            Dessert(self.italian),
        ]:
            self.assertIn("Italian", dish.serve())


class TestBridge(unittest.TestCase):
    """Verify abstraction and implementation vary independently."""

    def test_same_dish_with_different_cuisines(self) -> None:
        results = [
            SecondCourse(c).serve() for c in [Italian(), Japanese(), Ukrainian()]
        ]
        self.assertIn("Spaghetti Carbonara", results[0])
        self.assertIn("Salmon Ramen", results[1])
        self.assertIn("Chicken Kyiv", results[2])

    def test_all_dishes_with_same_cuisine(self) -> None:
        ukrainian = Ukrainian()
        dishes = [
            FirstCourse(ukrainian),
            SecondCourse(ukrainian),
            ThirdCourse(ukrainian),
            Dessert(ukrainian),
        ]
        served = [d.serve() for d in dishes]
        self.assertIn("Borscht", served[0])
        self.assertIn("Chicken Kyiv", served[1])
        self.assertIn("Varenyky", served[2])
        self.assertIn("Syrniki", served[3])

    def test_swap_cuisine_changes_output(self) -> None:
        dish_italian = FirstCourse(Italian())
        dish_japanese = FirstCourse(Japanese())
        self.assertNotEqual(dish_italian.serve(), dish_japanese.serve())
        self.assertIn("Minestrone", dish_italian.serve())
        self.assertIn("Miso", dish_japanese.serve())


if __name__ == "__main__":
    unittest.main()
