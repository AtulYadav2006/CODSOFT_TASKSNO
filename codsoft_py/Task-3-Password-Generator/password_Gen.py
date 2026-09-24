import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Characters that can be used in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the password
print("Generated Password:", password)