import random
import string


def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Welcome message
print("Welcome to the Password Generator!")
print("You can customize your password by selecting the character types to include.")

# User input for password length
password_length = int(input("Enter the length of the password: "))

# User input for character types to include
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate the password based on user inputs
generated_password = generate_password(
    length=password_length,
    uppercase=include_uppercase,
    lowercase=include_lowercase,
    digits=include_digits,
    special_chars=include_special_chars
)

if generated_password:
    print("Generated Password:", generated_password)
else:
    print("No password generated. Please try again.")