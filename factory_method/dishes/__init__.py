"""Dishes module - Product classes"""

from .base import Dish
from .cookies import Cookies
from .lasagna import Lasagna
from .pizza import Pizza

__all__ = ["Dish", "Pizza", "Lasagna", "Cookies"]
