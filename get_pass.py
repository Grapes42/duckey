
import rsa
import pysftp
import os

with open("keys/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("keys/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Gets encrypted password from the server
with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
    with sftp.cd('passwords'):
        sftp.get('password.txt')

with open("password.txt", "rb") as f:
    encrypted_password = f.read()

password = (rsa.decrypt(encrypted_password, private_key)).decode()
print(password)

os.remove("password.txt")
