import random

# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")
# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    # counts the number of times a user fails
    failed = 0
    for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:

        print("You Win")
        print("The word is: ", word)
        break

    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
