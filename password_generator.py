import random
import string

print("===== Random Password Generator =====")

try:
    length = int(input("Enter the password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
