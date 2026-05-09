import random

def password_generator(length):

    print("length received:", length)

    characters = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%&"

    password = ""

    for character in range(length):
        password += random.choice(characters)

    with open("Created_Passwords", "a") as cp:
        cp.write(password + "\n")

    return password


print("**Welcome! This is world's best password generator**")

length = int(input("Enter the length of password you want to generate:\n"))

password = password_generator(length)

with open("Created_Passwords", "r") as cp:
    content = cp.read()

if password in content:
    print(f"Your password is:\n{password}")