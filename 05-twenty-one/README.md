# Blackjack Game

## Introduction

This Blackjack game, implemented in Python, allows you to play a simplified version of the popular card game against the computer. The game follows standard Blackjack rules and provides a text-based interface for interaction.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Program Description

The Blackjack game consists of several key functions:

- `deal_card()`: Returns a random card from the deck.
- `calculate_score(cards)`: Calculates and returns the score of a player's hand.
- `compare(user_score, computer_score)`: Compares the user's and computer's scores to determine the game result.
- `clear_console()`: Clears the console for a better user experience.
- `play_blackjack()`: Main function to handle the game logic and user interaction.

## How the Code Works

1. The game starts by displaying the game logo.
1. Both the user and the computer are dealt two cards.
1. The user can choose to draw additional cards or pass.
1. The computer draws cards until its score is at least 17.
1. The scores are compared, and the result is displayed.
1. The user can choose to play again or exit the game.

## How to Run the Code

Follow these steps to run the Calculator Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/05-twenty-one` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```
1. Follow On-Screen Prompts.

## Example Usage

When you run the script, you will see the game logo and be prompted to start the game. Follow the on-screen instructions to play. Here's an example interaction:

```sh
.------.            _     _            _    
|A_  _ |.          | |   | |          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\
      |  \/ K|                            
      `------'                            
Your cards: [9, 7], current score: 16
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
Your final hand: [9, 7, 5], final score: 21
Computer's final hand: [10, 7], final score: 17
You win!
Do you want to play again? Type 'y' for yes or 'n' for no: n
```

Enjoy playing the Blackjack game!

