"""
Problem Statement
Write a Python function called check_password_strength(password) that takes a string password as input and returns a string indicating the strength of the password based on the following rules:

Weak:

Password length is less than 8 characters.

Contains only lowercase letters or only numbers.

Medium:

Password length is at least 8 characters.

Contains a combination of lowercase letters and numbers.

Strong:

Password length is at least 8 characters.

Contains a combination of lowercase letters, uppercase letters, numbers, and at least one special character (e.g., !, @, #, $, etc.).

Invalid:

If the password contains spaces, it is considered invalid.
"""

password = input("Please insert Your password... ")

haslower = any(char.islower() for char in password)
hasupper = any(char.isupper() for char in password)
hasdigit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()-_=+[]{};:'\",.<>/?`~" for char in password)


if(' ' in password):
    print("The password is Invalid")
elif (len(password)<8):
    print("Your password is Weak")

elif(len(password)>=8 and haslower and hasupper and hasdigit and has_special):
    print("You use Strong password")
elif(len(password)>=8 and haslower and hasdigit):
    print("You use Medium password")



