# HANGMAN PRACTICE CODING

import random
from hangman_art import logo, stages

print(logo)

word_list = ['apple', 'car', 'chair', 'computer', 'bridge', 'lake', 'airplane', 'teacher', 'ball', 'phone', 'mountain', 'cloud', 'building', 'river', 'elephant', 'bicycle', 'cat', 'dog', 'tree', 'house', 'phone', 'table', 'book', 'road', 'ocean', 'person', 'street', 'rain', 'boat', 'camera', 'sun', 'moon', 'laptop', 'keyboard', 'flower', 'guitar', 'city', 'lamp', 'jacket', 'train', 'bird', 'sand', 'cup', 'brush', 'hammer', 'blanket', 'window', 'mirror', 'door', 'chair', 'planet', 'star', 'fish']
chosen_word = random.choice(word_list)

game_over = False
correct_words = []
lives = 6

print("Word to guess: " + "_" * len(chosen_word))

while not game_over:
    print(f"\n****************************<{lives}>/6 LIVES LEFT****************************\n")

    guess = input("Enter your guess (You may guess the word): ").lower()


    if guess in correct_words:
        print(f"You already guessed \"{guess}\"")
    display = ""
    

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_words.append(guess)
        elif letter in correct_words:
            display += letter
        else:
            display += "_"
    print(display)
    
    print(stages[lives])

    if guess == chosen_word:
        game_over = True
        print(f"Wow! You guessed the word.\n****************************YOU WIN****************************")
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed \"{guess}\", it's not in the hidden word. You lose 1 life.")
        if lives == 0:
            game_over = True
            print(f"The hidden word is \"{chosen_word}\"")
            print("****************************YOU LOSE****************************")    
    if "_" not in display:
        game_over = True
        print(f"You guessed \"{chosen_word}\"")
        print("****************************YOU WIN****************************")