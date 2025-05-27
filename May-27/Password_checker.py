import string

password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

if len(password) >= 8 and has_upper and has_digit and has_symbol:
    print("Strong password")
else:
    print("Weak password")
    if len(password) < 8:
        print("At least 8 characters")
    if not has_upper:
        print(" At least one uppercase letter")
    if not has_digit:
        print("At least one number")
    if not has_symbol:
        print("At least one special symbol")
