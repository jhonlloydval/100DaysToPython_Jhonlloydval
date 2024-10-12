import random  # Importing the random module to randomly select cards
from art import logo  # Assuming 'art.py' has a variable 'logo' that contains ASCII art for the game title
import os
# The possible card values in the game (Ace is 11, face cards are 10)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    """
    The main function that handles one round of the Blackjack game.
    This function deals the initial cards to both the player and the dealer, checks for Blackjack, 
    and continues the game based on player input.
    """
    
    # Print a blank space for game clarity and display the game logo
    print("\n" * 20)
    print(logo)

    # Player's cards  
    own_cards = [random.choice(cards), random.choice(cards)]  # List containing player's initial cards
    score = sum(own_cards)  # Calculate the total score
    if score > 21:  # Check if the score is over 21
        adjust_for_ace(own_cards)  # Adjust the Ace (if present) from 11 to 1 if needed
    print(f"\n         Your cards: {own_cards}, current score: {score}")

    # Dealer's cards
    dealer_cards = [random.choice(cards), random.choice(cards)]
    dealer_score = sum(dealer_cards)
    if dealer_score > 21:
        adjust_for_ace(dealer_cards)
    print(f"         Dealer's first card: {dealer_cards[0]}\n")  # Only show one dealer card

    # Check for immediate Blackjack (win conditions)
    if score == 21 and dealer_score == 21:
        print("Draw!")
        prompt()  # Ask the player if they want to play again
    elif score == 21:
        print("BLACKJACK! You win.")
        prompt()  # Ask the player if they want to play again
    elif dealer_score == 21:
        print("Dealer BLACKJACK! You lose.")
        prompt()  # Ask the player if they want to play again
    else:
        new_card_mechanics(own_cards, dealer_cards)  # Continue the game if no one has Blackjack


def new_card_mechanics(own_cards, dealer_cards):
    """
    This function handles the mechanics of asking the player whether they want to draw another card.
    It also manages the dealer's card drawing if their score is below 17.
    """
    
    # Dealer draws cards until their score reaches at least 17 (dealer rule in Blackjack)
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))  # Draw another card for the dealer
        adjust_for_ace(dealer_cards)  # Adjust for Ace if necessary

    # Ask the player if they want to draw another card
    new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if new_card == "y":
        game_mechanics(own_cards, dealer_cards)  # Continue the game if the player chooses to draw
    elif new_card == "n":
        end_game(own_cards, dealer_cards)  # End the game if the player passes


def game_mechanics(own_cards, dealer_cards):
    """
    This function adds a new card to the player's hand and checks if the game should continue or end.
    """
    
    # Player draws a new card
    own_cards.append(random.choice(cards))
    adjust_for_ace(own_cards)  # Adjust for Ace if necessary
    dealer_score = sum(dealer_cards)
    score = sum(own_cards)
    
    # Display updated hands
    print(f"          Your cards: {own_cards}, current score: {score}")
    print(f"          Dealer's first card: {dealer_cards[0]}\n")

    # Check if the game should end based on the player's score
    if score > 21:
        end_game(own_cards, dealer_cards)  # Player busts if over 21
    elif score == 21:
        end_game(own_cards, dealer_cards)  # Automatically end game if player hits exactly 21
    else:
        new_card_mechanics(own_cards, dealer_cards)  # Continue if score is less than 21


def end_game(own_cards, dealer_cards):
    """
    This function determines the final result of the game based on the player's and dealer's scores.
    """
    
    score = sum(own_cards)  # Player's final score
    dealer_score = sum(dealer_cards)  # Dealer's final score
    print(f"          Your final hand: {own_cards}, final score: {score}")
    print(f"          Computer's final hand: {dealer_cards}, final score: {dealer_score}\n")

    # Determine the outcome of the game
    if score == dealer_score:
        print("You got a draw!")
    elif score > 21:
        print("You scored more than 21. You busted. You lose!")
    elif dealer_score > 21:
        print("The dealer scored more than 21. The dealer busted. You win!")
    elif 21 >= score > dealer_score:
        print("You scored more than the dealer. You win!")
    elif 21 >= dealer_score > score:
        print("The dealer scored more than you. You lose!")
    
    prompt()  # Ask the player if they want to play again


def adjust_for_ace(hand):
    """
    Adjusts the value of Ace from 11 to 1 if the hand's total score is greater than 21.
    """
    
    # If the hand exceeds 21 and there is an Ace (value 11), change the Ace value to 1
    while sum(hand) > 21 and 11 in hand:
        ace_index = hand.index(11)  # Find the index of the Ace
        hand[ace_index] = 1  # Change the Ace value to 1


def prompt():
    """
    This function prompts the player if they want to play another round of Blackjack.
    """
    
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "y":
        game()  # Start a new game if the player says yes
    elif start == "n":
        print("Goodbye!")  # Exit if the player says no
    print(os.system("clear"))

# Start the game by calling the prompt function
prompt()