import random
codes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
password = ""
for i in range(5):
        password += random.choice(codes)
print(password)        