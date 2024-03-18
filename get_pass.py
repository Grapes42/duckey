
import rsa
import pysftp
import os

with open("keys/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("keys/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

with open("keys/user_id.txt", "r") as f:
    user_id = f.read()

pass_name = input("Enter pass name: ")
address = "{}-{}.txt".format(user_id, pass_name)

# Gets encrypted password from the server
with pysftp.Connection('ilovemyholly.ddns.net', username='pass_man', password='6arleyhuman') as sftp:
    with sftp.cd('passwords'):
        sftp.get(address)

with open(address, "rb") as f:
    encrypted_password = f.read()

password = (rsa.decrypt(encrypted_password, private_key)).decode()
print(password)

os.remove(address)
