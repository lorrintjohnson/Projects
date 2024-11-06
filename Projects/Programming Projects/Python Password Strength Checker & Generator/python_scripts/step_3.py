import re, string

def checkPassword(password):
    if len(password) < 8:
        reason = "Password length is too short."
        return False, reason

    # Check for at least one uppercase letter
    if len(re.findall(r'[A-Z]', password)) < 1:
        reason = "Password must contain at least one uppercase letter."
        return False, reason

    # Check for at least one lowercase letter
    if len(re.findall(r'[a-z]', password)) < 1:
        reason = "Password must contain at least one lowercase letter."
        return False, reason

    # Check for at least one digit
    if len(re.findall(r'\d', password)) < 1:
        reason = "Password must contain at least one digit."
        return False, reason

    # Check for at least one special character
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 1:
        reason = "Password must contain at least one special character."
        return False, reason

    return True, "Password meets requirements."

password = input("Enter a password: ")
pw_check, reason = checkPassword(password)

if pw_check: print("Good password. " + reason + "\n")
else: print("Bad password. " + reason + "\n")
