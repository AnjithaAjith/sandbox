"""Anjitha Ajith"""

password = input("Enter a password of length atleast 6 characters ")
if len(password) < 6:
    password = input("Enter a password of length atleast 6 characters ")
print("*" * len(password))