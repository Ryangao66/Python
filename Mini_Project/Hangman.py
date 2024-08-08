import random

def hangman():
    words = ["python", "hangman", "challenge", "programming", "computer"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    guessed_word = ["_"] * len(word)

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you lost! The word was: {word}")

# Run the game
hangman()
