import os

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

while True:
    name = input('Enter your name (or "off" to exit): ').capitalize().strip()
    
    if name == "Off":
        break

    elif name == "Add":
        new_name = input('Enter a name for the blacklist: ').capitalize().strip()
        blacklist.add(new_name)
      
        save_data(blacklist, DB_FILE)
        print(f'{new_name} added and saved.')
        continue

    elif name == "Del":
        rm_name = input('Who to remove: ').capitalize().strip()
        if rm_name in blacklist:
            blacklist.remove(rm_name)

            save_data(blacklist, DB_FILE)
            print(f'{rm_name} removed from the list and file.')
        else:
            print('This name is not on the list.')
        continue


    if name in blacklist:
        print('ACCESS DENIED!')
    else:
        print('Welcome, access granted.')