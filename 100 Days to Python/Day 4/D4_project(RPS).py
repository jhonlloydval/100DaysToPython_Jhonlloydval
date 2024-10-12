# DAY 4 PROJECT
# ROCK PAPER SCISSORS GAME

import random


rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# FIRST SOLUTION
'''
game = [rock, paper, scissors]
print("Welcome to Rock Paper and Scissors Game!\nType 0 for Rock, 1 for Paper, or 2 for Scissors.")

# PLAYER SIDE
player = int(input(""))
print(game[player])

# COMPUTER SIDE
computer = random.choice(game)
print("Computer chose:\n",computer)

if player == 0:
    if computer == rock:
        print("DRAW.")
    elif computer == paper:
        print("YOU LOSE.")
    elif computer == scissors:
        print("YOU WON.")


elif player == 1:
    if computer == rock:
        print("YOU WON.")
    elif computer == paper:
        print("DRAW.")
    elif computer == scissors:
        print("YOU LOSE.")


elif player == 2:
    if computer == rock:
        print("YOU LOSE.")
    elif computer == paper:
        print("YOU WON.")
    elif computer == scissors:
        print("DRAW.")

else:
    print("Please play the game correctly.")

'''
# SECOND SOLUTION


game = [rock, paper, scissors]

# PLAYER SIDE
player = int(input("\nWelcome to Rock Paper Scissors Game!\nType 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(game[player])

# COMPUTER SIDE
computer_choice = random.randint(0,2)
print(f"Computer chose:\n{game[computer_choice]}")

# MECHANICS
if 2 < player < 0:
    print("Please play the game correctly.")
elif player == computer_choice:
    print("DRAW.")
elif player == 0 and computer_choice == 1:
    print("YOU LOSE.")
elif player == 0 and computer_choice == 2:
    print("YOU WIN.")
elif player == 1 and computer_choice == 2:
    print("YOU LOSE.")