# DAY 1 LEARNINGS
# Printing
print("Hello World") # Prints "Hello World"

# Coding Exercise 1
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# 7. String Manipulation and Code Intelligence
# \n = printing with more lines in 1 single print statement
print("Hello World\nHello World?\nHello World!") # Prints "Hello World" 3 times in different lines

# Concatenating Strings
print("Hello " + "Jhon Lloyd") 

# Debugging
# Started in 1980s where a moth came inside a computer machine

# Print Function
input("A prompt for the user: ")
print("Hello " + input("What is your name? ") + "!") # Putting a function inside a function

# Comments
# Mac = (command + forward slash) for automatic comment

# 9. Python Variables
# len() function
name = "Jack"
print(name)
print(len(name))
print(len(input("What is your name? ")))

username = input("What is your name: ")
length = len(username)
print(length)

# Errors
# Name error = Raised when a local or global variable is not found
# Syntax error = Happens when the Python parser encounters incorrect syntax.
# Indention error = Raised when there is incorrect indentation, which is critical in Python. 
# Type error = Happens when an operation or function is applied to an object of an inappropriate type. 
# Value error = Raised when a function receives an argument of the correct type but an inappropriate value.
# Index error = Raised when trying to access an index that is out of range for a list or another indexable object.
# Key error = Raised when trying to access a key that doesn’t exist in a dictionary.
# Attribute error = Raised when trying to access an attribute that doesn’t exist for an object.
# Zero Division error = Raised when a division or modulo operation is performed with zero as the divisor.
# Import error / Module Not Found error = Raised when an import statement fails to find the module or when a specific object within a module cannot be imported.
# Runtime error = A general-purpose error that indicates something went wrong during program execution but doesn’t fall under any other error category.
# Recursion error = Raised when the maximum recursion depth is exceeded, typically caused by a function that keeps calling itself indefinitely.
# File Not Found error = Raised when trying to open a file that doesn’t exist.
# Overflow error = Raised when a calculation exceeds the limits of the floating-point number representation.

#Proper handling with Try-except block makes the code more robust.
