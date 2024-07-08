import random
def user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


def display_result(user_choice, computer_choice, winner):
    """Display the user's choice, the computer's choice, and the result."""
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")


def play_game():
    """Play multiple rounds of Rock-Paper-Scissors with score tracking."""
    user_score = 0
    computer_score = 0
    play_again = "yes"

    while play_again.lower() in ["yes", "y"]:
        u_choice = user_choice()
        c_choice = computer_choice()
        winner = determine_winner(u_choice, c_choice)
        display_result(u_choice, c_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score -> You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ")

    print("Thanks for playing! Final score -> You: {}, Computer: {}".format(user_score, computer_score))


if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_game()
