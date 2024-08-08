import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)

    # Keep track of the number of guesses
    attempts = 0

    while True:
        # Ask the player for their guess
        guess = input("Take a guess: ")

        # Make sure the input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert the input to an integer
        guess = int(guess)
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guess_the_number()
