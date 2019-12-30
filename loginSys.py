choice = input("Welcome! Enter 1 to login or 2 to make a new account.")
choice = int(choice)
while choice != 1 and choice != 2:
 choice = input("Enter 1 to login or 2 to make a new account.")
 choice = int(choice)

def login():
  userAttempt = input("Enter your username:")
  passAttempt = input("Enter your password:")
  with open('usernamefile.txt') as f:
    if userAttempt in f.read():
      unameEntry = 1
    else:
      unameEntry = 0
  with open('passfile.txt') as f:
    if passAttempt in f.read():
      pEntry = 1
    else: 
      pEntry = 0
  if unameEntry == 1 and pEntry == 1:
    print("Successful Login")
  elif unameEntry == 1 and pEntry == 0:
    print("Username Corect, Incorrect Password")
  elif unameEntry == 0 and pEntry == 1:
    print("Incorrect Username")
  else:
    print("Unsuccessful Login")

suggPass = " "
import string
import random
def suggestPass():
  specialChar = ['!', '@', '#', '$', '%','^','&','*', '(', ')','-','_', '+','=','|','|','?','>','<','/','.',',']
  suggPass = random.choice(specialChar)
  for i in range(0, 5):
    suggPass = suggPass + str(random.randint(0,9))
    suggPass = suggPass + random.choice(string.ascii_letters)  
    suggPass = suggPass + random.choice(specialChar)
  print("Suggested Password: "+ suggPass)


def createNew():
  newUser = input("Enter a username:")
  newUser = str(newUser)
  suggestPass()
  newPass = input("Enter a secure password that is up to 16 characters long: ")
  newPass = str(newPass)
  while len(newPass) > 16:
    newPass = input("Enter a secure password that is UP TO 16 CHARACTERS LONG:")
  with open('usernamefile.txt', mode = 'w') as f:
    f.write(newUser+"\n")
  with open('passfile.txt', mode = 'w') as f:
    f.write(newPass+"\n")
  print("You have successfully created a new account with the username: "+newUser)


if (choice == 1):
    print("Login:")
    login()
elif (choice == 2):
   print("Create a New Account:")
   createNew()
 