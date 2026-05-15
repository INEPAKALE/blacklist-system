# CLI Blacklist System

A simple Python command-line utility for managing a user blacklist with automated state persistence.

## Tech Stack
* **Language:** Python 3.10+
* **OS:** Linux (Ubuntu)
* **Modules:** `os` (Standard Library)

## Architecture & Features
* **State Persistence:** Data is preserved between restarts by checking the file system with `os.path.isfile` and deserializing strings using `.splitlines()`.
* **Auto-Save (Data Integrity):** Any change to the list (`Add`/`Del`) is immediately synced to the disk by overwriting the storage file.
* **DRY Principle:** File I/O operations are encapsulated within an isolated, reusable function.
* **Data Cleaning:** User input is automatically sanitized using `.strip()` to remove accidental whitespaces.

## How to Run in Linux

1. Clone the repository:
```bash
git clone https://github.com/INEPAKALE/blacklist-system.git
cd blacklist-system
```
2. Run the script:
```bash
python3 main.py
```