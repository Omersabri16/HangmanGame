import random
import hangman_art
from hangman_words import word_list
from hangman_art import logo
from hangman_art import welcome

print(welcome)
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)  # Test için, gerçek oyunda kaldırabilirsin

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6


while not game_over:

    print(f"*******************{lives}/6 LIVES LEFT*******************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess : " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")

        if lives == 0:
            print(f"*******************IT WAS {chosen_word}! YOU LOSE*******************")
            game_over = True

    if "_" not in display:
        print("*******************YOU WIN*******************")
        game_over = True

    print(hangman_art.stages[lives])
