import string

def validate_password(password: str) -> bool:
    """
    A simple validates function to check if a password based on these rules:
    - At least 8 characters
    - At least one number
    - At least one uppercase letter
    - At least one special character (e.g. !@#$%^&)
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    if not any(char.islower() for char in password): # must have at least one lowercase character
        return False
    if len(password) > 20: # Add password can't more than 20 characters
        return False
    return True
