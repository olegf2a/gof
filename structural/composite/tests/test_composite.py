"""Unit tests for Composite pattern — Integer Tree"""

import unittest

from ..leaf import Leaf
from ..node import Node
from ..tree_element import TreeElement


class TestLeaf(unittest.TestCase):

    def setUp(self) -> None:
        self.leaf = Leaf(5)

    def test_get_value(self) -> None:
        self.assertEqual(self.leaf.get_value(), 5)

    def test_increment(self) -> None:
        self.leaf.increment()
        self.assertEqual(self.leaf.get_value(), 6)

    def test_decrement(self) -> None:
        self.leaf.decrement()
        self.assertEqual(self.leaf.get_value(), 4)

    def test_multiple_increments(self) -> None:
        for _ in range(3):
            self.leaf.increment()
        self.assertEqual(self.leaf.get_value(), 8)

    def test_get_children_returns_empty(self) -> None:
        self.assertEqual(self.leaf.get_children(), [])

    def test_implements_interface(self) -> None:
        self.assertIsInstance(self.leaf, TreeElement)


class TestNode(unittest.TestCase):

    def setUp(self) -> None:
        self.leaf1 = Leaf(1)
        self.leaf2 = Leaf(2)
        self.node = Node(0, [self.leaf1, self.leaf2])

    def test_get_value_sums_children(self) -> None:
        self.assertEqual(self.node.get_value(), 3)

    def test_get_children(self) -> None:
        self.assertEqual(self.node.get_children(), [self.leaf1, self.leaf2])

    def test_increment_propagates_to_children(self) -> None:
        self.node.increment()
        self.assertEqual(self.leaf1.get_value(), 2)
        self.assertEqual(self.leaf2.get_value(), 3)

    def test_decrement_propagates_to_children(self) -> None:
        self.node.decrement()
        self.assertEqual(self.leaf1.get_value(), 0)
        self.assertEqual(self.leaf2.get_value(), 1)

    def test_implements_interface(self) -> None:
        self.assertIsInstance(self.node, TreeElement)

    def test_empty_node(self) -> None:
        node = Node(0)
        self.assertEqual(node.get_value(), 0)
        self.assertEqual(node.get_children(), [])


class TestCompositeTree(unittest.TestCase):

    def setUp(self) -> None:
        self.leaf1 = Leaf(1)
        self.leaf2 = Leaf(2)
        self.leaf3 = Leaf(3)
        self.node_a = Node(0, [self.leaf1, self.leaf2])
        self.node_b = Node(0, [self.leaf3])
        self.root = Node(0, [self.node_a, self.node_b])

    def test_initial_total(self) -> None:
        self.assertEqual(self.root.get_value(), 6)

    def test_root_increment_affects_all(self) -> None:
        self.root.increment()
        self.assertEqual(self.leaf1.get_value(), 2)
        self.assertEqual(self.leaf2.get_value(), 3)
        self.assertEqual(self.leaf3.get_value(), 4)

    def test_subtree_increment_does_not_affect_siblings(self) -> None:
        self.node_a.increment()
        self.assertEqual(self.leaf1.get_value(), 2)
        self.assertEqual(self.leaf2.get_value(), 3)
        self.assertEqual(self.leaf3.get_value(), 3)  # unchanged

    def test_root_decrement_affects_all(self) -> None:
        self.root.decrement()
        self.assertEqual(self.leaf1.get_value(), 0)
        self.assertEqual(self.leaf2.get_value(), 1)
        self.assertEqual(self.leaf3.get_value(), 2)

    def test_get_value_after_operations(self) -> None:
        self.root.increment()  # all +1: node vals 1 each, leaves 2,3,4 → total 12
        self.node_a.decrement()  # node_a and its leaves -1: back to 0,1,2 → total 9
        self.assertEqual(self.root.get_value(), 9)


if __name__ == "__main__":
    unittest.main()
