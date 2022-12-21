# H A N G M A N

import random
import hangman_art
import hangman_words

print(hangman_art.logo)                         #

word_list = hangman_words.word_list             #
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6                                       #
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display.append("_")
print(f' '.join(display))

already_guessed = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in already_guessed:
        print(f"You already have guessed {guess}. Try again!")
    if guess not in already_guessed:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        already_guessed.append(guess)
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])            #



# # # # # Angela's solution # # # # #

import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    if not "_" in display:
        game_is_finished = True
        print("You win.")
    print(stages[lives])



