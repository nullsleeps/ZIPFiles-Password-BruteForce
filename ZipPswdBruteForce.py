import zipfile
import itertools

charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}";.,/`~±§'
max_length = 4 

z = zipfile.ZipFile('secret.zip') #Replace secret.zip with your zip file
tries = 0

def try_password(z, password):
    try:
        z.extractall(pwd=password.encode('ascii'))
        print(f'Password found after {tries} tries: {password}')
        return True
    except (RuntimeError, zipfile.BadZipFile):
        return False

for length in range(1, max_length + 1):
    for password in itertools.product(charlist, repeat=length):
        tries += 1
        password = ''.join(password)
        if try_password(z, password):
            break
    else:
        continue
    break
else:
    print("Password not found.")
