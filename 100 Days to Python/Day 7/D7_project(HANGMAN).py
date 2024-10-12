import random
from hangman_words import  word_list
from hangman_art import stages, logo



print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:

    print(f"\n****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed the letter {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"\nYou guessed \"{guess}\", it's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"\n***********************YOU LOSE**********************")
            print(f"The hidden word is: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("\n****************************YOU WIN****************************")

    print(stages[lives])

