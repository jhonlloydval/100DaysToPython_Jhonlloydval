# GUESSING GAME ni PANCIPANE
import random

randy = random.randint(1,100)
no_guess = 0

def condition1():
    global no_guess
    if no_guess == 4:
        if randy%2 == 0:
            print("Randy is an even number.")
        else:
            print("Randy is an odd number.")

def condition2():
    global no_guess
    if no_guess == 5:
        if randy%10 < 5:
            print


while True:
    guess = int(input("Enter your guess: "))
    no_guess += 1
    condition1()
    if guess != randy:
        if randy > guess:
            print("Enter a higher number")
        else: 
            print("Enter a lower number")
    else:
        print(f"You guessed {randy}. You win!")


