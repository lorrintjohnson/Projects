import re, random, string 

def checkPassword(password):
    reason = []
    # Check for at least 8 total characters
    if len(password) < p_length:
        reason.append("Password must contain " + str(p_length) + " characters and current length is " + str(len(password)) + ". ")

    # Check for at least one uppercase letter
    if len(re.findall(r'[A-Z]', password)) < p_upper:
        reason.append("Password must contain " + str(p_upper) + " uppercase letters and currently has " + str(len(re.findall(r'[A-Z]', password))) +  ". ")

    # Check for at least one lowercase letter
    if len(re.findall(r'[a-z]', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'[a-z]', password))) + " lowercase letters.")

    # Check for at least one digit
    if len(re.findall(r'\d', password)) < p_digit:
        reason.append("Password must contain " + str(p_digit) + " digits and currently has " + str(len(re.findall(r'\d', password))) + ". ")

    # Check for at least one special character
    if len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password)) < p_specChar:
        reason.append("Password must contain " + str(p_specChar) + " special characters and currently has " + str(len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password))) + ". ")

    if reason: return False, "\n".join(reason)
    return True, "Password meets requirements."

#Add user input validation  
def validateInteger(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer.")

#Add user inputs for each requirement 
p_length = validateInteger("Enter the number of required characters for the password: ")
p_upper = validateInteger("Enter the number of uppercase letters required: ")
p_digit = validateInteger("Enter the number of digits required: ")
p_specChar = validateInteger("Enter the number of special characters required: ") 

password = input("\nEnter a password: ")

pw_check, reason = checkPassword(password)

if pw_check: print("\nStrong password. " + reason + "\n")
else: print("\nPassword does not meet requirements. \n" + reason + "\n")
