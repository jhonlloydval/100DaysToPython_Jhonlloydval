# DAY 2 LEARNINGS

# Data types

# Index
# Always starts with 0 due to binary

# Subscripting = getting a certain character
print("Hello"[4])
print("Hello"[-1]) # -1 = Last index



# Data type : Integers (Whole Number)
print(123_456_789) # _ : For visualization 

# Data Type : Float (Floating Point Number)
print(3.14159)

# Boolean : True or False
print(True)
print(False)

# Len Function
print(len("Hello"))

# Type Function
print(type("Hello")) # Type checking
# 15. Type Check exercise
print(type("Hi"))
print(type(1))
print(type(1.1))
print(type(False))
# Type Conversion
print(int("123")+ int("456"))
# 15. Type Conversion challenge
# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Arithmetic Operations
print(1 + 1) # Addition
print(1 - 0) # Subtraction
print(2 / 1) # Division
print(2 * 1) # Multiplication
print(5 // 2) # Floor Division
print(2 ** 3) # Exponentiation
print(10 % 3) # Modulus
# PEMDAS
# BMI CALCULATOR EXERCISE IN ANOTHER PYTHON FILE

# Number Manipulation
# Flooring = base whole number
# Rounding = round up or down a whole number depending on the decimal place
print(round(3.8999)) # Output = 4
print(round(3.89679, 3)) # Output = 3.897

# Assignment Operators
# Accumulates the results of our calculations
score = 0
score = score + 1 # The user scores a point
score += 1 # Best way to do
print(score)

# F Strings
height = 1.8
is_winning = True
print(f"Your score is {score}. Your height is {height}. You are winning is {is_winning}")