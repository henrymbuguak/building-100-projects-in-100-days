# Coffee Shop Simulator

Welcome to the Coffee Shop Simulator, where you can experience the functionality of a virtual coffee machine right from your terminal.

## Introduction

The Coffee Shop Simulator is a Python program that simulates the operation of a coffee machine. It allows users to select from a menu of drinks (espresso, latte, cappuccino), check available resources like water, milk, and coffee beans, process payments, and dispense the chosen drink. This simulation aims to provide a simplified experience of managing a coffee shop's operations.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Program Description

The simulator uses predefined menus and resources to simulate the operation of a coffee machine. It tracks the amount of water, milk, and coffee beans available, manages user inputs for selecting drinks, processes payments using coins, and calculates profits from each transaction.

## How the Code Works

The program works by continuously prompting the user for input:

- It displays a menu of drink options and responds to user selections.
- It checks if there are enough resources available to fulfill the order.
- It processes coins inserted by the user to ensure the correct amount is paid.
- It calculates change and updates the profit when a transaction is successful.
- It dispenses the chosen drink and updates the resources accordingly.

## How to Run the Code

Follow these steps to run the Coffee Shop Simulator Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/08-digital-coffee-machine` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```

1. Follow the prompts to select a drink, insert coins, and interact with the simulator.

## Example Usage

```shell
$ python main.py

     )  (
    (   ) )
     ) ( (
  ._________.
  |         |]
  \         / 
   `-------'  

Welcome to the Coffee Shop!

What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
How many pennies? 4
How many nickels? 3
How many dimes? 2
How many quarters? 1
Here is $0.96 in change.
Here is your espresso ☕️. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 200ml
Milk: 150ml
Coffee: 100g
Money: $2.5

What would you like? (espresso/latte/cappuccino): turn off

```

Thank you for visiting the Coffee Shop Simulator! Enjoy your coffee experience.
