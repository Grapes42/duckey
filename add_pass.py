import rsa
import pysftp
import os

with open("keys/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("keys/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

password = input("Enter password: ")

encrypted_password = rsa.encrypt(password.encode(), public_key)

# Creates a password file
with open("password.txt", "wb") as f:
    f.write(encrypted_password)
    f.close()

# Sends encrypted password to the server
with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
    with sftp.cd('passwords'):
        sftp.put('password.txt')

os.remove("password.txt")
