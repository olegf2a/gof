from .sort_strategy import SortStrategy


class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, items: list[int]) -> list[int]:
        return self._strategy.sort(items)
