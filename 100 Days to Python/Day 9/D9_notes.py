# DAY 9 NOTES
# ABOUT DICTIONARIES AND NESTING

# Dictionaries in python works like in real life
# code:program instructions

# Have two parts
# left = Key (Bug, Function, Loop)
# right = Value (An error in a program that prevents the program from running as expected,
# A piece of code that you can easily call over and over again, and the action of doing something over and over again)

# Dictionary usage
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again"
}

# Dictionary printing
# output = A piece of code that you can easily call over and over again
print(programming_dictionary["Function"])

# Dictionary, adding a key/value
# output = same as dictionary but with loop and its value
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# Output = {}
# programming_dictionary = {}
# print(programming_dictionary)

# Changing a value in dictionary
programming_dictionary["Bug"] = "Hello"
print(programming_dictionary)

# When looped, the KEY is the one being looped
# output = Bug Function Loop
for thing in programming_dictionary:
    print(thing, end=" ")

# Printing the value of the key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

