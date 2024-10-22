# DAY 14 PROJECT
# HIGHER OF LOWER

# TO DO

# IMPORT MODULES

import random
from art import logo, vs
from game_data import data

# SET UP THE MECHANICS

# SET UP THE GAME START MENU

# Grammar check for description
def grammar(word):
    if word[0] in ["A", "E", "I", "O", "U"]:
        return "an"
    else:
        return "a"
# FUNCTION : SCORING
score = 0
compare2 = ""

# FUNCTION : FIRST COMPAREE
def game(score, prev_comparee):
    while True:
        # LOGO print
        print("\n" * 20, logo)

        # Print current score
        if score > 0:
            print(f"You're right! Current score: {score}")
        
        # Preparing the first comparee
        if score > 0:
            compare1 = prev_comparee
        else:
            compare1 = random.choice(data)
        compare1_followers = int(compare1['follower_count'])
        name1 = compare1['name']
        description1 = compare1['description']
        country1 = compare1['country']

        print(f"Compare A: {name1}, {grammar(description1)} {description1}, from {country1} \n")
        
        # VS print
        print(vs)

        # Preparting the second comparee
        while True:
            compare2 = random.choice(data)
            if compare2 == compare1:
                continue
            else:
                break
        compare2_followers = compare2['follower_count']
        name2 = compare2['name']
        description2 = compare2['description']
        country2 = compare2['country']
        
        print(f"Against B: {name2}, {grammar(description2)} {description2}, from {country2} ")


        while True:
            choice = input("Who has more followers? Type \"A\" or \"B\": ").upper()
            if choice in ["A", "B"]:
                break
            else:
                print("Enter a valid answer.")

        if choice == "A":
            if compare1_followers > compare2_followers:
                score += 1
                game(score, compare2)
            else:
                print("\n" * 20)
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                exit()
            
        elif choice == "B":
            if compare2_followers > compare1_followers:
                score += 1
                game(score, compare2)
            else:
                print("\n" * 20)
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                exit()


game(score, compare2)