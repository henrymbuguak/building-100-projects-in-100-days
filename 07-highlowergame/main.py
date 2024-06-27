from art import logo, vs_logo
from game_data import data
import random

def starts_with_vowel(word):
    """
    Check if a word starts with a vowel.

    Args:
    - word (str): The word to check.

    Returns:
    - bool: True if the word starts with a vowel, False otherwise.
    """
    vowels = 'aeiouAEIOU'
    return word[0] in vowels

def print_comparison(item, label):
    """
    Print a comparison statement for a given dictionary item.

    Args:
    - item (dict): The dictionary item containing 'name' and 'description' keys.
    - label (str): The label to indicate whether it's "Compare A" or "Compare B".
    """
    description = item["description"]
    article = 'an' if starts_with_vowel(str(description)) else 'a'
    country = item["country"]
    print(f"Compare {label}: {item['name']}, {article} {description}, from {country}.")

def has_more_followers(item_a, item_b, user_choice):
    """
    Determine if the user chose the item with more followers.

    Args:
    - item_a (dict): The first dictionary item.
    - item_b (dict): The second dictionary item.
    - user_choice (str): The user's choice ('a' or 'b').

    Returns:
    - bool: True if the user chose the item with more followers, False otherwise.
    """
    if user_choice == "a":
        return item_a["follower_count"] > item_b["follower_count"]
    elif user_choice == "b":
        return item_b["follower_count"] > item_a["follower_count"]
    else:
        return False

def main():
    """
    Main function to run the game comparison.

    Prints the logo, selects random items from game data,
    and prints comparison statements for the selected items.
    Repeats the process until the user makes an incorrect selection.
    """
    print(logo)
    
    score = 0
    current_item = random.choice(data)
    
    while True:
        print_comparison(current_item, 'A')
        print(vs_logo)
        next_item = random.choice(data)
        print_comparison(next_item, 'B')

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if has_more_followers(current_item, next_item, user_choice):
            score += 1
            print(f"Correct! Your current score is {score}.\n")
            current_item = current_item if user_choice == "a" else next_item
        else:
            print(f"Incorrect. Your final score is {score}. Thanks for playing!\n")
            break
    
if __name__ == "__main__":
    main()
