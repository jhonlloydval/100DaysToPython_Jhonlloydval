# DAY 3 Challenge coding task
# Pizza Delivery Coding Challenge

'''
print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if pepperoni == "Y":
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
'''

# Another solution based on the bootcamp itself

print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size of pizza do you want? S, M, or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Enter a valid size.")
    exit()

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
