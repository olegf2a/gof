from unittest import TestCase
from unittest import main as unittest_main
from unittest.mock import MagicMock

from ..sort_strategy import SortStrategy
from ..sorter import Sorter
from ..strategies.bubble_sort import BubbleSortStrategy
from ..strategies.quick_sort import QuickSortStrategy


class TestBubbleSortStrategy(TestCase):
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


class TestQuickSortStrategy(TestCase):
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


class TestSorter(TestCase):
    def setUp(self) -> None:
        self.data = [64, 34, 25, 12, 22, 11, 90]
        self.expected = [11, 12, 22, 25, 34, 64, 90]

    def test_sort(self) -> None:
        mock_strategy = MagicMock(spec=SortStrategy)
        mock_strategy.sort.return_value = self.expected

        sorter = Sorter(mock_strategy)
        result = sorter.sort(self.data)

        mock_strategy.sort.assert_called_once_with(self.data)
        self.assertEqual(result, self.expected)

    def test_set_strategy_swaps_at_runtime(self) -> None:
        mock_strategy_1 = MagicMock(spec=SortStrategy)
        mock_strategy_1.sort.return_value = self.expected
        mock_strategy_2 = MagicMock(spec=SortStrategy)
        mock_strategy_2.sort.return_value = self.expected

        sorter = Sorter(mock_strategy_1)
        sorter.sort(self.data)
        mock_strategy_1.sort.assert_called_once_with(self.data)

        sorter.set_strategy(mock_strategy_2)
        sorter.sort(self.data)
        mock_strategy_2.sort.assert_called_once_with(self.data)
        mock_strategy_1.sort.assert_called_once()


if __name__ == "__main__":
    unittest_main()
