# Testing Guide for Design Patterns

This guide explains how the abstract testing system works and how to add tests for new design patterns.

## Abstract Test System

The project uses an **abstract test discovery system** that automatically finds and runs tests for all design patterns without needing to manually configure each pattern in the CI pipeline.

### How It Works

1. **Simple Discovery**: The pipeline checks each directory for a `tests/` subdirectory
2. **Standardized Structure**: All tests must be in `pattern_name/tests/test_*.py`
3. **Future-Proof**: New patterns automatically get tested when they follow the structure
4. **Zero Configuration**: No pipeline changes needed for new patterns

## Test Structure Requirements

For tests to be automatically discovered and run, follow this simple structure:

```
pattern_name/
├── __init__.py              # Pattern module
├── pattern_implementation.py
├── tests/                   # Tests directory (required)
│   ├── __init__.py         # Tests package (required)
│   └── test_*.py           # Test files starting with "test_"
└── README.md
```

### Example Structures

#### ✅ Correct Structure (Builder Pattern):
```
builder/
├── __init__.py
├── pizza.py
├── pizza_builder.py
├── tests/
│   ├── __init__.py
│   └── test_pizza_builder.py  ← Auto-discovered ✅
└── README.md
```

#### ❌ Incorrect Structures:
```
# Missing tests directory
pattern/
├── test_pattern.py          ← Not discovered ❌
└── pattern.py

# Wrong test location
pattern/
├── pattern.py
└── test/                    ← Should be "tests" ❌
    └── test_pattern.py

# Wrong test naming
pattern/
├── pattern.py
└── tests/
    └── pattern_test.py      ← Should start with "test_" ❌
```

## Adding Tests for New Patterns

### Step 1: Create Test Directory Structure
```bash
mkdir -p new_pattern/tests
touch new_pattern/tests/__init__.py
```

### Step 2: Create Test File
Create `new_pattern/tests/test_new_pattern.py`:

```python
"""Unit tests for new pattern implementation"""

import unittest
from ..new_pattern_class import NewPatternClass


class TestNewPattern(unittest.TestCase):
    """Test cases for new pattern"""

    def setUp(self):
        """Set up test fixtures"""
        self.instance = NewPatternClass()

    def test_basic_functionality(self):
        """Test basic pattern functionality"""
        # Your tests here
        self.assertIsNotNone(self.instance)

    # Add more test methods...


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

### Step 3: Push and Verify
Once pushed, the GitLab CI will automatically:
1. Discover your test module
2. Run your tests
3. Report results in the pipeline

## Running Tests

### CI Pipeline

The pipeline runs automatically on:
- Merge requests
- Pushes to main branch

## Test Best Practices

### 1. Comprehensive Coverage
```python
class TestPattern(unittest.TestCase):
    def test_initialization(self):
        """Test object creation"""

    def test_core_functionality(self):
        """Test main pattern behavior"""

    def test_edge_cases(self):
        """Test boundary conditions"""

    def test_error_handling(self):
        """Test error conditions"""

    def test_integration(self):
        """Test pattern working with other components"""
```

### 2. Clear Test Names
```python
# ✅ Good
def test_builder_returns_self_for_method_chaining(self):

# ❌ Bad
def test_builder(self):
```

### 3. Setup and Teardown
```python
def setUp(self):
    """Set up test fixtures before each test"""
    self.pattern = PatternClass()

def tearDown(self):
    """Clean up after each test"""
    # Cleanup code if needed
```

### 4. Test Categories
Group tests logically:
- `TestPatternCore` - Core functionality
- `TestPatternEdgeCases` - Edge cases and error conditions
- `TestPatternIntegration` - Integration with other components

## Test Requirements

- Test all public methods and core functionality
- Test error conditions and edge cases
- Include integration tests where applicable
- Follow unittest best practices

## Current Patterns with Tests

| Pattern | Test File | Test Count | Status |
|---------|-----------|------------|--------|
| Builder | `builder/tests/test_pizza_builder.py` | 37 tests | ✅ Active |

## Future Patterns

When you add a new pattern, it will automatically be included in the test suite if it follows the structure guidelines above. No pipeline configuration changes needed!

## Troubleshooting

### Tests Not Discovered
Check that your structure matches exactly:
```
pattern_name/tests/test_*.py
```

### Import Errors
Make sure you have `__init__.py` files:
```
pattern_name/
├── __init__.py
└── tests/
    ├── __init__.py
    └── test_*.py
```

### Relative Import Issues
Use relative imports in test files:
```python
from ..module_name import ClassName  # ✅ Good
from module_name import ClassName    # ❌ May fail
```
