from .base import Dish


class SecondCourse(Dish):
    def get_course_name(self) -> str:
        return "Second Course"

    def serve(self) -> str:
        return f"[{self._cuisine.get_name()}] {self._cuisine.prepare_second()}"
