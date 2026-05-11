import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: -")

    print("Mistakes:", mistakes)
    print()

def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!\n")
        else:
            mistakes += 1
            print("Wrong!\n")

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!")
    else:
        print("The snowman melted!")
        print("The word was:", secret_word)