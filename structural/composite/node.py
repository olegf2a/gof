from typing import List

from .tree_element import TreeElement


class Node(TreeElement):
    """A class for a Node."""

    def __init__(self, value: int, children: List[TreeElement] | None = None) -> None:
        self._value = value
        self._children: List[TreeElement] = children if children else []

    def get_value(self) -> int:
        resul = self._value
        for child in self._children:
            resul += child.get_value()
        return resul

    def increment(self) -> int:
        self._value += 1
        for child in self.get_children():
            child.increment()

        return self._value

    def decrement(self) -> int:
        self._value -= 1
        for child in self.get_children():
            child.decrement()
        return self._value

    def get_children(self) -> List[TreeElement]:
        return self._children
