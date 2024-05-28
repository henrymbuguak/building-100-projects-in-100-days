import random
import hangman_words
import hangman_art

# List of words
word_list = hangman_words.word_list
stages = hangman_art.stages

def choose_word(word_list):
    """Randomly choose a word from the word_list."""
    return random.choice(word_list)

def create_display(chosen_word):
    """Create a display list with underscores for each letter in the chosen_word."""
    return ["_" for _ in chosen_word]

def update_display(chosen_word, display, guess):
    """Update the display list with the guessed letter in the correct positions."""
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    return display

def main():
    chosen_word = choose_word(word_list)
    print(f'Pssst, the solution is {chosen_word}.')  # For testing purposes
    
    display = create_display(chosen_word)
    
    # TODO-1: Create a variable called 'lives' to keep track of the number of lives left.
    # Set 'lives' to equal 6.
    lives = 6
    guessed_letters = set()

    while "_" in display and lives > 0:
        print(stages[lives])
        print(f"Current word: {' '.join(display)}")
        guess = input("Guess a letter: ").lower()

        # TODO-4: If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue
        else:
            guessed_letters.add(guess)
        
        # TODO-2: If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if guess in chosen_word:
            display = update_display(chosen_word, display, guess)
        else:
            lives -= 1
            print(f"Wrong guess. You have {lives} lives left.")
        
        # TODO-3: Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    
    if "_" not in display:
        print("Congratulations! You've guessed the word.")
    else:
        print(stages[lives])
        print(f"Sorry, you've run out of guesses. The word was '{chosen_word}'. You lose.")

if __name__ == "__main__":
    main()
