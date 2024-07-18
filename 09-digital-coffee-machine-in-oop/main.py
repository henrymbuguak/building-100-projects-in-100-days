from resources_manager import Resources
from menu import Menu
from transaction import Transaction

coffee_logo = r"""
     )  (
    (   ) )
     ) ( (
  ._________.
  |         |]
  \         / 
   `-------'  
"""

class CoffeeMachine:
    """
    A class to manage the coffee machine's overall functionality.

    Attributes:
    - profit (float): The total profit made from sales.
    - machine_on (bool): The state of the coffee machine (on or off).
    - resources (Resources): An instance of the Resources class.
    - menu (Menu): An instance of the Menu class.
    - transaction (Transaction): An instance of the Transaction class.
    """
    def __init__(self):
        """
        Initialize the CoffeeMachine class.
        """
        self.profit = 0
        self.machine_on = True
        self.resources = Resources()
        self.menu = Menu()
        self.transaction = Transaction()
    
    def print_logo(self):
        """
        Print the coffee machine logo.
        """
        print(coffee_logo)
    
    def turn_off(self):
        """
        Turn off the coffee machine.
        """
        self.machine_on = False
        print("Coffee machine is now OFF.")
    
    def make_coffee(self, drink):
        """
        Make the selected coffee and deduct the resources.

        Args:
        - drink (str): The name of the drink selected by the user.
        """
        self.resources.use_resources(drink)
        print(f"Here is your {drink} ☕️. Enjoy!")
    
    def run(self):
        """
        Run the coffee machine simulation.
        """
        self.print_logo()
        print("Welcome to the Coffee Shop!")
        
        while self.machine_on:
            user_choice = input("What would you like? (espresso/latte/cappuccino/turn off): ").lower()

            if user_choice == "report":
                self.resources.print_report(self.profit)
            
            elif user_choice == "turn off":
                self.turn_off()
            
            elif user_choice in self.menu.menu:
                if self.resources.check_resources(user_choice):
                    drink_cost = self.menu.get_cost(user_choice)
                    total_inserted = self.transaction.process_coins()
                    if self.transaction.check_transaction(total_inserted, drink_cost):
                        self.profit += drink_cost
                        self.make_coffee(user_choice)
                else:
                    break  # Exit the loop if resources are not enough
            
            else:
                print("Invalid input. Please choose 'espresso', 'latte', 'cappuccino', or 'turn off'.")

if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()
