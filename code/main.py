from server import Server
from key_man import Key_man
from string_operations import get_part

server = Server("duckey.ddns.net", "duckey", "quack")
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

    print("\n")

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

    # Merge IDs
    elif option == 5:
        server.get_ids()
        key_man.print_matched(server.ids)

        print("\nCurrent ID")
        print(key_man.id)

        option = int(input("\n\n1. Merge specific ID\n2. Merge all IDs\nEnter option: "))

        if option == 1:
            id_to_merge = key_man.local_ids[  (int(input("Enter ID to merge: ")))-1  ]

            for id in server.ids:
                if id_to_merge in id:
                    print(id)
                    server.get(id)

                    name = get_part()
                    print(name)

                    password = server.decrypt(id, key_man.private_key)

                    path = "{}-{}".format(key_man.id, name)
                    server.encrypt(key_man.id, )

                    server.put(path)


    print("\n\n")