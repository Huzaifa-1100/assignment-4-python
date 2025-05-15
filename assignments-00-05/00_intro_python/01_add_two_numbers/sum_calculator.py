def main():
    # Step 1: Prompt the user to enter the first number
    try:
        # Ask the user for input and convert it to an integer
        num1 = int(input("Enter the first number: "))
    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        print("Invalid input! Please enter a valid integer.")
        return  # Exit the function if input is invalid

    # Step 2: Prompt the user to enter the second number
    try:
        # Ask the user for input and convert it to an integer
        num2 = int(input("Enter the second number: "))
    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        print("Invalid input! Please enter a valid integer.")
        return  # Exit the function if input is invalid

    # Step 3: Calculate the sum of the two numbers
    # Add the two integers and store the result in a variable
    total_sum = num1 + num2

    # Step 4: Print the total sum with an appropriate message
    # Display the result in a clear and descriptive format
    print(f"The sum of {num1} and {num2} is: {total_sum}")


# Run the program
if __name__ == "__main__":
    # Call the main() function to start the program
    main()