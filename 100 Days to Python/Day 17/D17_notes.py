# DAY 17
# MAKING YOUR OWN CLASS

# We make a CLASS by class User: (The naming should be in PascalCase or camelCase)
class User:
    pass # used to ignore a requirement to input

# Making an OBJECT of a class. 
user_1 = User()

# Making an attribute of a class
# ATTRIBUTE is a variable associated with an object
# Attributes are the things that the object will have

user_1.id = "001"
user_1.username = "angela"
print(user_1.username)

# CONSTRUCTOR part of a blueprint that allows us to specify what
# should happen when our object is being constructed
# also called as INITIALIZING
# using __init__(self) function


class NewClass:
    def __init__(self):
        print("new user being created")

first = NewClass()