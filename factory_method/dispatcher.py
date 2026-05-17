"""Dispatcher function to get appropriate oven for dish type"""

from .ovens import PizzaOven, LasagnaOven, CookieOven

def get_oven(dish_type: str):
    """Factory function to get the appropriate oven for a dish type"""
    oven_map = {
        'pizza': PizzaOven,
        'lasagna': LasagnaOven,
        'cookies': CookieOven
    }

    dish_type = dish_type.lower()
    if dish_type not in oven_map:
        raise ValueError(f"Unknown dish type: {dish_type}")

    return oven_map[dish_type]()