import rsa
import pysftp
import os

with open("keys/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("keys/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

with open("keys/user_id.txt", "r") as f:
    user_id = f.read()

password = input("Enter password: ")
pass_name = input("Enter pass name: ")

encrypted_password = rsa.encrypt(password.encode(), public_key)

# Creates a password file
address = "{}-{}.txt".format(user_id, pass_name)

with open(address, "wb") as f:
    f.write(encrypted_password)
    f.close()

# Sends encrypted password to the server
with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
    with sftp.cd('passwords'):
        sftp.put(address)

os.remove(address)