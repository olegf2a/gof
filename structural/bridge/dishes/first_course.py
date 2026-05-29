from .base import Dish


class FirstCourse(Dish):
    def get_course_name(self) -> str:
        return "First Course"

    def serve(self) -> str:
        return f"[{self._cuisine.get_name()}] {self._cuisine.prepare_first()}"
