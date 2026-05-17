"""Ovens module - Creator classes"""

from .base import Oven
from .pizza_oven import PizzaOven
from .lasagna_oven import LasagnaOven
from .cookie_oven import CookieOven

__all__ = ['Oven', 'PizzaOven', 'LasagnaOven', 'CookieOven']