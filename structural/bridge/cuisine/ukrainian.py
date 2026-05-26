from .base import Cuisine


class Ukrainian(Cuisine):
    def get_name(self) -> str:
        return "Ukrainian"

    def prepare_first(self) -> str:
        return "Borscht"

    def prepare_second(self) -> str:
        return "Chicken Kyiv"

    def prepare_third(self) -> str:
        return "Varenyky"

    def prepare_dessert(self) -> str:
        return "Syrniki"
