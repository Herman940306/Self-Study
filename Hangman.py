import random

# List of words to choose from
words = ["python", "programming", "computer", "science", "algorithm", "database", "network"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main game function
def hangman():
    # Choose a random word
    secret_word = choose_word()
    
    # Initialize variables
    guessed_letters = set()
    attempts_left = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    
    # Main game loop
    while attempts_left > 0:
        # Display current state of the word
        print("\nWord:", display_word(secret_word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print("Guessed letters:", ", ".join(guessed_letters))
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guessed letter to the set
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in secret_word:
            print("Good guess!")
            
            # Check if the player has won
            if set(secret_word) <= guessed_letters:
                print(f"\nCongratulations! You've guessed the word: {secret_word}")
                return
        else:
            print("Wrong guess!")
            attempts_left -= 1
    
    # Game over
    print(f"\nGame over! The word was: {secret_word}")

# Start the game
hangman()