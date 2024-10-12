# DAY 4 

# RANDOMISATION
import random

# Random Functions for integers
# random.randint(a,b)
print(random.randint(1,100)) # prints number from 1-100 including 1 and 100


# What is a MODULE?
# Module is responsible for different bit of functionality of a program
# How do we create our own module? 

# Random Functions for float numbers
# random.random = 0 to 0.999999
random_float = random.random() * 10 #from 0 to 10 not including int 10
print(random_float)

# Random function for floating point number
# random.uniform(1-10)
print(random.uniform(1,10)) # from 1.0000 to 10.0000, both inclusive


# LISTS 
# List is a data structure - a way of storing a data in a group in python
# fruits = ['cherry', 'cucumber, 'durian']
# They have order called index

numlist = [1, 2, 3, 4, 5, 6, 7]
print(numlist)
# [-1] = last item
# [-2] = 2nd to the last
numlist.append(8) # Append, add 1 to the list
print(numlist)

numlist.extend([9, 10]) # Extend the list, add to the last
print(numlist)

numlist.insert(1, 10) # Insert 10 at index 1
print(numlist)

# Nested Lists
fruits = ["apple", "banana", "cucumber"]
numbers = [1, 2, 3, 4, 5]

fruity_number = [fruits, numbers] # output = [['apple', 'banana', 'cucumber'], [1, 2, 3, 4, 5]]
print(fruity_number)
print(fruity_number[0][1]) # prints index 0 = fruits so index 1 = banana


# IndexError
print(numlist[len(numlist) - 1])
