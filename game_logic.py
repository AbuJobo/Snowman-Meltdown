import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + "=" * 30)
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"Word: {display_word}")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("=" * 30 + "\n")

def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one character.\n")
            continue

        if not guess.isalpha():
            print("Please enter a letter from a to z.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        return guess

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_valid_guess(guessed_letters)

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!\n")
        else:
            mistakes += 1
            print("Wrong!\n")

    display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!\n")
    else:
        print("The snowman melted!")
        print(f"The word was: {secret_word}\n")

def ask_replay():
    while True:
        answer = input("Play again? (y/n): ").lower().strip()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.\n")