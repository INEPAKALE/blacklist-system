import os, argparse

DB_FILE = "blacklist.txt"


def save_data(data_list, filename):
        with open(filename, "w", encoding='utf-8') as file:
            for person in data_list:
                file.write(person + "\n")
if os.path.isfile(DB_FILE):
    with open(DB_FILE, "r", encoding='utf-8') as file:
        blacklist = set(file.read().splitlines())
else:
    blacklist = set()
    print("Database file not found, new list created.")

parser = argparse.ArgumentParser(description="CLI blacklist-system")
#Add username to list
parser.add_argument("--add", type=str, help="Add username to list")
#Checking a Name in a List
parser.add_argument("--check", type=str, help="Check for the presence of a name")
#Removing a user from the list
parser.add_argument("--remove", type=str, help="Removing a user from the list")
args = parser.parse_args()

if args.add:
    new_name = args.add.capitalize().strip()
    blacklist.add(new_name)
    save_data(blacklist, DB_FILE)
    print(f'{new_name} added and saved.')
elif args.check:
    name_to_check = args.check.capitalize().strip()
    print(blacklist)
    if name_to_check in blacklist:
        print('ACCESS DENIED!')
    else:
        print('Welcome, access granted.')
elif args.remove:
    rm_name = args.remove.capitalize().strip()
    if rm_name in blacklist:
        blacklist.remove(rm_name)
        save_data(blacklist, DB_FILE)
        print(f'{rm_name} removed from the list and file.')
    else:
        print('This name is not on the list.')