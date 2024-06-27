# Higher Lower Game

Welcome to the Higher Lower Game! This is a simplified version of the [Higher Lower Game](https://www.higherlowergame.com/).

## Introduction

The Higher Lower Game challenges you to guess which of two options has more followers. Test your knowledge and see how high you can score!


- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Program Description

This program displays two items with their descriptions and asks the player to guess which item has more followers. The player scores a point for each correct guess and the game continues until the player makes an incorrect guess.

## How the Code Works

1. **Imports**: The code imports the necessary libraries and modules (`random`, `logo`, `vs_logo`, `data`).
1. **Functions**:

    - `starts_with_vowel(word)`: Checks if a word starts with a vowel.
    - `print_comparison(item, label)`: Prints the comparison statement for a given item.
    - `has_more_followers(item_a, item_b, user_choice)`: Determines if the user chose the item with more followers.

1. Main Function:

    - Prints the game logo.
    - Randomly selects two items to compare.
    - Asks the user to choose which item has more followers.
    - Updates the score if the user is correct and continues the game.
    - Ends the game if the user makes an incorrect choice and prints the final score.

## How to Run the Code

Follow these steps to run the Calculator Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/07-highlowergame` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```

1. Follow On-Screen Prompts.

## Example Usage

When you run the game, you will see something like this:

```shell
 _    _ _       _               
| |  | (_)     | |              
| |__| |_  __ _| |__   ___ _ __ 
|  __  | |/ _` | '_ \ / _ \ '__|
| |  | | | (_| | | | |  __/ |   
|_|  |_|_|\__, |_| |_|\___|_|   
          __/ |                 
         |___/                  
                                

Compare A: Instagram, a social media platform
 _    _ _            __  
| |  | (_)          / _| 
| |  | |_ _ __ __ _| |_  
| |/\| | | '__/ _` |  _| 
\  /\  / | | | (_| | |   
 \/  \/|_|_|  \__,_|_|   
                         

Compare B: TikTok, a video-sharing platform

Who has more followers? Type 'A' or 'B': 

```

Enjoy testing your knowledge of follower counts!
