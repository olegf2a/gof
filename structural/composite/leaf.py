from typing import List

from .tree_element import TreeElement


class Leaf(TreeElement):
    """A class for a Leaf."""

    def __init__(self, value: int):
        self._value = value

    def get_children(self) -> List[TreeElement]:
        return []

    def increment(self) -> int:
        self._value += 1
        return self._value

    def decrement(self) -> int:
        self._value -= 1
        return self._value

    def get_value(self) -> int:
        return self._value
