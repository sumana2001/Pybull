# Hangman Game

Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters within a certain number of guesses.

### Game play 👾
Computer selects a word randomly; the others try to guess using letters one letter at a time. The computer draws a number of dashes equivalent to the number of letters in the word. If a guessing player suggests a letter that occurs in the word, the computer fills in the blanks with that letter in the right places. If the word does not contain the suggested letter, the computer draws one element of a hangman’s gallows. As the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word. The number of incorrect guesses before the game ends is up to the players, but completing a character in a noose provides a minimum of seven wrong answers until the game ends.

### Objective 🎯 💯
Guess the word/phrase before your man gets hung!

### Code explained 📝
I have defined a tuple of words, one of them is selected randomly by the computer and we need to guess the word within 7 incorrect attempts.
**Used[]** is a list which stores the letters that the user has already guessed.

**Note:** 😎
A good acronym to commit to memory is: ETAOIN SHRDLU. It’s hard to pronounce, yes, but its order denotes the most commonly used letters (in order) in the English language.
