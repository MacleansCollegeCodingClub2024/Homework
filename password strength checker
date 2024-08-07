import re

def validate_password(word):
    if len(word) < 8:
        return False
    
    if not re.search(r'[A-Z]', word):
        return False
    
    if not re.search(r'[a-z]', word):
        return False
    
    if not re.search(r'\d', word):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', word):
        return False
    
    return True

word = input("Type in the funny password: ")
probably_works = validate_password(word)

if probably_works:
    print("wowie good job!!1!")
else:
    print("your password is skill issue.")
