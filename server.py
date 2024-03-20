import rsa
import pysftp
import os

class Server:
    def __init__(self, address, username, password):
        self.connection = pysftp.Connection(address, username=username, password=password)
        self.ids = []

    # Put file in server
    def put(self, path):
        with self.connection as sftp:
            with sftp.cd("passwords"):
                sftp.put(path)

    # Get file from server
    def get(self, path):
        with self.connection as sftp:
                with sftp.cd("passwords"):
                    sftp.get(path)

    # Add a encrypted password in the server
    def add_pass(self, id, public_key):
        pass_name = input("Enter password name: ")
        password = input("Enter password: ")

        encrypted_password = rsa.encrypt(password.encode(), public_key)

        path = "{}-{}.txt".format(id, pass_name)

        with open(path, "wb") as f:
            f.write(encrypted_password)
            f.close()

        self.put(path)

        os.remove(path)

    # Return and decrypt a password from the server
    def get_pass(self, id, private_key):
        pass_name = input("Enter pass name: ")
        path = "{}-{}.txt".format(id, pass_name)

        try:
            self.get(path)
        except:
            print("Password with name {} not found".format(pass_name))
            os.remove(path)
            exit()

        with open(path, "rb") as f:
            encrypted_password = f.read()

        password = (rsa.decrypt(encrypted_password, private_key)).decode()
        print(password)

        os.remove(path)

    # List all IDs in the server
    def get_ids(self):
        with self.connection as sftp:
            with sftp.cd("passwords"):
                self.ids = sftp.listdir()