"""

Make a password decryptor, which will take an encrypted string as input and will give your password

"""

# Importing fernet from cryptography.fernet 

from email.utils import decode_params
from cryptography.fernet import Fernet
import random
import string

#Passoword Generator function
#stroring all variable words for password
available_words = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# making a function, which takes length as an argument for our password.
def password_maker(length):
    password_words = []
    for i in range(length):
        password_words.append(random.choice(available_words))
    password = "".join(password_words)
    return password

#Making password generator obj for storing password
password = password_maker(5)
# Generating key for encryption and decryption
key = Fernet.generate_key()

#instance the fernet class with key generator
fernet = Fernet(key)

#Encrypting the password
encPassword = fernet.encrypt(password.encode())

print("The Encoded password is : ", encPassword)

#Decrypting of the encoded password and storing it into a decPassword variable
decPassword = fernet.decrypt(encPassword).decode()

# Printing decoded password
print("The Decoded password is : ", decPassword)