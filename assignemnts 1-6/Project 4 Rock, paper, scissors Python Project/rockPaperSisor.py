import random

def rock_paper_scissors():
    print("🌟 Welcome to Rock, Paper, Scissors! 🌟\n")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

    # Define choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").strip().lower()

        # Quit condition
        if user_choice == "quit":
            print("\nThanks for playing! Goodbye!")
            break

        # Validate user input
        if user_choice not in choices:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Computer's choice
        computer_choice = random.choice(choices)

        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("🎉 You win!")
        else:
            print("🤖 Computer wins!")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()