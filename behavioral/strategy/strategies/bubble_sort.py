from ..sort_strategy import SortStrategy


class BubbleSortStrategy(SortStrategy):
    def sort(self, items: list[int]) -> list[int]:
        result = items.copy()
        n = len(result)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break
        return result
