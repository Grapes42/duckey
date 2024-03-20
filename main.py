import os
from rsa_sftp import RSA_SFTP
from rsa_man import RSA_man

man = RSA_man()
sftp = RSA_SFTP()

if os.path.isfile("keys/public.pem") and os.path.isfile("keys/private.pem") and os.path.isfile("keys/id.txt"):
    suffix = "(Current key structure is valid)"
    valid_structure = True

elif os.path.isfile("keys/public.pem") or os.path.isfile("keys/private.pem") or os.path.isfile("keys/id.txt"):
    suffix = "(Current key structure is incomplete)"
    valid_structure = False
else:
    suffix = "(No keys found)"
    valid_structure = False

options = """1. Get password
2. Add password
3. Generate keys {}
4. Rollback to previous keys
""".format(suffix)

print(options)
option = int(input("Enter option: "))

if option == 0:
    exit()
elif option == 1:
    sftp.get_pass()
elif option == 2:
    sftp.add_pass()
elif option == 3:
    if valid_structure:
        man.backup_keys()
        man.generate_keys()
    else:
        man.generate_keys()
        man.backup_keys()
elif option == 4:
    sftp.get_matched_ids(man.get_user_ids())
    man.rollback(sftp.matched_ids)

