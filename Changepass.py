import re


def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W])[A-Za-z0-9\W]{8,}$"
    return re.match(pattern, password)


def change_password():
    while True:
        password = input("Enter your new password: ")
        if validate_password(password):
            print("Password successfully changed!")
            break
        else:
            print("Invalid password!Passwords must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special symbol.")


change_password()
