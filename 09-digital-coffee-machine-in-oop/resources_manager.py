from coffee_data import MENU, resources

class Resources:
    """
    A class to manage the coffee machine's resources.

    Attributes:
    - resources (dict): A dictionary containing the amounts of each resource.
    """
    def __init__(self):
        """
        Initialize the Resources class with the provided resources.
        """
        self.resources = resources
    
    def print_report(self, profit):
        """
        Print the current resource values and profit.

        Args:
        - profit (float): The total profit made from sales.
        """
        water = self.resources["water"]
        coffee = self.resources["coffee"]
        milk = self.resources["milk"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")
    
    def check_resources(self, drink):
        """
        Check if there are enough resources to make the drink.

        Args:
        - drink (str): The name of the drink selected by the user.

        Returns:
        - bool: True if there are enough resources, False otherwise.
        """
        for ingredient in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][ingredient] > self.resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}. Please refill the resources.")
                return False
        return True
    
    def use_resources(self, drink):
        """
        Deduct the required resources to make the coffee.

        Args:
        - drink (str): The name of the drink selected by the user.
        """
        for ingredient in MENU[drink]["ingredients"]:
            self.resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
