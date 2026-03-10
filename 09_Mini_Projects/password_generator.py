Purpose

Generate a random strong password using letters, numbers, and symbols.

Code
# password_generator.py

import random
import string

print("Password Generator")

# Password length
length = int(input("Enter password length: "))

# Characters used for password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
Example Output
Password Generator
Enter password length: 10
Generated Password: aK#9xP!2@b
