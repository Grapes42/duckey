import rsa
from datetime import datetime
import os.path
import shutil

class RSA_man:

    def __init__(self):
        self.update_keys()

    def update_keys(self):
        if os.path.exists("keys/id.txt"):
            with open("keys/id.txt", "r") as f:
                self.id = f.read()

        if os.path.exists("keys/id.txt"):
            with open("keys/public.pem", "rb") as f:
                self.public_key = rsa.PublicKey.load_pkcs1(f.read())

        if os.path.exists("keys/id.txt"):
            with open("keys/private.pem", "rb") as f:
                self.private_key = rsa.PrivateKey.load_pkcs1(f.read())

    def generate_keys():

        id = str( int( (datetime.now() - datetime(1970, 1, 1)).total_seconds()) )

        with open("keys/id.txt", "w") as f:
            f.write(id)

        public_key, private_key = rsa.newkeys(1024)

        with open("keys/public.pem", "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))

        with open("keys/private.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

    def backup_keys(self):
        self.update_keys()

        path = "backup_keys/{}".format(self.id)

        if not os.path.exists(path):
            os.makedirs(path)

            shutil.copy("keys/public.pem", "{}/public.pem".format(path))
            shutil.copy("keys/private.pem", "{}/private.pem".format(path))
            shutil.copy("keys/id.txt", "{}/id.txt".format(path))

    def get_user_ids():
        # Gets and sorts a list of all of the user's IDs
        user_ids = os.listdir("backup_keys")
        user_ids.sort()
        return user_ids
    
    
    def print_user_ids(self):
        # Prints all ids as an options list
        print("IDs stored locally:")
        pos = 1

        user_ids = self.get_user_ids()

        for id in user_ids:
            print("{}. {}".format(pos, id))
            pos += 1
        print("")

    def rollback(self, matched_passes):
        user_ids = self.get_user_ids()

        print("\nPasswords stored in the server that you own:")
        for id in matched_passes: print(id)

        print("")
        self.print_user_ids()

        rollback_option = int(input("ID to rollback to: "))-1
        rollback_id = user_ids[rollback_option]

        shutil.copy("backup_keys/{}/public.pem".format(rollback_id), "keys/public.pem")
        shutil.copy("backup_keys/{}/private.pem".format(rollback_id), "keys/private.pem")
        shutil.copy("backup_keys/{}/id.txt".format(rollback_id), "keys/id.txt")

    #def merge_id():

    #def merge_all():


