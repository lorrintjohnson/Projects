def checkPassword(password):
 if len(password) < 8:
     return False
 else: return True

password = input("Enter a password: ")
pw_check = checkPassword(password)

if pw_check:
    print("Good password")
else: print ("Bad password")
