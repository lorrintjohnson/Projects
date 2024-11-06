import string 

def checkPassword(password):
    if len(password) < 8:
        reason = "Password length is too short."
        return False, reason
    else: return True, "Password meets requirements."

password = input("Enter a password: ")
pw_check, reason = checkPassword(password)

if pw_check:
    print("Good password. " + reason)
else: print ("Bad password. " + reason)
