import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# prompts the user for details
response = input(
    "Do you want your password to contain digits and special characters (Y/N): ")
length = int(input("Enter length for password: "))

# checks to see if user wants digits and special charcters then creates password
if response.lower() == 'y':
    combination = letters + numbers + symbols
    password = "".join(random.sample(combination, length))
    print(f"Your Generated Password is: {password}")

elif response.lower() == 'n':
    combination = letters
    password = "".join(random.sample(combination, length))
    print(f"Your Generated Password is: {password}")
