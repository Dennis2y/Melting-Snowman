# game_logic.py
import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current state of the game with the snowman stages."""
    print(STAGES[mistakes])
    word_display = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {word_display}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word.")
            mistakes += 1

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break
    else:
        print(f"You've run out of attempts! The word was: {secret_word}")
