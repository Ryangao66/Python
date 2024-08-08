import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    low = 1
    high = 100

    while True:
        guess = input(f"Guess a number between {low} and {high}: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < low or guess > high:
            print(f"Your guess is out of bounds! It must be between {low} and {high}.")
        elif guess < secret_number:
            print("Too low!")
            low = guess + 1
        elif guess > secret_number:
            print("Too high!")
            high = guess - 1
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
number_guessing_game()
