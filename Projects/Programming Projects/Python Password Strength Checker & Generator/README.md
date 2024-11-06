# Python Password Strength Checker & Generator

## Project Summary
This project started as my first beginner cyber project, aimed at diving into cybersecurity while also enhancing my Python skills. What began as a simple exercise quickly grew into a full-blown password validation and generation tool. Initially, I just wanted to ensure a password met a basic length requirement. But as I got more into it, I realized there was so much more I could do.

## Steps Taken
1. **Create the Password Validation Function**: 
   - Started with a simple function to check if a password meets the minimum length requirement of 8 characters. This step helped refresh my Python skills and set the foundation for more complex validations. 
   - View Code

2. **Provide Feedback for Invalid Passwords**: 
   - Enhanced the function to include feedback on why a password did not meet the requirements. Introduced a `reason` variable to store and return specific feedback, improving user experience by providing immediate insights into what went wrong.
   - View Code

3. **Implement Advanced Password Requirements**: 
   - Added checks for uppercase letters, lowercase letters, digits, and special characters using regular expressions. This step ensured that passwords are not only of sufficient length but also complex enough to be secure.
   - View Code

4. **Enhance Feedback Specificity**: 
   - Improved the feedback mechanism by listing all unmet requirements and the current count of each type of character in the password. This detailed feedback helps users understand exactly what is missing from their passwords.
   - View Code

5. **Customize Password Requirements**: 
   - Allowed users to specify the minimum number of characters, uppercase letters, digits, and special characters required in the password. This customization makes the script more flexible and user-friendly, catering to different security needs.
   - View Code

6. **Implement Input Validation**: 
   - Added error checks to ensure user inputs for password requirements are valid integers. Created a `validateInteger` function to prompt users for valid integer inputs, ensuring the script handles invalid inputs gracefully.
   - View Code

7. **Generate a Valid Password**: 
   - Created a function to automatically generate a valid password if the user-provided password does not meet the specified requirements. This function adjusts the password to include the necessary characters and meet the specified length, providing a ready-to-use strong password.
   - View Code

## Conclusion
Overall, this project was a great way to dive into cybersecurity and Python, resulting in a really useful tool for password validation and generation. Key functions included: 
- **checkPassword**: Validates the password against specified criteria, including length, uppercase and lowercase letters, digits, and special characters. Provides detailed feedback on any unmet requirements.
- **validateInteger**: Ensures that user inputs for password requirements are valid integers, prompting the user to enter a valid integer if necessary.
- **generatePassword**: Automatically generates a valid password if the user-provided password does not meet the specified requirements. Adjusts the password to include the necessary characters and meet the specified length.

**Skills Demonstrated**
- Data validation
- Regular expressions
- User input handling
- Error checking
- Python scripting

### Potential Future Projects
- **Generating Passwords Upon Request**: Extending the tool to let users request a new password that meets their criteria without needing to provide an initial password.
- **Integrating MySQL for a Password Manager**: Turning this into a full-blown password manager by integrating MySQL, creating a secure database to store and manage passwords, implementing encryption for security, and building a user-friendly interface for easy access.

These future projects would make the tool even more versatile and useful, turning it into a robust solution for managing and securing passwords.
