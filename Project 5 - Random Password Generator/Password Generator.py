# Password Generator Project

# Problem Statement:
# Generate a password according to user input. First you will ask the user the count of letters, symbols and numbers, and accordingly you will generate a random password.




# Program

# Importing random module
import random

# Define letters, numbers, and symbols in a list first
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print Welcome message
print("Welcome to the PyPassword Generator!")

# Ask the count of letters, symbols, and numbers to the user
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Declare the empty list
password_list = []

# Generate random letters with given count
for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Generate random symbols with given count
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# Generate random numbers with given count
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Shuffle the generated password_list
random.shuffle(password_list)

# Declare the empty string
password = ""

# Iterate and store the password in defined string
for p in password_list:
    password = password + p

# Printing the generated password
print(f"Your password is: {password}")
