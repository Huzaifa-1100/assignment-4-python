import random
import string

def generate_password():
    print("🌟 Welcome to the Password Generator! 🌟\n")
    
    # Get user input for password length
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length must be at least 6 characters.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Ask the user for character preferences
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
    use_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/" if use_special else ""

    # Combine selected character pools
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if not all_characters:
        print("You must select at least one character type!")
        return

    # Generate the password
    password = "".join(random.choices(all_characters, k=length))
    print(f"\n🔒 Your generated password is: {password}")

# Run the program
if __name__ == "__main__":
    generate_password()