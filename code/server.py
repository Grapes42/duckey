import rsa
import pysftp
import os

class Server:
    def __init__(self, host, username, password):
        self.connection_info = {'host': host, 'username': username, 'password': password}
        self.ids = []

    # Put file in server
    def put(self, path):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                sftp.put(path)

    # Get file from server
    def get(self, path):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                sftp.get(path)

    # Get all files from server in list
    def list_get(self, paths):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                for path in paths:
                    sftp.get(path)

    def decrypt(self, path, private_key):
            with open(path, "rb") as f:
                encrypted_password = f.read()

            password = (rsa.decrypt(encrypted_password, private_key)).decode()
            return password
    
    def encrypt(self, path, public_key, password):

        encrypted_password = rsa.encrypt(password.encode(), public_key)

        with open(path, "wb") as f:
            f.write(encrypted_password)
            f.close()

    # Add a encrypted password in the server
    def add_pass(self, id, public_key):
        pass_name = input("Enter password name: ")
        password = input("Enter password: ")

        path = "{}-{}.txt".format(id, pass_name)

        self.encrypt(path, public_key, password)

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

        password = self.decrypt(path, private_key)
        print(password)

        os.remove(path)

    # List all IDs in the server
    def get_ids(self):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                self.ids = sftp.listdir()