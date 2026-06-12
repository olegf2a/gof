# Memento Pattern

An implementation of the Memento design pattern for a text editor — the editor saves timestamped snapshots of its content, and a version history caretaker can restore any saved version by its version key without ever reading the snapshot's internal state.

![memento_general_uml.png](uml/memento_general_uml.png)

## Problem and Solution

### The Problem
Without the pattern, the client must hold all previous states itself and expose the editor's internals to do so:

```python
content = ""
history = {}

content = "First draft."
history["v1"] = content          # client copies the string manually

content = "Second draft."
history["v2"] = content

content = history["v1"]          # client reaches into raw state directly
```

### The Solution
The editor creates timestamped snapshots of itself on demand. The caretaker stores them by version key without inspecting their contents. The client picks a version key and restores — no raw state exposed:

```python
from behavioral.memento.text_editor import TextEditor
from behavioral.memento.caretaker import VersionHistory

editor = TextEditor()
history = VersionHistory()

editor.write("First draft.")
history.save(editor)

editor.write("Second draft.")
history.save(editor)

snapshots = history.history()
v1 = snapshots[0].get_version()   # "2026-06-12 10:00:00.000001"
v2 = snapshots[1].get_version()   # "2026-06-12 10:00:00.000042"

history.restore(editor, v1)
print(editor.content)   # → "First draft."

history.restore(editor, v2)
print(editor.content)   # → "Second draft."
```

## Pattern Overview

- **Memento** (`memento.py`): ABC — declares `get_state()` and provides `get_version()` (microsecond-precision timestamp set on construction)
- **TextSnapshot** (`text_snapshot.py`): concrete memento — stores the content string; calls `super().__init__()` to stamp the version key
- **Originator** (`originator.py`): ABC — declares `save() → Memento` and `restore(memento: Memento)`
- **TextEditor** (`text_editor.py`): concrete originator — holds `_content`, creates `TextSnapshot` on `save()`, reads it back on `restore()`
- **VersionHistory** (`caretaker.py`): caretaker — stores snapshots in a `dict[str, Memento]` keyed by version string, restores by key, never reads snapshot content

## Structure

```
behavioral/memento/
├── __init__.py
├── __main__.py              ← demo: write → save × 3 → restore by version key
├── module_schema.txt
├── memento.py               ← Memento ABC (get_state + get_version)
├── text_snapshot.py         ← TextSnapshot (concrete memento)
├── originator.py            ← Originator ABC
├── text_editor.py           ← TextEditor (concrete originator)
├── caretaker.py             ← VersionHistory (dict-based caretaker)
├── uml/
│   ├── memento_general.puml ← abstract pattern diagram
│   ├── memento_schema.puml  ← structural class diagram
│   └── memento_flow.puml    ← sequence diagram
└── tests/
    ├── __init__.py
    └── test_memento.py
```

## Usage

### Run the demo:
```bash
python -m behavioral.memento
```

### Run the tests:
```bash
python -m unittest behavioral.memento.tests.test_memento -v
```

## Key Components

### Memento (`memento.py`)
Version key is auto-generated with microsecond precision in `__init__` — no two snapshots collide even when saved in rapid succession:

```python
class Memento(ABC):
    def __init__(self) -> None:
        self._version: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def get_version(self) -> str:
        return self._version
```

### TextEditor (`text_editor.py`)
Creates and consumes snapshots. The caretaker is never involved in either:

```python
def save(self) -> TextSnapshot:
    return TextSnapshot(self._content)

def restore(self, memento: Memento) -> None:
    self._content = memento.get_state()
```

### VersionHistory (`caretaker.py`)
Stores snapshots by version key. Wraps `KeyError` as a descriptive `RuntimeError`:

```python
def save(self, editor: Originator) -> None:
    memento = editor.save()
    self._history[memento.get_version()] = memento

def restore(self, editor: Originator, version: str) -> None:
    try:
        editor.restore(self._history[version])
    except KeyError:
        raise RuntimeError(f"Version {version} does not exist")
```

## UML Diagrams

### Abstract pattern diagram
![memento_general_uml.png](uml/memento_general_uml.png)

### Structural diagram
See `uml/memento_schema.puml`

### Sequence diagram
See `uml/memento_flow.puml`

## Difference from Related Patterns

| Pattern | Intent |
|---------|--------|
| **Memento** | Snapshots the originator's **state** so it can be restored later. Caretaker stores snapshots but never reads them. Undo is "go back to this exact state." |
| **Command** | Encapsulates an **operation** so it can be executed and undone. Each command knows how to reverse itself — no full copy of state needed. |
| **Key distinction** | Memento saves **what it was**. Command saves **what was done and how to undo it**. |
| **When to use Memento** | When reversing an operation is impractical. Restore any arbitrary version directly by key. |
| **When to use Command** | When operations are well-defined and invertible. Undo walks history step-by-step; no full copies needed. |
| **Combined** | Command for step-by-step undo/redo + Memento for "save point" restore across many operations at once. |
