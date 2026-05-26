from .base import Dish


class ThirdCourse(Dish):
    def get_course_name(self) -> str:
        return "Third Course"

    def serve(self) -> str:
        return f"[{self._cuisine.get_name()}] {self._cuisine.prepare_third()}"
