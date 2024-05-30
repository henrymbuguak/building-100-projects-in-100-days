import os
import blind_action_art

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bid():
    """Get a bid from the user."""
    name = input("Enter your name: ")
    bid = float(input("Enter your bid amount $: "))
    return name, bid

def add_bid(bids, name, bid):
    """Add a bid to the bids dictionary."""
    bids[name] = bid

def determine_winner(bids):
    """Determine the winner from the bids dictionary."""
    if not bids:
        return None, 0
    winner = max(bids, key=bids.get)
    winning_bid = bids[winner]
    return winner, winning_bid

def main():
    print(blind_action_art.logo)
    print("Welcome to the First-price sealed-bid auction")
    bids = {}
    while True:
        name, bid = get_bid()
        add_bid(bids, name, bid)
        
        another_bidder = input("Is there another bidder? (yes/no): ").strip().lower()
        if another_bidder == 'yes':
            clear_screen()
        else:
            break
    
    winner, winning_bid = determine_winner(bids)
    if winner:
        print(f"The winner is {winner} with a bid of ${winning_bid}")
    else:
        print("No bids were placed.")

# Run the auction program
if __name__ == "__main__":
    main()
