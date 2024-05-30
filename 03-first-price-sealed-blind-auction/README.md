# First-Price Sealed-Bid Auction Program

## Introduction

This Python program simulates a simplified version of a [first-price sealed-bid auction](https://en.wikipedia.org/wiki/First-price_sealed-bid_auction). In this type of auction, all bidders submit their bids without knowing the bids of other participants. The highest bidder wins and pays the amount they bid. This program provides a basic framework for understanding how a first-price sealed-bid auction operates.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Program Description

This program allows multiple users to participate in a first-price sealed-bid auction. Each user enters their name and bid amount. The program then determines the highest bidder and announces the winner along with the winning bid amount.

## How the Code Works

1. Introduction and Setup:

    - The program displays a welcome message along with an ASCII art logo (imported from blind_action_art). 

1. Bid Collection:

    - The program prompts each user to enter their name and bid amount.
    - Users are asked if there is another bidder. If yes, the screen clears, and the next bidder can input their details. If no, the auction ends.

1. Determine the Winner:

    - The program evaluates all bids and determines the highest bidder.
    - It then announces the winner and their bid amount.

## Run the Program

1. Open your terminal or command prompt.
1. Navigate to the directory where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```

1. Follow the on-screen prompts to enter bidder names and bid amounts.
1. After all bids are entered, the program will announce the winner.

## Example Usage

```sh
$ python main.py
Welcome to the First-price sealed-bid auction
Enter your name: Alice
Enter your bid amount $: 300
Is there another bidder? (yes/no): yes
Enter your name: Bob
Enter your bid amount $: 450
Is there another bidder? (yes/no): yes
Enter your name: Charlie
Enter your bid amount $: 350
Is there another bidder? (yes/no): no
The winner is Bob with a bid of $450
```

By following these steps, you can successfully run the first-price sealed-bid auction program and understand its basic functionality.
