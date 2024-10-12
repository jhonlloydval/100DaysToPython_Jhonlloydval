# DAY 2 PROJECT
# TIP CALCULATOR

# EFFICIENT 
'''
print("Welcome to the tip calculator!")
total_bill = int(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill_split = int(input("How many people to split the bill? "))
# or tip / 100 * total_bill + total_bill
print(f"Each person should pay: ${round(total_bill * (1 + tip/100) / bill_split, 2)}")
'''

# READABILITY
# Real world scenarios prefer readability than efficiency

print("Welcome to the tip calculator!")
total_bill = int(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill_split = int(input("How many people to split the bill? "))

total_with_tip = tip / 100 * total_bill + total_bill
splitted_bill = total_with_tip / bill_split
final_bill = round(splitted_bill, 2)

print(f"Each person should pay: ${final_bill}")
