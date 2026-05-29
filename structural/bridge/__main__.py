from typing import List

from .cuisine import Cuisine, Italian, Japanese, Ukrainian
from .dishes import Dessert, Dish, FirstCourse, SecondCourse, ThirdCourse


def serve_meal(cuisine: Cuisine) -> None:
    print(f"\n=== {cuisine.get_name()} Menu ===")
    for dish in [
        FirstCourse(cuisine),
        SecondCourse(cuisine),
        ThirdCourse(cuisine),
        Dessert(cuisine),
    ]:
        print(f"  {dish.get_course_name()}: {dish.serve()}")


def bridge_demo(cuisines: List[Cuisine]) -> None:
    """Show that the same dish type works with any cuisine."""
    print(f"\n--- Serving only Second Course across cuisines ---")
    for c in cuisines:
        dish = SecondCourse(c)
        print(f"  {dish.serve()}")


def main() -> None:
    cuisines: List[Cuisine] = [Italian(), Japanese(), Ukrainian()]

    print("*** Full menus ***")
    for cuisine in cuisines:
        serve_meal(cuisine)

    print("\n*** Bridge demo: swap cuisine, same dish class ***")
    bridge_demo(cuisines)


if __name__ == "__main__":
    main()
