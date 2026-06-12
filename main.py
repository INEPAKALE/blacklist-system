import os
import argparse


def check_user(username):
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            blacklist = set(file.read().splitlines())
            if username in blacklist:
                print("ACCESS DENIED!")
                exit(1)
            else:
                print("Welcome, access granted.")
                exit(0)
    except FileNotFoundError:
        print("The database is empty.")
        print("welcome")
        exit(0)
    except PermissionError:
        print("No access rights")
        exit(1)


DB_FILE = "blacklist.txt"


def save_data(data_list, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for person in data_list:
            file.write(person + "\n")  


def main():
    if os.path.isfile(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as file:
            blacklist = set(file.read().splitlines())
    else:
        blacklist = set()
        print("Database file not found, new list created.")

    parser = argparse.ArgumentParser(description="CLI blacklist-system")
    parser.add_argument("--add", type=str, help="Add username to list")
    parser.add_argument("--check", type=str, help="Check for the presence of a name")
    parser.add_argument("--remove", type=str, help="Removing a user from the list")
    args = parser.parse_args()

    if args.add:
        new_name = args.add.capitalize().strip()
        blacklist.add(new_name)
        save_data(blacklist, DB_FILE)
        print(f"{new_name} added and saved.")
    elif args.check:
        name_to_check = args.check.capitalize().strip()
        print(blacklist)
        if name_to_check in blacklist:
            print("ACCESS DENIED!")
    else:
        print("Welcome, access granted.")
    if args.remove:
        rm_name = args.remove.capitalize().strip()
        if rm_name in blacklist:
            blacklist.remove(rm_name)
            save_data(blacklist, DB_FILE)
            print(f"{rm_name} removed from the list and file.")
        else:
            print("This name is not on the list.")


if __name__ == "__main__":
    main()