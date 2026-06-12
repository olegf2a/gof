from .caretaker import VersionHistory
from .text_editor import TextEditor


def demo() -> None:
    print("=== Memento Pattern — Text Editor Versions ===\n")

    editor = TextEditor()
    history = VersionHistory()

    print("--- Writing and saving versions ---")
    editor.write("First draft: introduction only.")
    history.save(editor)
    print(f"  saved: {editor.content!r}")

    editor.write("Second draft: added body paragraphs.")
    history.save(editor)
    print(f"  saved: {editor.content!r}")

    editor.write("Third draft: conclusion added, ready for review.")
    history.save(editor)
    print(f"  saved: {editor.content!r}")

    snapshots = history.history()
    print(f"\n--- Saved history ({len(snapshots)} versions) ---")
    for snap in snapshots:
        print(f"  [{snap.get_version()}]  {snap.get_state()!r}")

    v1, v2, v3 = (snap.get_version() for snap in snapshots)

    print(f"\n--- Restore to v1 ---")
    history.restore(editor, v1)
    print(f"  current: {editor.content!r}")

    print(f"\n--- Restore to v2 ---")
    history.restore(editor, v2)
    print(f"  current: {editor.content!r}")

    print(f"\n--- Restore to v3 ---")
    history.restore(editor, v3)
    print(f"  current: {editor.content!r}")

    print("\n--- Restore to unknown version ---")
    try:
        history.restore(editor, "2000-01-01 00:00:00.000000")
    except RuntimeError as e:
        print(f"  RuntimeError: {e}")


if __name__ == "__main__":
    demo()
