from .leaf import Leaf
from .node import Node
from .tree_element import TreeElement


def print_tree(element: TreeElement, indent: int = 0) -> None:
    prefix = "  " * indent
    name = type(element).__name__
    print(f"{prefix}{name}(value={element.get_value()})")
    for child in element.get_children():
        print_tree(child, indent + 1)


def main() -> None:
    leaf1, leaf2, leaf3 = Leaf(1), Leaf(2), Leaf(3)
    node_a = Node(0, [leaf1, leaf2])
    node_b = Node(0, [leaf3])
    root = Node(0, [node_a, node_b])

    print("=== Initial tree ===")
    print_tree(root)

    root.increment()
    print("\n=== After root.increment() ===")
    print_tree(root)
    print(f"Total: {root.get_value()}")

    node_a.decrement()
    print("\n=== After node_a.decrement() ===")
    print_tree(root)
    print(f"Total: {root.get_value()}")


if __name__ == "__main__":
    main()
