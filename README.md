# myproject

A short description of what this project does.

## Install

```bash
python -m venv .venv
source .venv/bin/activate    # on Windows: .venv\Scripts\activate
```

## Pre-commit hooks

This project uses [pre-commit](https://pre-commit.com/) to run Black, isort, mypy, and a few file-hygiene checks on every commit.

Install the git hook once after cloning:

```bash
pip install --upgrade pip
pip install pre-commit black isort mypy
pre-commit install
```

Run all hooks across the whole repo (useful the first time, or after pulling in new changes):

```bash
pre-commit run --all-files
```

To bypass the hooks in an emergency, add `--no-verify`. Use sparingly.
To update hook versions to their latest releases:

```bash
pre-commit autoupdate
```
