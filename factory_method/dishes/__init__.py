"""Dishes module - Product classes"""

from .base import Dish
from .pizza import Pizza
from .lasagna import Lasagna
from .cookies import Cookies

__all__ = ['Dish', 'Pizza', 'Lasagna', 'Cookies']