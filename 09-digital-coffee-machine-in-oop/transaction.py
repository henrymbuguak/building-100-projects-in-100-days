class Transaction:
    """
    A class to manage the transactions in the coffee machine.
    """
    def __init__(self):
        """
        Initialize the Transaction class.
        """
        pass
    
    def process_coins(self):
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
    
    def check_transaction(self, total_inserted, drink_cost):
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
