"""Oven Factory - Factory Method Pattern Implementation"""

from .dishes import Cookies, Dish, Lasagna, Pizza
from .oven import Oven

__all__ = [
    "Dish",
    "Pizza",
    "Lasagna",
    "Cookies",
    "Oven",
]
