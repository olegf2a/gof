"""Cookie oven implementation - Concrete Creator"""

from .base import Oven
from ..dishes import Cookies

class CookieOven(Oven):
    """Concrete creator for cookie dishes"""

    def create_dish(self) -> Cookies:
        """Factory method implementation - creates Cookies"""
        return Cookies()