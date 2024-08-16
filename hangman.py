import random

def get_word():
    # Reads words.txt and splits words by whitespace - adds to array word_list
    with open("words.txt") as words:
        word_list = words.read().split()
    # Chooses a random word as hangman word
    return random.choice(word_list)

def get_hangman(tries):
    stage = [    
        """
            |
            |
            |
            |
            | """,
        """
            |
            |
            |
            |
            |
        ====== """,
        """
        _____
            |
            |
            |
            |
            |
        ====== """,
        """
        _____
           \|
            |
            |
            |
            |
        ====== """,
        """
        _____
        |  \|
            |
            |
            |
            |
        ======""",
        """
        _____
        |  \|
        O   |
            |
            |
            |
        ======"""]
    return stage[tries - 1]

def guesses(guess):
    guess_list = []
    if guess not in guess_list:
        guess_list.append(guess)
    else:
        print("You have already guessed this letter!")

def play_game():
    word = get_word()
    guess = input("Enter your guess: ")
    cor_guesses = []
    incor_guesses = []
    if len(guess) != 1:
        print("Please enter a valid input.")
    else:
        guesses(guess)
