# DAY 10 PROJECT
# MAKING A CALCULATOR

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def floor_division(n1,n2):
    return n1 // n2

def modulo(n1, n2):
    return n1 % n2

operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide,
             "//": floor_division,
             "%": modulo}

print(logo)
n1 = float(input("\nWhat's the first number?: "))

while True:
    for symbol in operation:
        print(symbol)
    enter_operation = input("Pick an operation: ")
    n2 = float(input("What's the second number?: "))
    answer = operation[enter_operation](n1, n2)
    print(f"{n1} {enter_operation} {n2} = {answer}")

    prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    if prompt == "y":
        n1 = answer
        continue
    if prompt == "n":
        print("\n" * 20)
        print(logo)
        n1 = float(input("\nWhat's the first number?: "))
        continue

# DAY 10 SOLUTION BASED ON ANGELA YU

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def floor_division(n1,n2):
    return n1 // n2

def modulo(n1, n2):
    return n1 % n2

operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide,
             "//": floor_division,
             "%": modulo}

def calculator():
        
    print(logo)
    should_accumulate = True
    n1 = float(input("\nWhat's the first number?: "))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        enter_operation = input("Pick an operation: ")
        n2 = float(input("What's the second number?: "))
        answer = operation[enter_operation](n1, n2)
        print(f"{n1} {enter_operation} {n2} = {answer}")

        prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        
        if prompt == "y":
            n1 = answer
        if prompt == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
