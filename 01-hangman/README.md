# Hangman Game

This Python program implements a simple version of the [classic hangman game](https://en.wikipedia.org/wiki/Hangman_(game)). The user tries to guess a randomly chosen word by suggesting letters within a certain number of attempts. For each incorrect guess, a part of a hangman is drawn. The game ends when the user either correctly guesses the word or runs out of guesses, resulting in the completion of the hangman drawing.

The program includes:

- A list of possible words to guess.
- Visual representation of the hangman in ASCII art.
- Logic to handle user guesses, track guessed letters, and manage the number of lives (attempts) left.
- Feedback to the user about their guesses and the state of the game.

## How to Set Up and Run the Code

### Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

### Steps to Create a Python 3.12 Virtual Environment

1. Open a terminal (or command prompt).
1. Navigate to the directory where you want to create your virtual environment.

    ```shell
    cd /path/to/your/project
    ```

1. Create a virtual environment.

    ```shell
    python3.12 -m venv hangman_env
    ```

1. Activate the virtual environment.

    - On Windows:

        ```shell
        hangman_env\Scripts\activate
        ```

    - On macOS/Linux:

        ```shell
        source hangman_env/bin/activate
        ```
    

### Steps to Run the Code

1. Ensure you have the virtual environment activated. (See step 4 above)
1. Run the code.

    ```shell
    python main.py
    ```

## Game Play

The program will randomly select a word from the predefined list.
You will be prompted to guess letters one by one.
Correct guesses will reveal the letter in the word.
Incorrect guesses will result in the drawing of a hangman. You have 6 incorrect guesses before the game ends.
The game will provide feedback if you have already guessed a letter.
The game continues until you either guess the word correctly or run out of guesses.

Enjoy playing the hangman game!