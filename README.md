# Rock, Paper, Scissors Game

This is a simple command-line implementation of the classic game Rock, Paper, Scissors. The user plays against the computer, and the winner is determined based on the traditional rules of the game.

## How to Play

1. Run the game script.
2. When prompted, enter your choice: "rock", "paper", or "scissors".
3. The computer will randomly select its choice.
4. The winner will be displayed based on the game rules.

## Rules

- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.
- If both choices are the same, it's a tie.

## Files

- `rock_paper_scissors.py`: The main script to run the game.
- `README.md`: This file, providing an overview of the game and instructions.

## Example Usage

```bash
python rock_paper_scissors.py

Code Explanation
Functions
get_user_choice()

Prompts the user to enter their choice (rock, paper, or scissors).
Validates the input to ensure it's one of the allowed options.
Returns the user's choice.
get_computer_choice()

Randomly selects one of the three options for the computer's choice.
Returns the computer's choice.
determine_winner(user_choice, computer_choice)

Compares the user's choice with the computer's choice to determine the winner.
Prints the result (Tie, User won, or AI won).
play_game()

Main function to start the game.
Calls the above functions to get choices and determine the winner.
Prints the choices and the result.
