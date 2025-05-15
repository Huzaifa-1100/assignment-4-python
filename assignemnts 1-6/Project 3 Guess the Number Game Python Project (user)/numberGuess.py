import random

def guess_the_number_user():
    print("🌟 Welcome to the Guess the Number Game (User Edition)! 🌟\n")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    input("Press Enter when you're ready...")

    # Set the range for guessing
    low = 1
    high = 100
    attempts = 0

    while True:
        # Computer guesses a number in the current range
        guess = random.randint(low, high)
        attempts += 1

        # Ask the user for feedback
        feedback = input(f"\nIs your number {guess}? (Enter 'correct', 'too high', or 'too low'): ").strip().lower()

        if feedback == "correct":
            print(f"\n🎉 I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == "too high":
            high = guess - 1  # Adjust the upper bound
        elif feedback == "too low":
            low = guess + 1  # Adjust the lower bound
        else:
            print("Invalid input! Please enter 'correct', 'too high', or 'too low'.")
            attempts -= 1  # Don't count invalid attempts

        # Check if the range becomes invalid
        if low > high:
            print("\nHmm, it seems like you gave me conflicting feedback. Let's try again!")
            break

# Run the game
if __name__ == "__main__":
    guess_the_number_user()