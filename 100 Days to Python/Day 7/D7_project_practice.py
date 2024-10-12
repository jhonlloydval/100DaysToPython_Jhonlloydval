# DAY 7 PROJECT
# HANGMAN GAME

import random

# LIST OF WORDS
# word_list = list(map(str, input("Input words separated by spaces: ").split()))
word_list = ['apple', 'car', 'chair', 'computer', 'bridge', 'lake', 'airplane', 'teacher', 'ball', 'phone', 'mountain', 'cloud', 'building', 'river', 'elephant', 'bicycle', 'cat', 'dog', 'tree', 'house', 'phone', 'table', 'book', 'road', 'ocean', 'person', 'street', 'rain', 'boat', 'camera', 'sun', 'moon', 'laptop', 'keyboard', 'flower', 'guitar', 'city', 'lamp', 'jacket', 'train', 'bird', 'sand', 'cup', 'brush', 'hammer', 'blanket', 'window', 'mirror', 'door', 'chair', 'planet', 'star', 'fish']

# LIVES 
lives = 6

# GENERATE A RANDOM WORD
hidden_word = random.choice(word_list)
print(hidden_word)

# REMAINING LETTERS
remaining_letters = len(hidden_word)

# GENERATE BLANKS AS MANY AS LETTERS IN WORD
blank_word = "_ " * len(hidden_word)
print(blank_word)

# ASK THE USER TO GUESS A LETTER

# GUESS CHECKER FUNCTION
def guess_check(guess):
    global remaining_letters
    global lives
    lives_for_now = 0
    for letter in hidden_word:
        if letter == guess:
            letter = guess + " "
            remaining_letters -= 1
            lives_for_now += 1
        else:
            letter = "_ "
        print(letter, end="")
    
    if lives_for_now == 0:
        lives -= 1

# MAIN FUNCTION

while lives != 0 and remaining_letters != 0:
    guess = input("\nGuess a letter: ").lower()
    guess_check(guess)
