# Autumn Tuccitto
# CIS256 Spring 2025
# EX 4

def word_list():
    # Here is the pre-defined list I have come up with.
    return ["pinecone", "berry", "paint", "marble", "insect", "fox"]


def get_random(words):
    import random
    # This is how random will be implemented.
    return random.choice(words)


# How the word will be displayed whether the user guessed correctly or not.
def display_word(word, guesses):
    return "".join([letter if letter in guesses else "_" for letter in word])


def word_game():
    words = word_list()
    word = get_random(words)
    guesses = []
    attempts = 3

    # As long as there are still some guesses left...
    while attempts > 0:
        display = ""
        # ... Attempts to guess the word can still be made.
        for letter in word:
            if letter in guesses:
                display += letter
            else:
                display += "_"
        print("The correct word is: ", display)

        # If there are no more underscores, the program will know the game was won.
        if "_" not in display:
            print("Congrats! You've guessed the word!")
            break

        # The user input for guesses.
        guess = input("Guess a letter: ")

        # Assuming the user guessed a letter correctly, it adds the letter to the blank space.
        if guess in word:
            guesses.append(guess)
            print("Good guess!")
        else:
            # Of course, you can only attempt so many times before you have to restart.
            attempts -= 1
            print("Incorrect guess. Too bad! Attempts left: ", attempts)

    if attempts == 0:
        print("You ran out of guesses. The word was: ", word)

if __name__ == "__main__":
    word_game()
