# Guess the Number Game

## Introduction

Welcome to the Guess the Number Game! This interactive game challenges you to guess a random number between 1 and 100. You can choose between easy mode (10 attempts) or hard mode (5 attempts) to test your skills.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Program Description

This Python program implements a classic guess the number game. It includes the following features:

- ASCII art logo for a fun introduction.
- Difficulty selection (easy or hard).
- Random number generation between 1 and 100.
- User input for guess attempts.
- Feedback messages indicating if the guess is too high or too low.
- Tracking the number of remaining attempts based on difficulty.
- Congratulatory message upon successful guess, including the number of attempts used.
- Indication of failed attempts and revealing the answer.

## How the code works

The code is divided into several functions:

- `print_logo()`: Displays the cool ASCII art logo at the beginning of the game.
- `get_difficulty()`: Prompts the user to choose their difficulty level (easy or hard) and validates the input.
- `get_guess()`: Asks the user to enter their guess and ensures it's a valid number between 1 and 100.
- `play_game()`: This is the core function that runs the entire game loop. It handles difficulty selection, generating the random number, tracking turns, providing guess feedback, and ending the game with congratulations or revealing the answer if attempts are exhausted.

## How to Run the Code

Follow these steps to run the Calculator Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/06-guess-number` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```
1. Follow On-Screen Prompts.

## Example Usage

Here's an example of how the game might play out in easy mode:

```sh
 _______  __   __  _______  _______  _______   _______  __   __  _______   __    _  __   __  __   __  _______  _______  ______   
|       ||  | |  ||       ||       ||       | |       ||  | |  ||       | |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
|    ___||  | |  ||    ___||  _____||  _____| |_     _||  |_|  ||    ___| |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
|   | __ |  |_|  ||   |___ | |_____ | |_____    |   |  |       ||   |___  |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
|   ||  ||       ||    ___||_____  ||_____  |   |   |  |       ||    ___| |  _    ||       ||       ||  _   | |    ___||    __  |
|   |_| ||       ||   |___  _____| | _____| |   |   |  |   _   ||   |___  | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_______||_______||_______|   |___|  |__| |__||_______| |_|  |__||_______||_|   |_||_______||_______||___|  |_|

Choose difficulty (easy/hard): easy
You have 10 attempts remaining. Guess the number: 50
Too low. Aim a bit higher!
You have 9 attempts remaining. Guess the number: 75
Too high. Try a lower number!
You have 8 attempts remaining. Guess the number: 62
Too high. Try a lower number!
... (continues until the user guesses the number or runs out of attempts)
Congratulations! You guessed the number in 7 turns.
```
Enjoy playing the Number Guessing game!
