from .sorter import Sorter
from .strategies.bubble_sort import BubbleSortStrategy
from .strategies.quick_sort import QuickSortStrategy


def demo() -> None:
    print("=== Strategy Pattern — List Sorter ===\n")

    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original:  {data}\n")

    sorter = Sorter(BubbleSortStrategy())

    print("--- Bubble Sort ---")
    result = sorter.sort(data)
    print(f"  sorted:   {result}")
    print(f"  original: {data}  (unchanged)\n")

    sorter.set_strategy(QuickSortStrategy())

    print("--- Quick Sort (strategy swapped at runtime) ---")
    result = sorter.sort(data)
    print(f"  sorted:   {result}")
    print(f"  original: {data}  (unchanged)\n")

    print("--- Edge cases ---")
    for case, label in [
        ([], "empty list"),
        ([42], "single element"),
        ([3, 3, 3], "all equal"),
        ([5, 4, 3, 2, 1], "reverse sorted"),
        ([1, 2, 3, 4, 5], "already sorted"),
    ]:
        sorter.set_strategy(BubbleSortStrategy())
        bubble = sorter.sort(case)
        sorter.set_strategy(QuickSortStrategy())
        quick = sorter.sort(case)
        match = "✓" if bubble == quick else "✗"
        print(f"  {label:<16} bubble={bubble}  quick={quick}  {match}")


if __name__ == "__main__":
    demo()
