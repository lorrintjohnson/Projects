import string, re

def checkPassword(password):
    reason = []
    # Check for at least 8 total characters
    if len(password) < 8:
        reason.append("Password length is " + str(len(password)) + " characters.")

    # Check for at least one uppercase letter
    if len(re.findall(r'[A-Z]', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'[A-Z]', password))) +  " uppercase letters.")

    # Check for at least one lowercase letter
    if len(re.findall(r'[a-z]', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'[a-z]', password))) + " lowercase letters.")

    # Check for at least one digit
    if len(re.findall(r'\d', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'\d', password))) + " digits.")

    # Check for at least one special character
    if len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password))) + " special characters.")

    if reason: return False, "\n".join(reason)
    return True, "Password meets requirements."

password = input("Enter a password: ")
pw_check, reason = checkPassword(password)

if pw_check: print("Good password. " + reason + "\n")
else: print("Bad password. \n" + reason + "\n")
