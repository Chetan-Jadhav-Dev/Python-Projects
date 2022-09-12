"""
Make a password generator which takes the length of the
password as input from the user and returns a random
password

"""

#importing random and string modules

import random
import string

# Taking length of the password
length = int(input("Enter password length : "))

#stroring all variable words for password
available_words = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# making a function, which takes length as an argument for our password.
def password_maker(length):
    password_words = []
    for i in range(length):
        password_words.append(random.choice(available_words))
    password = "".join(password_words)
    return password

# making object of function and getting our result using print 
obj = password_maker(length)
print(obj)