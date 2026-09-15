# Data Archivist: Digital Preservation in the Cyber Archives

> Preserve digital knowledge by mastering file operations, managing data streams, and building robust archival systems that protect information. *(Version 3.0)*

---

## 📁 Repository Structure
```text
ex0/
  └── ft_ancient_text.py
ex1/
  └── ft_archive_creation.py
ex2/
  └── ft_stream_management.py
ex3/
  └── ft_vault_security.py
```

# ⚙️ General Rules & Requirements

>  Python Version: Python 3.10 or later.

>  Linting: Must comply with flake8 linter standards.

>  Type Safety: All functions and methods must include type hints and pass mypy.

>  Error Handling: Graceful exception handling required to prevent crashes.

>  Context Manager Restriction: The with statement is only introduced and allowed starting from Exercise 3. Do not use it in exercises 0–2.

>  Allowed Types & Collections: str, int, float, list, dict, set, tuple (plus exercise-authorized modules/methods).

>  Submission: Submit your work to the assigned Git repository; only repository contents are evaluated.

# 🚀 Exercises Overview
## Exercise 0: Ancient Text Recovery (ex0/ft_ancient_text.py)

>  Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO, io.read(), io.close(), print()

>  Description: Recover an ancient text fragment from a file provided via CLI. Display contents like cat with custom headers/footers. Handle failure cases (nonexistent files, permission denied).

>  Run: python3 ft_ancient_text.py <file>

## Exercise 1: Archive Creation (ex1/ft_archive_creation.py)

>  Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO, io.read(), io.write(), io.close(), print(), input()

>  Description: Reuse Exercise 0 logic, append # (2087-compatible archive character) to the end of each line, display transformed content, prompt user for a destination file name (or empty to skip), and save/replace if specified.

>  Run: python3 ft_archive_creation.py <file>

## Exercise 2: Stream Management (ex2/ft_stream_management.py)

>  Authorized: import sys, sys.argv, sys.stdin, sys.stdout, sys.stderr, len(), open(), import typing, typing.IO, io.read(), io.readline(), io.write(), io.flush(), io.close(), print()

>  Description: Update Exercise 1 logic to route error messages from exceptions to sys.stderr with a [STDERR] prefix, and get user input via sys.stdin instead of the built-in input() function.

>  Run: python3 ft_stream_management.py <file>

## Exercise 3: Vault Security (ex3/ft_vault_security.py)

>  Authorized: open(), read(), write(), print() (along with the with statement)

>  Description: Implement secure_archive(filename, action, content) using the with statement context manager for safe read/write. Returns a tuple (bool, str) indicating success/failure and the content or error message.

>  Run: python3 ft_vault_security.py

# 🛠️ Verification & Quality Assurance
Bash

## Check code style compliance
flake8 .

## Check static type annotations
mypy .
