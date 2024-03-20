import rsa
import pysftp
import os

class RSA_SFTP:
    def __init__(self):
        self.matched_ids = []
        self.matched_passes = []

    def add_pass(self):
        pass_name = input("Enter pass name: ")
        password = input("Enter password: ")

        encrypted_password = rsa.encrypt(password.encode(), self.public_key)

        # Names the password file
        address = "{}-{}.txt".format(self.id, pass_name)

        # Creates password file
        with open(address, "wb") as f:
            f.write(encrypted_password)
            f.close()

        # Sends encrypted password to the server
        with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
            with sftp.cd('passwords'):
                sftp.put(address)

        os.remove(address)

    def get_pass(self):
        pass_name = input("Enter pass name: ")
        address = "{}-{}.txt".format(self.id, pass_name)

        # Gets encrypted password from the server
        try:
            with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
                with sftp.cd('passwords'):
                    sftp.get(address)
        except:
            print("Password with name {} not found".format(pass_name))
            os.remove(address)
            exit()

        with open(address, "rb") as f:
            encrypted_password = f.read()

        password = (rsa.decrypt(encrypted_password, self.private_key)).decode()
        print(password)

        os.remove(address)

    def get_matched_ids(self, user_ids):
        # Gets a list of all the IDs from the server
        with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
            with sftp.cd('passwords'):
                server_ids = sftp.listdir()

        # Prints a list of all the IDs from the server that the user has a matching ID to

        for id in server_ids:
            id_stripped = id.split("-", 1)[0]
            if id_stripped in user_ids:
                self.matched_ids.append(id)

                id_pass = id.split(".", 1)[0]
                self.matched_passes.append(id_pass)
