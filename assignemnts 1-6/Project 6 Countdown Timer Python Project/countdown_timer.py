import time

def countdown_timer():
    print("🌟 Welcome to the Countdown Timer! 🌟\n")
    
    # Get user input for countdown time
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        if total_seconds <= 0:
            print("Please enter a positive number of seconds.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    print("\nCountdown started!\n")

    # Countdown loop
    while total_seconds > 0:
        # Format the time into minutes and seconds
        minutes, seconds = divmod(total_seconds, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")  # Overwrite the same line
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1

    print("\n🎉 Time's up! Countdown finished!")

# Run the program
if __name__ == "__main__":
    countdown_timer()