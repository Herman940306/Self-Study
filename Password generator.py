import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters  # Contains a-z and A-Z
    numbers = string.digits  # Contains 0-9
    symbols = string.punctuation  # Contains !@#$%^&*()_+{}|:"<>?-=[];',./`~

    # Create a pool of characters based on user preferences
    char_pool = ""
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    # Check if at least one character set is selected
    if not char_pool:
        return "Error: Please select at least one character set (letters, numbers, or symbols)."

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Main program
if __name__ == "__main__":
    # Get user input for password length
    length = int(input("Enter the desired password length: "))

    # Get user preferences for character sets
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"Generated Password: {password}")