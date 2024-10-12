# DAY 3 PROJECT
# TREASUE ISLAND GAME

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('You\'re at the cross road, where do you want to go? Type "left" or "right".')
direction = input("").lower()

if direction == "left":
    print("\nYou've come to a lake. There is an island in the middle of the lake.    Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    swim = input(" ").lower()
    if swim == "wait":
        print("\nYou arrive at the island unharmed. There is a house with 3 doors.\n   One red, one yellow, and one blue. Which colour do you choose?\n")
        colour = input(" ").lower()
        if colour == "red":
            print("\nGame Over.\n")
        elif colour == "blue":
            print("\nGame Over.\n")
        elif colour == "yellow":
            print("\nYou Win!\n")
    elif swim == "swim":
        print("\nGame Over.\n")
    else:
        print("\nEnter a valid input.\n")
elif direction == "\nright\n":
    print("\nGame Over.\n")
else:
    ("\nEnter a valid input.\n")

# I SHOULD MAKE MY OWN VERSION

