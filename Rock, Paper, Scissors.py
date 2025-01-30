import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Function to get the player's choice
def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    print("Welcome to Rock Paper Scissors!")
    
    while True:
        # Get choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        # Print choices
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and print the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Thanks for playing!")

# Start the game
play_game()