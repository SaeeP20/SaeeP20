import random

def get_word():
    # Reads words.txt and splits words by whitespace - adds to array word_list
    with open("words.txt") as words:
        word_list = words.read().split()
    # Chooses a random word as hangman word
    rand_word = random.choice(word_list)

