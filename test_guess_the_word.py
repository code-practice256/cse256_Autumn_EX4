# Autumn Tuccitto
# CIS256 Spring 2025
# EX 4

# I went through way too many hoops trying to understand Git.
# I had to make an entirely new file in a new folder and start fresh.
# Hopefully there are no issues now.
import guess_the_word

# This should test the program's ability to pick randomly.
def test_random():
    words = guess_the_word.word_list()
    chosen = guess_the_word.get_random(words)
    assert chosen in words


# This will test if the guesses here match the word.
def test_correct():
    word = "fox"
    guesses = ["f", "o", "x"]
    result = guess_the_word.display_word(word, guesses)
    assert result == "fox"


# This will test if the guesses do NOT match the word.
def test_incorrect():
    word = "marble"
    guesses = ["o", "d"]
    result = guess_the_word.display_word(word, guesses)
    assert result == "______"
