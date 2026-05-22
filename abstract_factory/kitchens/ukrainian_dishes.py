"""Ukrainian cuisine dish implementations"""

from ..dishes import MainDish, SideDish, Dessert, Drink

class Borscht(MainDish):
    """Traditional Ukrainian main dish"""

    def prepare(self) -> str:
        return "Cooking traditional borscht with beets, cabbage, and beef"

    def get_name(self) -> str:
        return "Ukrainian Borscht"

    def get_calories(self) -> int:
        return 180

class Varenyky(SideDish):
    """Ukrainian side dish"""

    def prepare(self) -> str:
        return "Making varenyky (dumplings) with potato and cheese filling"

    def get_name(self) -> str:
        return "Potato Varenyky"

    def get_portion_size(self) -> str:
        return "6 pieces"

class Syrniki(Dessert):
    """Ukrainian dessert"""

    def prepare(self) -> str:
        return "Pan-frying cottage cheese pancakes with sour cream"

    def get_name(self) -> str:
        return "Syrniki with Sour Cream"

    def get_sweetness_level(self) -> str:
        return "Mildly sweet"

class Kompot(Drink):
    """Traditional Ukrainian drink"""

    def prepare(self) -> str:
        return "Brewing fruit kompot with apples, pears, and berries"

    def get_name(self) -> str:
        return "Mixed Fruit Kompot"

    def get_temperature(self) -> str:
        return "Room temperature"