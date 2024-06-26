import random
import os
import blackjack_art

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate and return the score of a player's hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare scores and return the result of the game."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has a blackjack. You lose!"
    elif user_score == 0:
        return "You have a blackjack. You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_blackjack():
    print(blackjack_art.logo)
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ")
    if play_again == 'y':
        clear_console()
        play_blackjack()

if __name__ == "__main__":
    play_blackjack()
