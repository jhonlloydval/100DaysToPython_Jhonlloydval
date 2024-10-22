# D14 PROJECT
# OPTIMIZED

import random
from art import logo, vs
from game_data import data

# Grammar check for description
def grammar(word):
    return "an" if word[0].upper() in {"A", "E", "I", "O", "U"} else "a"

# Function to get a random comparee from data
def get_random_comparee(exclude=None):
    comparee = random.choice(data)
    while comparee == exclude:  # Avoid duplicate selection
        comparee = random.choice(data)
    return comparee

# Function to play the game
def play_game():
    score = 0
    compare1 = get_random_comparee()
    
    while True:
        print("\n" * 20, logo)
        
        if score > 0:
            print(f"You're right! Current score: {score}")
        
        # Prepare the comparees
        compare2 = get_random_comparee(exclude=compare1)
        
        # Display the comparees
        name1, description1, country1 = compare1['name'], compare1['description'], compare1['country']
        name2, description2, country2 = compare2['name'], compare2['description'], compare2['country']
        print(f"Compare A: {name1}, {grammar(description1)} {description1}, from {country1}")
        print(vs)
        print(f"Against B: {name2}, {grammar(description2)} {description2}, from {country2}")
        
        # Get user input
        while True:
            choice = input("Who has more followers? Type \"A\" or \"B\": ").upper()
            if choice in ["A", "B"]:
                break
            else:
                print("Enter a valid answer.")
                        
        # Determine if the guess is correct
        compare1_followers = compare1['follower_count']
        compare2_followers = compare2['follower_count']
        
        if (choice == "A" and compare1_followers > compare2_followers) or \
           (choice == "B" and compare2_followers > compare1_followers):
            score += 1
            compare1 = compare2  # Move to the next round with the correct comparee
        else:
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

# Start the game
play_game()