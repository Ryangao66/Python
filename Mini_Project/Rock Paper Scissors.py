import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")

    # Options for the game
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get the player's choice
        player_choice = input("Your choice: ").lower()

        # Check if the input is valid
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Get the computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Run the game
rock_paper_scissors()
