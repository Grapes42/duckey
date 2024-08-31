import rsa
import pysftp
import os

class Encryption:
    def __init__(self, host, username, password):
        self.connection_info = self.connection_info = {'host': host, 'username': username, 'password': password}

        self.user_info_dir = "user_info"

        self.id_path = f"{self.user_info_dir}/id.txt"
        self.public_key_path = f"{self.user_info_dir}/public.pem"
        self.private_key_path = f"{self.user_info_dir}/private.pem"

        # If there is an empty or invalid key structure, backup and generate keys
        if (not os.path.exists(self.id_path) 
            or not os.path.exists(self.public_key_path) 
            or not os.path.exists(self.private_key_path)
            ):
            self.generate()

        self.update_user_info()


    def update_user_info(self):
        with open(self.id_path, "r") as f:
            self.id = f.read()

        with open(self.public_key_path, "r") as f:
            self.public_key = rsa.PublicKey.load_pkcs1(f.read())

        with open(self.private_key_path, "r") as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())

    def generate(self):
        if not os.path.exists(self.user_info_dir):
            os.makedirs(self.user_info_dir)

        # Generates a private and public key
        generated_public_key, generated_private_key = rsa.newkeys(1024)

        with open(self.public_key_path, "wb") as f:
            f.write(generated_public_key.save_pkcs1("PEM"))
            f.close()

        with open(self.private_key_path, "wb") as f:
            f.write(generated_private_key.save_pkcs1("PEM"))
            f.close()

        # Generates a ID based off the first 10 chars of the public key
        generated_id = str(generated_public_key)[10:20]
        
        with open(self.id_path, "w") as f:
            f.write(generated_id)      

    #
    # Basic file sending and retrieving
    #
    def put(self, path):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                sftp.put(path)

    def get(self, path):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                sftp.get(path)
    #
    #
    #

    #
    # Encryption
    #
    def encrypt_and_store(self, passname, username, password):
        path = f"{self.id}-{passname}.duckey"

        encrypted_username = rsa.encrypt(username.encode(), pub_key=self.public_key)
        encrypted_password = rsa.encrypt(password.encode(), pub_key=self.public_key)

        content = f"{encrypted_username}:::{encrypted_password}"

        with open(path, "w") as f:
            f.write(content)

        self.put(path)
        os.remove(path)

    def get_and_decrypt(self, passname):
        path = f"{self.id}-{passname}.duckey"
        self.get(path)

        with open(path, "r") as f:
            content = f.read()

        encrypted_username = content.split(":::")[0]
        encrypted_password = content.split(":::")[1]

        username = (rsa.decrypt(encrypted_username, self.private_key)).decode()
        password = (rsa.decrypt(encrypted_password, self.private_key)).decode()

        print(username)
        print(password)


    def list_passwords(self):
        with pysftp.Connection(**self.connection_info) as sftp:
            with sftp.cd("passwords"):
                all_passwords = sftp.listdir()

        owned_passwords = []

        for password in all_passwords:
            if self.id in password:
                owned_passwords.append(password)

        return owned_passwords