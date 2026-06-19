# Blacklist CLI Utility

## Description
A command-line utility for efficient system blacklist management. Implemented in Python, it leverages hash-maps (dictionaries) to ensure $O(1)$ average time complexity for identity lookups.

## Usage
The utility interacts with the local storage via JSON-backed state.

* **Check Access:**
  `python3 main.py --check <name>`
  *Exit codes:* `0` - Allowed (Access Granted), `1` - Denied (Blocked).

* **Modify Blacklist:**
  `python3 main.py --add <name> [--reason <reason>]` - Adds user with an optional block description.
  `python3 main.py --remove <name>` - Removes user and clears their metadata.

## Technical Specifications
* **Data Structure:** Python `dict` backing, ensuring $O(1)$ search bottlenecks.
* **CLI Interface:** Declarative argument parsing via `argparse`.
* **Persistence Layer:** Full state serialization to a `.json` file using standard I/O blocks.