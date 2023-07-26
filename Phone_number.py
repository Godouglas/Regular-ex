import re


def validate_number(phone_number):
    pattern = r"^\+233[0-9]{9}$"
    return re.match(pattern, phone_number)


def check_number():
    while True:
        phone_number = (input("Enter your phone number: "))
        if validate_number(phone_number):
            print("Phone number is valid!")
            break
        else:
            print("Please enter phone number in the format: +233'XXXXXXXXX'")


check_number()
