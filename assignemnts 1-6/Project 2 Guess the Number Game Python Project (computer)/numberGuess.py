import random

def guess_the_number():
    print("🌟 Welcome to the Guess the Number Game! 🌟\n")
    print("I'm thinking of a number between 1 and 10. Can you guess what it is?")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()