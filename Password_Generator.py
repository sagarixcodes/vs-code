print("**WELCOME TO WORLDS BEST PASSWORD GENERATOR**")
print("Press enter to use our service!")
input()

while True:
  import random
  import keyboard


  def password_generator(length):  
    codes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

    password = ""

    for i in range(length):
        password += random.choice(codes)

    return password    


  length = int(input("Enter the desired length of PASSWORD you want to generate : "))

  with open("created_password","a+") as cp :  
    created_passwords = cp.read()

  password = ""
  while password  in created_passwords:
      password = password_generator(length)

  with open("created_password","a+") as cp :
    cp.write(password + "\n")
    
  print("Your password is:",password,"\n")
  print("Do you want to regenerate a new password ?")
  print("Press enter to do so or press q to stop")
  user_input = keyboard.read_key()

  if user_input == "enter":
     continue
  
  elif user_input == "q":
     print("THANK YOU!for using our service.")
     break
