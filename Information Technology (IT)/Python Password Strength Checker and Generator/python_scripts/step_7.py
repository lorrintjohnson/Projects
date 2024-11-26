import re, random, string 

def checkPassword(password):
    reason = []
    fix = []
    # Check for at least 8 total characters
    if len(password) < p_length:
        reason.append("Password must contain " + str(p_length) + " characters and current length is " + str(len(password)) + ". ")
        
    # Check for at least one uppercase letter
    if len(re.findall(r'[A-Z]', password)) < p_upper:
        reason.append("Password must contain " + str(p_upper) + " uppercase letters and currently has " + str(len(re.findall(r'[A-Z]', password))) +  ". ")
        #Add uppers
        password += ''.join(random.choices(string.ascii_uppercase, k=p_upper - len(re.findall(r'[A-Z]', password))))
        
    # Check for at least one lowercase letter
    if len(re.findall(r'[a-z]', password)) < 1:
        reason.append("Password contains " + str(len(re.findall(r'[a-z]', password))) + " lowercase letters.")
        #Remove? 

    # Check for at least one digit
    if len(re.findall(r'\d', password)) < p_digit:
        reason.append("Password must contain " + str(p_digit) + " digits and currently has " + str(len(re.findall(r'\d', password))) + ". ")
        #Add digits
        
    # Check for at least one special character
    if len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password)) < p_specChar:
        reason.append("Password must contain " + str(p_specChar) + " special characters and currently has " + str(len(re.findall(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password))) + ". ")
        #Add special chars 
        
    if reason: return False, "\n".join(reason), password
    return True, "Password meets requirements.", password

#Add user input validation  
def validateInteger(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer.")

def generatePassword(input_str, p_length, p_upper, p_digit, p_specChar):
    # Initialize lists to store characters
    lower_chars = []
    upper_chars = []
    digit_chars = []
    special_chars = []
    
    # Split the input string into character categories
    for char in input_str:
        if char.islower():
            lower_chars.append(char)
        elif char.isupper():
            upper_chars.append(char)
        elif char.isdigit():
            digit_chars.append(char)
        else:
            special_chars.append(char)
    
    # Calculate how many more characters are needed for each category
    add_upper = max(0, p_upper - len(upper_chars))
    add_digit = max(0, p_digit - len(digit_chars))
    add_specChar = max(0, p_specChar - len(special_chars))
    
    # Generate additional random characters for each category
    random_upper = ''.join(random.choice(string.ascii_uppercase) for _ in range(add_upper)) if len(upper_chars) < p_upper else ''
    random_digit = ''.join(random.choice(string.digits) for _ in range(add_digit))
    random_specChar = ''.join(random.choice(string.punctuation) for _ in range(add_specChar))
    
    # Combine all characters to form the password
    password = (
        ''.join(upper_chars) +
        ''.join(digit_chars) +
        ''.join(special_chars) +
        ''.join(lower_chars) +  # Keep the original lowercase characters
        random_upper +
        random_digit +
        random_specChar
        )
    
    # Trim or pad the password to meet the minimum length requirement
    if len(password) < p_length:
        # Add lowercase letters if needed to meet the minimum length
        add_lower = p_length - len(password)
        random_lower = ''.join(random.choice(string.ascii_lowercase) for _ in range(add_lower))
        password += random_lower
        
    if len(password) > p_length:
        excess_lower = len(password) - p_length
        # Remove the excess lowercase characters
        lower_chars = lower_chars[:-excess_lower]
        # Recombine the password
        password = (
        ''.join(upper_chars) +
        ''.join(digit_chars) +
        ''.join(special_chars) +
        ''.join(lower_chars) +  # Keep the original lowercase characters
        random_upper +
        random_digit +
        random_specChar
        )
    return password

#Add user inputs for each requirement
p_length = validateInteger("Enter the number of required characters for the password: ")
p_upper = validateInteger("Enter the number of uppercase letters required: ")
p_digit = validateInteger("Enter the number of digits required: ")
p_specChar = validateInteger("Enter the number of special characters required: ")

password = input("\nEnter a password: ")

pw_check, reason, password = checkPassword(password)

#Generate new password 
if pw_check: print("\nStrong password. " + reason + "\n")
else:
    print("\nPassword does not meet requirements. \n" + reason)
    new_p = generatePassword(password, p_length, p_upper, p_digit, p_specChar)
    print("\nNew password that meets requirements: " + new_p + "\n")
