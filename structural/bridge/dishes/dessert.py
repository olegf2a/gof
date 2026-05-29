from .base import Dish


class Dessert(Dish):
    def get_course_name(self) -> str:
        return "Dessert"

    def serve(self) -> str:
        return f"[{self._cuisine.get_name()}] {self._cuisine.prepare_dessert()}"
