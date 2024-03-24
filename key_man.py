from datetime import datetime
import rsa
import shutil
import os.path
import time

class Key_man:
    def __init__(self, keys_dir, backup_keys_dir):
        self.id_path = "{}/id.txt".format(keys_dir)
        self.public_key_path = "{}/public.pem".format(keys_dir)
        self.private_key_path = "{}/private.pem".format(keys_dir)

        self.id = ""
        self.public_key = ""
        self.private_key = ""

        self.keys_dir = keys_dir
        self.backup_keys_dir = backup_keys_dir

        self.local_ids = []
        self.matched_ids = []

        # If there is an empty or invalid key structure, backup and generate keys
        if (not os.path.exists(self.id_path) 
            or not os.path.exists(self.public_key_path) 
            or not os.path.exists(self.private_key_path)
            ):
            self.generate()
            time.sleep(1)
            self.backup()

    # Gets the information from all the keys and puts them in variables
    def get_keys(self):
        with open(self.id_path, "r") as f:
            self.id = f.read()

        with open(self.public_key_path, "r") as f:
            self.public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open(self.private_key_path, "r") as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())

    # Generates new keys
    def generate(self):
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)

        # Generates a ID based off the unix timestamp
        generated_id = str( int( (datetime.now() - datetime(1970, 1, 1)).total_seconds()) )

        with open(self.id_path, "w") as f:
            f.write(generated_id)
            f.close

        # Generates a private and public key
        generated_public_key, generated_private_key = rsa.newkeys(1024)

        with open(self.public_key_path, "wb") as f:
            f.write(generated_public_key.save_pkcs1("PEM"))
            f.close()

        with open(self.private_key_path, "wb") as f:
            f.write(generated_private_key.save_pkcs1("PEM"))
            f.close()

    # Copies keys to the backup key dir in a folder named by their ID
    def backup(self):
        self.get_keys()

        path = "{}/{}".format(self.backup_keys_dir, self.id)

        if not os.path.exists(path):
            os.makedirs(path)

        shutil.copy(self.id_path, "{}/id.txt".format(path))
        shutil.copy(self.public_key_path, "{}/public.pem".format(path))
        shutil.copy(self.private_key_path, "{}/private.pem".format(path))


    # Gets all local ids and stores them in a list
    def get_ids(self):
        self.local_ids = os.listdir(self.backup_keys_dir)
        self.local_ids.sort()

    # Print all passwords in the server matching the users local IDs
    def print_matched(self, server_ids):
        self.get_ids()
        self.get_keys()

        self.matched_ids = []

        print("Passwords stored in the server that you own: ")
        for id in server_ids:
            id_stripped = id.split("-", 1)[0]
            if id_stripped in self.local_ids:
                self.matched_ids.append(id)

                id_pass = id.split(".", 1)[0]
                print(id_pass)

        print("\nLocal IDs: ")
        pos = 1
        for id in self.local_ids:
            print("{}. {}".format(pos, id))
            pos += 1
                
        
    # Rolls the user back to a chosen backed up ID
    def rollback(self, server_ids):
        self.print_matched(server_ids)

        print("\nCurrent ID")
        print(self.id)

        rollback_option = int(input("ID to rollback to: "))-1
        rollback_id = self.local_ids[rollback_option]

        shutil.copy("{}/{}/public.pem".format(self.backup_keys_dir, rollback_id), "keys/public.pem")
        shutil.copy("{}/{}/private.pem".format(self.backup_keys_dir, rollback_id), "keys/private.pem")
        shutil.copy("{}/{}/id.txt".format(self.backup_keys_dir, rollback_id), "keys/id.txt")
        



