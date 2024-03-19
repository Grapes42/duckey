import rsa
from datetime import datetime
import os.path
import shutil

def generate_keys():
    public_key, private_key = rsa.newkeys(1024)

    with open("keys/public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("keys/private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

    id = str( int( (datetime.now() - datetime(1970, 1, 1)).total_seconds()) )

    with open("keys/user_id.txt", "w") as f:
        f.write(id)

def backup_keys():
    with open("keys/user_id.txt", "r") as f:
        user_id = f.read()

    path = "backup_keys/{}".format(user_id)

    if not os.path.exists(path):
        os.makedirs(path)

        shutil.move("keys/public.pem", "{}/public.pem".format(path))
        shutil.move("keys/private.pem", "{}/private.pem".format(path))
        shutil.move("keys/user_id.txt", "{}/user_id.txt".format(path))





# Gets information about current key structure
if os.path.isfile("keys/public.pem") and os.path.isfile("keys/private.pem") and os.path.isfile("keys/user_id.txt"):
    is_keys = True
    valid_structure = True

elif os.path.isfile("keys/public.pem") or os.path.isfile("keys/private.pem") or os.path.isfile("keys/user_id.txt"):
    is_keys = True
    valid_structure = False

else:
    is_keys = False
    valid_structure = False




# If there are no keys generated, generate some then exit the program
if is_keys == False:
    generate_keys()
    print("No keys were found, generated keys")
    exit()

# If the key structure is invalid add a message stating so after option 1 below
if valid_structure == False:
    suffix = "(current keys structure is invalid)"
else:
    suffix = ""


print("""1. Generate new keys {}
2. Rollback to previous keys""".format(suffix))

option = int(input("Enter option: "))

# Generate backup keys and generate new keys
if option == 1:
    if valid_structure:
        backup_keys()
    generate_keys()

# Backup current keys and rollback to chosen keys
elif option == 2:
    if valid_structure == False:
        print("Current key structure must be correct before rolling back!")
        exit()

    ids = os.listdir("backup_keys")
    ids.sort()

    backup_keys()

    pos = 1
    for id in ids:
        print("{}. {}".format(pos, id))
        pos += 1

    rollback_option = int(input("ID to rollback to: "))-1
    rollback_id = ids[rollback_option]

    shutil.copyfile("backup_keys/{}/public.pem".format(rollback_id), "keys/public.pem")
    shutil.copyfile("backup_keys/{}/private.pem".format(rollback_id), "keys/private.pem")
    shutil.copyfile("backup_keys/{}/user_id.txt".format(rollback_id), "keys/user_id.txt")



