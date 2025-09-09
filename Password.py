import random
import string

# User input for password length
length = int(input("Enter the desired password length: "))

# Characters to use in the password (letters, digits, symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("Generated Password:", password)