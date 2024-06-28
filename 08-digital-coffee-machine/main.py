from coffee_data import MENU, resources

coffee_logo = r"""
     )  (
    (   ) )
     ) ( (
  ._________.
  |         |]
  \         / 
   `-------'  
"""

def print_report(profit):
    """
    Print the current resource values and profit.

    Args:
    - profit (float): The total profit made from sales.
    """
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")

def process_coins():
    """
    Process the coins inserted by the user and return the total amount.

    Returns:
    - float: The total amount of money inserted by the user.
    """
    print("Please insert coins.")
    pennies = int(input("How many pennies? ")) * 0.01
    nickels = int(input("How many nickels? ")) * 0.05
    dimes = int(input("How many dimes? ")) * 0.10
    quarters = int(input("How many quarters? ")) * 0.25
    return pennies + nickels + dimes + quarters

def check_transaction(total_inserted, drink_cost):
    """
    Check if the transaction is successful.

    Args:
    - total_inserted (float): The total amount of money inserted by the user.
    - drink_cost (float): The cost of the drink selected by the user.

    Returns:
    - bool: True if the transaction is successful, False otherwise.
    """
    if total_inserted < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(total_inserted - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True

def check_resources(drink):
    """
    Check if there are enough resources to make the drink.

    Args:
    - drink (str): The name of the drink selected by the user.

    Returns:
    - bool: True if there are enough resources, False otherwise.
    """
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}. Please refill the resources.")
            return False
    return True

def make_coffee(drink):
    """
    Deduct the required resources and make the coffee.

    Args:
    - drink (str): The name of the drink selected by the user.
    """
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink} ☕️. Enjoy!")

def turn_machine_off():
    """
    Turn off the coffee machine.
    """
    global machine_on
    machine_on = False
    print("Coffee machine is now OFF.")

def main():
    """
    Main function to run the coffee machine simulation.

    - Continuously prompt the user for their choice of drink.
    - Print the current resources and profit if the user chooses "report".
    - Check resources, process coins, and make the coffee if the user selects a drink.
    - Track the profit and update the resources.
    - Allow the user to turn off the coffee machine by entering "turn off".
    """
    global profit
    global machine_on
    profit = 0
    machine_on = True

    print(coffee_logo)
    print("Welcome to the Coffee Shop!")

    while machine_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino/turn off): ").lower()

        if user_choice == "report":
            print_report(profit)
        
        elif user_choice == "turn off":
            turn_machine_off()
        
        elif user_choice in MENU:
            if check_resources(user_choice):
                drink_cost = MENU[user_choice]["cost"]
                total_inserted = process_coins()
                if check_transaction(total_inserted, drink_cost):
                    profit += drink_cost
                    make_coffee(user_choice)
            else:
                break  # Exit the loop if resources are not enough
        
        else:
            print("Invalid input. Please choose 'espresso', 'latte', 'cappuccino', or 'turn off'.")

if __name__ == "__main__":
    main()
