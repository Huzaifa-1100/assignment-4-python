# 🧮 Sum Calculator
# 📚 Overview

The Sum Calculator is a simple Python program that takes two integer inputs from the user and calculates their sum. It demonstrates basic input handling, type conversion, and error handling in Python. This program is perfect for beginners learning Python or anyone who needs a quick tool to add two numbers.

# 🛠️ Features

Input Validation : Ensures the user enters valid integers. If invalid input is provided, the program gracefully handles the error and exits.

Clear Output : Displays the sum with a descriptive message.

Modular Design : Encapsulates the logic in a main() function for better readability and maintainability.

# 📋 Usage
# How It Works

The program prompts the user to enter the first number.

It reads the input, validates it, and converts it to an integer.

The program then prompts the user to enter the second number and performs the same validation.

It calculates the sum of the two numbers and displays the result with a clear message.

# 🔧 Code Explanation
# Key Components

Input Validation :
The program uses try-except blocks to handle invalid inputs (e.g., non-numeric values).

If the user enters invalid data, the program prints an error message and exits gracefully.

Sum Calculation :
The two integers are added using the + operator, and the result is stored in a variable.

Output :
The result is displayed using an f-string for clarity, including both input numbers and their sum.

# Code Structure

The logic is encapsulated in the main() function, making the program modular and easy to extend.