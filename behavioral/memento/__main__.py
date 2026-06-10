from .caretaker import VersionHistory
from .text_editor import TextEditor


def demo() -> None:
    print("=== Memento Pattern — Text Editor Versions ===\n")

    editor = TextEditor()
    history = VersionHistory()

    print("--- Writing and saving versions ---")
    editor.write("First draft: introduction only.")
    history.save(editor)
    print(f"  v1 saved: {editor.content!r}")

    editor.write("Second draft: added body paragraphs.")
    history.save(editor)
    print(f"  v2 saved: {editor.content!r}")

    editor.write("Third draft: conclusion added, ready for review.")
    history.save(editor)
    print(f"  v3 saved: {editor.content!r}")

    print(f"\n--- Saved history ({len(history.history())} versions) ---")
    for i, snap in enumerate(history.history()):
        print(f"  [{i}] {snap.get_content()!r}")

    print("\n--- Restore to version 0 ---")
    history.restore(editor, 0)
    print(f"  current: {editor.content!r}")

    print("\n--- Restore to version 1 ---")
    history.restore(editor, 1)
    print(f"  current: {editor.content!r}")

    print("\n--- Restore to last version (-1) ---")
    history.restore(editor, -1)
    print(f"  current: {editor.content!r}")

    print("\n--- Restore to invalid version ---")
    try:
        history.restore(editor, 99)
    except RuntimeError as e:
        print(f"  RuntimeError: {e}")


if __name__ == "__main__":
    demo()
