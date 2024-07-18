from coffee_data import MENU

class Menu:
    """
    A class to manage the coffee machine's menu.

    Attributes:
    - menu (dict): A dictionary containing the menu items and their details.
    """
    def __init__(self):
        """
        Initialize the Menu class with the provided menu.
        """
        self.menu = MENU

    def get_cost(self, drink):
        """
        Get the cost of the specified drink.

        Args:
        - drink (str): The name of the drink.

        Returns:
        - float: The cost of the drink.
        """
        return self.menu[drink]["cost"]
