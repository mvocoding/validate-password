from main import validate_password

# valid password
def test_valid_password():
    assert validate_password("GoodPass123!") is True

# edge case with exactly 8 characters
def test_eight_characters():
    assert validate_password("Abc123!@") is True

# exactly 20 characters
def test_max_length():
    assert validate_password("StrongPass123!@ABCde") is True

# password has space
def test_password_with_space():
    assert validate_password("My Pass123!") is True  

# no special character
def test_no_special_char():
    assert validate_password("Password1234") is True 
