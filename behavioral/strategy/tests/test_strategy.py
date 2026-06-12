import unittest

from ..sorter import Sorter
from ..strategies.bubble_sort import BubbleSortStrategy
from ..strategies.quick_sort import QuickSortStrategy


class TestBubbleSortStrategy(unittest.TestCase):
    def setUp(self) -> None:
        self.strategy = BubbleSortStrategy()

    def test_sorts_unsorted_list(self) -> None:
        self.assertEqual(self.strategy.sort([3, 1, 2]), [1, 2, 3])

    def test_sorts_reverse_list(self) -> None:
        self.assertEqual(self.strategy.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_already_sorted(self) -> None:
        self.assertEqual(self.strategy.sort([1, 2, 3]), [1, 2, 3])

    def test_single_element(self) -> None:
        self.assertEqual(self.strategy.sort([42]), [42])

    def test_empty_list(self) -> None:
        self.assertEqual(self.strategy.sort([]), [])

    def test_duplicates(self) -> None:
        self.assertEqual(self.strategy.sort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])

    def test_does_not_mutate_original(self) -> None:
        data = [3, 1, 2]
        self.strategy.sort(data)
        self.assertEqual(data, [3, 1, 2])


class TestQuickSortStrategy(unittest.TestCase):
    def setUp(self) -> None:
        self.strategy = QuickSortStrategy()

    def test_sorts_unsorted_list(self) -> None:
        self.assertEqual(self.strategy.sort([3, 1, 2]), [1, 2, 3])

    def test_sorts_reverse_list(self) -> None:
        self.assertEqual(self.strategy.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_already_sorted(self) -> None:
        self.assertEqual(self.strategy.sort([1, 2, 3]), [1, 2, 3])

    def test_single_element(self) -> None:
        self.assertEqual(self.strategy.sort([42]), [42])

    def test_empty_list(self) -> None:
        self.assertEqual(self.strategy.sort([]), [])

    def test_duplicates(self) -> None:
        self.assertEqual(self.strategy.sort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])

    def test_does_not_mutate_original(self) -> None:
        data = [3, 1, 2]
        self.strategy.sort(data)
        self.assertEqual(data, [3, 1, 2])


class TestSorter(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [64, 34, 25, 12, 22, 11, 90]
        self.expected = [11, 12, 22, 25, 34, 64, 90]

    def test_sorts_with_bubble(self) -> None:
        sorter = Sorter(BubbleSortStrategy())
        self.assertEqual(sorter.sort(self.data), self.expected)

    def test_sorts_with_quick(self) -> None:
        sorter = Sorter(QuickSortStrategy())
        self.assertEqual(sorter.sort(self.data), self.expected)

    def test_set_strategy_swaps_at_runtime(self) -> None:
        sorter = Sorter(BubbleSortStrategy())
        self.assertEqual(sorter.sort(self.data), self.expected)
        sorter.set_strategy(QuickSortStrategy())
        self.assertEqual(sorter.sort(self.data), self.expected)

    def test_both_strategies_produce_same_result(self) -> None:
        bubble = Sorter(BubbleSortStrategy()).sort(self.data)
        quick = Sorter(QuickSortStrategy()).sort(self.data)
        self.assertEqual(bubble, quick)

    def test_does_not_mutate_original(self) -> None:
        original = self.data.copy()
        Sorter(BubbleSortStrategy()).sort(self.data)
        Sorter(QuickSortStrategy()).sort(self.data)
        self.assertEqual(self.data, original)


if __name__ == "__main__":
    unittest.main()
