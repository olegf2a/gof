"""Japanese cuisine dish implementations"""

from ..dishes import Dessert, Drink, MainDish, SideDish


class Sushi(MainDish):
    """Traditional Japanese main dish"""

    def prepare(self) -> str:
        return "Preparing fresh sushi with salmon, tuna, and rice"

    def get_name(self) -> str:
        return "Assorted Sushi Platter"

    def get_calories(self) -> int:
        return 320


class Miso(SideDish):
    """Japanese side dish"""

    def prepare(self) -> str:
        return "Preparing warm miso soup with tofu and seaweed"

    def get_name(self) -> str:
        return "Miso Soup"

    def get_portion_size(self) -> str:
        return "Small bowl (150ml)"


class Mochi(Dessert):
    """Japanese dessert"""

    def prepare(self) -> str:
        return "Preparing soft mochi with sweet red bean filling"

    def get_name(self) -> str:
        return "Red Bean Mochi"

    def get_sweetness_level(self) -> str:
        return "Moderately sweet"


class GreenTea(Drink):
    """Japanese traditional drink"""

    def prepare(self) -> str:
        return "Brewing authentic matcha green tea"

    def get_name(self) -> str:
        return "Matcha Green Tea"

    def get_temperature(self) -> str:
        return "Hot (70°C)"
