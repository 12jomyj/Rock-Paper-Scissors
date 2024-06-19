import random

def get_user_choice():
    while True:
        try:
            user_choice = input("Enter rock, paper or scissors: ")
            if user_choice not in ["rock", "paper", "scissors"]:
                raise ValueError("Please make a valid selection")
            return user_choice
        except ValueError as e:
            print(e)

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("User won")
    else:
        print("AI won")

# driver function
def play_game():
    print("Lets play rock paper scissors")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer's choice : {computer_choice}")
    print(f"user's choice : {user_choice}")
    determine_winner(user_choice, computer_choice)

# play the game 
play_game()