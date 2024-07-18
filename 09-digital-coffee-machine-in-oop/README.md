# Coffee Machine Simulation with OOP

This project demonstrates a coffee machine simulation using Object-Oriented Programming (OOP) principles in Python. It features a menu with various coffee options, resource management, and transaction processing, all structured in a modular and maintainable way.

## Introduction

The coffee machine simulation showcases the power of OOP by dividing the program into distinct classes responsible for different aspects of the machine. Users can select coffee options, check resources, insert coins, and receive their drinks while the program tracks resources and profit.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.
- Basic understanding of Python and OOP concepts

## Program Description

The program simulates a coffee machine where users can:

- Select from espresso, latte, and cappuccino
- Check resource availability
- Insert coins
- Receive their selected drink

The machine keeps track of resources and profit, providing a report on demand.

## How the Code Works

The program is organized into four main classes:

- **Resources**: Manages the coffee machine's resources, prints reports, and checks resource availability.
- **Menu**: Handles the menu items and retrieves the cost of selected drinks.
- **Transaction**: Manages the transaction process, including coin insertion and transaction validation.
- **CoffeeMachine**: Integrates the other classes and manages the overall functionality of the coffee machine, including user interactions.

Each class is defined in its own module and imported into the main script (`main.py`) to ensure a clean and modular structure.

## How to Run the Code

Follow these steps to run the Coffee Shop Simulator Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/09-digital-coffee-machine-in-oop` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```

1. Follow the prompts to select a drink, insert coins, and interact with the simulator.

## Example Usage

When you run the program, you will see the following prompt:

```shell
Welcome to the Coffee Shop!
What would you like? (espresso/latte/cappuccino/turn off): 
```

Type one of the options (e.g., "latte") to order a drink, or "report" to see the current resources and profit. Type "turn off" to shut down the coffee machine.

By following these steps and understanding the code structure, you can effectively interact with and modify the coffee machine simulation. Enjoy exploring the power of OOP with this practical project!
