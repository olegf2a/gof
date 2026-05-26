from .base import Cuisine


class Japanese(Cuisine):
    def get_name(self) -> str:
        return "Japanese"

    def prepare_first(self) -> str:
        return "Miso soup"

    def prepare_second(self) -> str:
        return "Salmon Ramen"

    def prepare_third(self) -> str:
        return "Gyoza"

    def prepare_dessert(self) -> str:
        return "Mochi"
