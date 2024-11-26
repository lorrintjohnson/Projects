import re, random, string 

def checkPassword(password, p_length):
    reason = []
    # Check for at least 8 total characters
    if len(password) < int(p_length):
        reason.append("Password must contain " + p_length + " characters and current length is " + str(len(password)) + " characters.")

    # Check for at least one uppercase letter
    if len(re.findall(r'[A-Z]', password)) < int(p_upper):
        reason.append("Password must contain " + p_upper + " uppercase letters and currently has " + str(len(re.findall(r'[A-Z]', password))) +  " uppercase letters.")

    # Check for at least one lowercase letter
    if len(re.findall(r'[a-z]', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'[a-z]', password))) + " lowercase letters.")

    # Check for at least one digit
    if len(re.findall(r'\d', password)) < int(p_digit):
        reason.append("Password must contain " + p_digit + " digits and currently has " + str(len(re.findall(r'\d', password))) + " digits.")

    # Check for at least one special character
    if len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password)) < int(p_specChar):
        reason.append("Password must contain " + p_specChar + " special characters and currently has " + str(len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password))) + " special characters.")

    if reason: return False, "\n".join(reason)
    return True, "Password meets requirements."

#Add user inputs for each requirement 
p_length = input("Enter the number of required characters for the password: ")
p_upper = input("Enter the number of required uppercase letters for the password: ")
p_digit = input("Enter the number of required numbers/digits for the password: ")
p_specChar = input("Enter the number of required special characters for the password: ") #Any restrictions?
#print("\n")
password = input("\nEnter a password: ")

pw_check, reason = checkPassword(password, p_length)
#print("\n")
if pw_check: print("\nStrong password. " + reason +"\n")
else: print("\nPassword does not meet requirements. \n" + reason+"\n")
