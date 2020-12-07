import zipfile

charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}";.,/`~±§'
complete = []

for current in range(100):
    a = [i for i in charlist]
    for x in range(current):
        a =[y + i for i in charlist for y in a]
    complete = complete + a

print(complete)

z = zipfile.ZipFile('secret.zip')

tries = 0

for password in complete:
    try:
        z.setpassword(password.encode('ascii'))
        z.extract('secret.zip')
        print(f'password was found tries are : {tries}, the password was {password}')
    
    except:
        pass
