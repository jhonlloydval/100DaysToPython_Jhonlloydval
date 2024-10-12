# DAY 5 
# PASSWORD GENERATOR

import random
password = []    

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("\nHow many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# EASY PASSWORD
for x in range(nr_letters):
    password.append(random.choice(letters))
for x in range(nr_numbers):
    password.append(random.choice(numbers))
for x in range(nr_symbols):
    password.append(random.choice(symbols))

print(password)

# PASSWORD IN SHUFFLE
hard_password = []
for x in password:
    hard_password.insert(random.randint(0,len(hard_password)), x)
print(hard_password)

# PRINTING THE PASSWORDS
easy_password = ""
for x in password:
    easy_password = easy_password + x
print(f"Your easy password is: {easy_password}")

harder_password = ""
for x in hard_password:
    harder_password = harder_password + x
print(f"Your hard password is: {harder_password}")


# LEARN ABOUT .SHUFFLE AND .JOIN










'''
for x in password:
    password.insert((1, len(password)+ 1), random.choice(password))
print(f"Your password is: {password}")
'''








'''
letter_r = 0
while letter_r != nr_letters:
    print(random.choice(letters))
    letter_r += 1

symbols_r = 0
while symbols_r != nr_symbols:
    print(random.choice(symbols))
    symbols_r += 1

numbers_r = 0
while numbers_r != nr_numbers:
    print(random.choice(numbers))
    numbers_r +=1
'''