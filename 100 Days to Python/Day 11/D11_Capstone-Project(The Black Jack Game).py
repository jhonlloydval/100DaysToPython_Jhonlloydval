# This is the first Capstone Project on Angela Yu's 100 days to python bootcamp
# Started on October 10, 2024

# THE BLACK JACK GAME

import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    # OWN CARDS ONE BY ONE
    print("\n"*20)
    print(logo)

    first_card = random.choice(cards) 
    second_card = random.choice(cards) 
    own_cards = [first_card, second_card]
    score = sum(own_cards)
    if score > 21:
        adjust_for_ace(own_cards)
    print(f"\n         Your cards: {own_cards}, current score: {score}")

    # ENEMY CARDS
    dealer_first_card = random.choice(cards) 
    dealer_second_card = random.choice(cards)
    dealer_cards = [dealer_first_card, dealer_second_card]
    dealer_score = sum(dealer_cards)
    if dealer_score > 21:
        adjust_for_ace(dealer_cards)
    print(f"         Dealer's first card: {dealer_cards[0]}\n")

    # BLACKJACK
    if score == 21 and dealer_score == 21:
        print("Draw!")
        prompt()
    elif score == 21:
        print("BLACKJACK! You win.")
        prompt()
    elif dealer_score == 21:
        print("Dealer BLACKJACK! You lose.")
        prompt()
    else:
        new_card_mechanics(own_cards, dealer_cards)

def new_card_mechanics(own_cards, dealer_cards):

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        adjust_for_ace(dealer_cards)

    new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if new_card == "y":
        game_mechanics(own_cards, dealer_cards) 
    elif new_card == "n":
        end_game(own_cards, dealer_cards)

def game_mechanics(own_cards, dealer_cards):

    own_cards.append(random.choice(cards))
    adjust_for_ace(own_cards)
    dealer_score = sum(dealer_cards)
    score = sum(own_cards)
    
    print(f"          Your cards: {own_cards}, current score: {score}")
    print(f"          Dealer's first card: {dealer_cards[0]}\n")

    if score > 21:
        end_game(own_cards, dealer_cards)
    if score == 21:
        end_game(own_cards, dealer_cards)
    if score < 21:
        new_card_mechanics(own_cards, dealer_cards)


def end_game(own_cards, dealer_cards):
    score = sum(own_cards)
    dealer_score = sum(dealer_cards)
    print(f"          Your final hand: {own_cards}, final score: {score}")
    print(f"          Computer's final hand: {dealer_cards}, final score: {dealer_score}\n")

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
    prompt()
    
def adjust_for_ace(hand):
    while sum(hand) > 21 and 11 in hand:
        ace_index = hand.index(11)
        hand[ace_index] = 1

def prompt():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "y":
        game()
    elif start == "n":
        print("Good bye!")


prompt()

