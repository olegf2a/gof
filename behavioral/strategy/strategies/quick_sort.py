from ..sort_strategy import SortStrategy


class QuickSortStrategy(SortStrategy):
    def sort(self, items: list[int]) -> list[int]:
        result = items.copy()
        self._quicksort(result, 0, len(result) - 1)
        return result

    def _quicksort(self, items: list[int], low: int, high: int) -> None:
        def _partition(items: list[int], low: int, high: int) -> int:
            pivot = items[high]
            i = low - 1
            for j in range(low, high):
                if items[j] <= pivot:
                    i += 1
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]
            return i + 1

        if low < high:
            pivot_index = _partition(items, low, high)
            self._quicksort(items, low, pivot_index - 1)
            self._quicksort(items, pivot_index + 1, high)
