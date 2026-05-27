# Blacklist CLI Utility

## Description
A command-line utility designed for efficient blacklist management. Implemented in Python, it utilizes hash sets to ensure $O(1)$ average time complexity for lookups.

## Usage
The utility interacts directly with the Ubuntu file system.
- `python3 main.py --add <name>` — Add an element to the set.
- `python3 main.py --check <name>` — Check for entry existence (exit code 0: Allowed, 1: Denied).
- `python3 main.py --remove <name>` — Remove an element from the set.

## Technical Specifications
- **Algorithmic Complexity:** Lookup operations are performed using `set` data structures, ensuring $O(1)$ efficiency.
- **Interface:** Declarative argument parsing implemented via `argparse`.
- **Persistence:** Data is persisted via synchronized writes to a `.txt` file.