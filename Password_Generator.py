import random

def password_generator(length):
    codes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

    password = ""

    for i in range(length):
        password += random.choice(codes)

    return password    

print("**WELCOME TO WORLDS BEST PASSWORD GENERATOR**")
length = int(input("Enter the desired length of PASSWORD you want to generate : "))

with open("created_password","a+") as cp :
    created_passwords = cp.read()

password = ""
while password  in created_passwords:
    password = password_generator(length)

with open("created_password","a+") as cp :
    cp.write(password + "\n")
    
print("Your password is:",password)
