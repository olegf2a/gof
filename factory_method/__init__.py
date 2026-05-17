"""Oven Factory - Factory Method Pattern Implementation"""

from .dispatcher import get_oven
from .dishes import Dish, Pizza, Lasagna, Cookies
from .ovens import Oven, PizzaOven, LasagnaOven, CookieOven

__all__ = [
    'get_oven',
    'Dish', 'Pizza', 'Lasagna', 'Cookies',
    'Oven', 'PizzaOven', 'LasagnaOven', 'CookieOven'
]