import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if user_choice == 'stone':
        return "You win!" if computer_choice == 'scissor' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'stone' else "Computer wins!"
    elif user_choice == 'scissor':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def play_game():
    print("Stone Paper Scissor Game")
    print("-" * 30)
    
    while True:
        user_choice = input("\nEnter your choice (stone/paper/scissor) or 'quit' to exit: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in ['stone', 'paper', 'scissor']:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()