# D12 Project
# Number Guessing Game

import random  # Importing the random module to generate a random number

# Generate a random number between 1 and 100
hidden_number = random.randint(1, 100)

def game(lives):
    """
    The main game function that runs the guessing game.
    Takes an argument 'lives' which determines the number of attempts.
    """
    while lives > 0:  # Continue the game as long as there are remaining attempts
        print(f"You have {lives} attempts to guess the number.")
        guess = int(input("Make a guess: "))  # Player makes a guess

        # Check if the guess is correct
        if guess == hidden_number:
            print(f"You got it! The answer was {hidden_number}.")
            return  # Exit the function since the game is won

        # Decrement the number of lives if the guess is wrong
        lives -= 1

        # Provide feedback if the guess is too low or too high
        if guess < hidden_number:
            print("Too low.")
        elif guess > hidden_number:
            print("Too high.")

        # If lives run out, inform the player they've lost
        if lives == 0:
            print(f"\nYou've run out of guesses.\nThe hidden number was {hidden_number}.\n\nYou lose. ")
        else:
            print("Guess again.")  # Prompt the player to try again if they have remaining lives

# ASCII art and game introduction
print("""
   _   _                 _                  
  | \\ | |               | |                 
  |  \\| |_   _ _ __ ___ | |__   ___ _ __    
  | . ` | | | | '_ ` _ \\| '_ \\ / _ \\ '__|   
  | |\\  | |_| | | | | | | |_) |  __/ |      
  |_| \\_|\\__,_|_| |_| |_|_.__/ \\___|_|      
   / ____|                   (_)            
  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
  | | |_ | | | |/ _ \\/ __/ __| | '_ \\ / _` |
  | |__| | |_| |  __/\\__ \\__ \\ | | | | (_| |
   \\_____|\\__,_|\\___||___/___/_|_| |_|\\__, |
   / ____|                             __/ |
  | |  __  __ _ _ __ ___   ___        |___/ 
  | | |_ |/ _` | '_ ` _ \\ / _ \\             
  | |__| | (_| | | | | | |  __/             
   \\_____|\\__,_|_| |_| |_|\\___|             
                                           
                                           """)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

# Choose difficulty and set the number of attempts based on the choice
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    game(10)  # Start the game with 10 attempts for easy mode
elif difficulty == "hard":
    game(5)  # Start the game with 5 attempts for hard mode
else:
    print("Invalid difficulty choice. Please restart and choose 'easy' or 'hard'.")