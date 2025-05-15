import random

def hangman():
    print("🌟 Welcome to Hangman! 🌟\n")
    print("You have 6 attempts to guess the word. Good luck!\n")

    # List of words to choose from
    word_list = ["python", "hangman", "challenge", "programming", "developer", "algorithm"]
    secret_word = random.choice(word_list).lower()  # Randomly select a word
    guessed_letters = []  # Track guessed letters
    attempts = 6  # Number of allowed incorrect guesses

    # Display placeholders for unguessed letters
    display_word = ["_"] * len(secret_word)

    while attempts > 0:
        # Show the current state of the word and remaining attempts
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Attempts Remaining: {attempts}")

        # Get user input
        guess = input("Enter a letter: ").strip().lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Update the display_word with the guessed letter
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        # Check if the player has won
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'!")
            break

    # If the player runs out of attempts
    if attempts == 0:
        print(f"\n❌ Game Over! The word was: '{secret_word}'.")

# Run the game
if __name__ == "__main__":
    hangman()