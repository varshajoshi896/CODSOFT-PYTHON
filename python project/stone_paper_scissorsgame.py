import random

def get_user_choice():
    while True:
        print("\nChoose Rock, Paper, or Scissors:")
        choice = input("Your choice: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("=== Welcome to Rock-Paper-Scissors Game ===")

    while True:
        print(f"\n--- Round {round_number} ---")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose: {user.capitalize()}")
        print(f"Computer chose: {computer.capitalize()}")

        result = determine_winner(user, computer)
        if result == "win":
            print("You win this round!")
            user_score += 1
        elif result == "lose":
            print("Computer wins this round.")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

# Run the game
play_game()

