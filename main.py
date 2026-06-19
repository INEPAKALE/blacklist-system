import os
import argparse
import json

DB_FILE = "blacklist.json"


def save_data(data_list, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def load_blacklist(filepath):
    if not os.path.isfile(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            blacklist = json.load(file)
            return blacklist
    except PermissionError:
        return {}
    except json.JSONDecodeError:
        return {}


def main():
    blacklist = load_blacklist(DB_FILE)

    parser = argparse.ArgumentParser(description="CLI blacklist-system")
    parser.add_argument("--add", type=str, help="Add username to list")
    parser.add_argument("--check", type=str,
                        help="Check for the presence of a name")
    parser.add_argument("--remove", type=str,
                        help="Removing a user from the list")
    parser.add_argument("--reason", type=str, help="reason for the block")
    args = parser.parse_args()

    if args.add:
        if args.reason:
            reason = args.reason.strip()
        else:
            reason = "reason not specified"

        current_date = "2026-06-18"

        new_name = args.add.capitalize().strip()
        blacklist[new_name] = {
            "reason": reason,
            "blocked_at": current_date
        }
  
        save_data(blacklist, DB_FILE)
        
    elif args.check:
        name = args.check.capitalize().strip()
        if name in blacklist:
            user_data = blacklist[name]
            reason = user_data.get("reason", "reason not specified")
            blocked_at = user_data.get("blocked_at", "unknown date")
            print(f"ACCESS DENIED! Reason: {reason}, Date: {blocked_at}")
            exit(1)
        else:
            print("Welcome, access granted")
            exit(0)
    elif args.remove:
        rm_name = args.remove.capitalize().strip()
        if rm_name in blacklist:
            del blacklist[rm_name]
            save_data(blacklist, DB_FILE)
            print(f"{rm_name} removed from the list and file.")
        else:
            print("This name is not on the list.")


if __name__ == "__main__":
    main()