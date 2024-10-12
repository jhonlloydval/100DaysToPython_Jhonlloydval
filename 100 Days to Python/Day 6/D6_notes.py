# DAY 6 LEARNING

# FUNCTIONS
# docs.python.org/3/library/functions.html

# def function
def my_function(): # name of function
    print("hi")

my_function() # calling of function




while True:
    try:
        hello = int(input("Enter a number: "))  # Request numeric input
        break  # Exit the loop if a valid number is entered
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  # Prompt for a valid integer

def my_function(): # Naming your function
    global hello
    print("Hello")
    while hello <= 12:
        print("Hi")
        hello = hello + 1
my_function()

# WHILE LOOP
# while something is true, it will continue running