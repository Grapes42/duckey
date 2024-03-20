from server import Server
from key_man import Key_man

server = Server("ilovemyholly.ddns.net", "pass_man", "6arleyhuman")
key_man = Key_man("keys", "backup_keys")

options = """0. Exit
1. Get password
2. Add password
3. Generate new ID and keys
4. Rollback to previous ID
5. Merge IDs"""

while True:
    print(options)
    option = int(input("Enter option: "))

    # Exit
    if option == 0:
        exit()

    # Get password
    elif option == 1:
        key_man.get_keys()
        server.get_pass(key_man.id, key_man.private_key)

    # Add password
    elif option == 2:
        key_man.get_keys()
        server.add_pass(key_man.id, key_man.public_key)

    # Generate new keys
    elif option == 3:
        key_man.generate()
        key_man.backup()

    # Rollback to ID
    elif option == 4:
        server.get_ids()
        key_man.rollback(server.ids)

    print("\n\n")