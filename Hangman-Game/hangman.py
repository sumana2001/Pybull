# Hangman Game
#
# The classic game of Hangman.The computer picks a random word
# and the player wrong to guess it, one letter at a time.If the player
# can't guess the word in time, the little stick figure gets hanged.

# All credits to Michael Dawson to mention this code in his book -> Python for Absolute Beginners

import random
# constants
HANGMAN = (
    """
		------
		|
		|
		|
		|
		|
		|
		|
		|
		|
		----------
""",
    """
		------
		|  |
		|  O
		|
		|
		|
		|
		|
		|
		----------
""",
    """
		------
		|  |
		|  O
		| -+-
		|
		|
		|
		|
		|
		----------
""",
    """
		------
		|   |
		|   O
		| /-+-
		|
		|
		|
		|
		|
		----------
""",
    """
		------
		|   |
		|   O
		| /-+-/
		|
		|
		|
		|
		|
		----------
""",
    """
		------
		|    |
		|    O
		|  /-+-/
		|    |
		|
		|
		|
		|
		----------
""",
    """
		------
		|   |
		|   O
		| /-+-/
		|   |
		|   |
		|  |
		|  |
		|
		----------
""",
    """
		------
		|   |
		|   O
		| /-+-/
		|   |
		|   |
		|  | |
		|  | |
		|
		----------
""")

MAX_WRONG = len(HANGMAN) - 1

# feel free to change the words as per your needs

WORDS = ("CRYPTOGRAPHY", "WAVELENGTH", "CHAMPAGNE", "CONFIGURATION", "AMAZEMENT")

word = random.choice(WORDS)
# the word to be guessed (using a random word from the above tuple)

so_far = "_" * len(word)
# one dash for each letter in word to be guessed (keeps track of current progress)

wrong = 0
# number of wrong guesses player has made

used = []
# letters already guessed

# Main loop
print("\n	Welcome to Hangman. Good luck!\n")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n\n", so_far)

    # Getting the player's guess
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()
    used.append(guess)

    # Checking the Guess
    if guess in word:
        print("\nYes!", guess, "is in the word!")
        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

# Ending the Game
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit.")
