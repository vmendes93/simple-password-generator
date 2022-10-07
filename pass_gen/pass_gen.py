# Necessary imports
import string
import secrets

# Global variables
CHARACTERS = string.ascii_letters + string.digits + string.punctuation

# Passgen. function
def password_gen(length=8):
    """
    This function generates a random password with random alphanumeric and special characters.
    Password length can be changed by the user when calling the function.
    """
    global CHARACTERS
    
    password = "".join(secrets.choice(CHARACTERS) for i in range(length))
    
    return password
        