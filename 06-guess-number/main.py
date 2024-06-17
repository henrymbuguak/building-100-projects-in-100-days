import random
import guess_art
  

def get_difficulty():
  """Gets the difficulty level (easy/hard) from the user.

  This function prompts the user to choose a difficulty level
  ('easy' or 'hard') and validates the input. It returns the chosen
  difficulty level (lowercase string).
  """
  while True:
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    if difficulty in ("easy", "hard"):
      return difficulty
    else:
      print("Invalid difficulty. Please choose 'easy' or 'hard'.")

def get_guess():
  """Gets a valid guess number (between 1 and 100) from the user.

  This function prompts the user to enter a guess number and validates
  the input. It ensures the guess is a number between 1 and 100 
  (inclusive). It returns the valid guess number as an integer.
  """
  while True:
    try:
      guess = int(input("Enter your guess (1-100): "))
      if 1 <= guess <= 100:
        return guess
      else:
        print("Guess must be between 1 and 100.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def play_game():
  """Runs the guess number game.

  This function implements the core gameplay logic. It includes:
      - Displaying the game logo
      - Getting difficulty level from the user
      - Generating a random number (answer)
      - Tracking the number of turns based on difficulty
      - Providing feedback to the user based on their guess (too high/low)
      - Keeping track of remaining attempts
      - Ending the game with congratulations or indicating failed attempts

  """
  print(guess_art.logo)
  print("Welcome to the Number Guessing Game!")
  difficulty = get_difficulty()
  total_turns = {"easy": 10, "hard": 5}[difficulty]
  answer = random.randint(1, 100)
  turns = total_turns

  while turns > 0:
    # Show remaining attempts before user guesses
    print(f"You have {turns} attempts remaining. Guess the number:")
    guess = get_guess()
    turns -= 1

    if guess == answer:
      print(f"Congratulations! You guessed the number in {total_turns - turns} turns.")
      return

    if guess < answer:
      if difficulty == "easy":
        print(f"Too low. Aim a bit higher!")
      else:
        print(f"Too low. You're getting close!")
    else:
      if difficulty == "easy":
        print(f"Too high. Try a lower number!")
      else:
        print(f"Too high. Be careful not to overshoot!")

  print(f"You ran out of guesses! The answer was {answer}.")

if __name__ == "__main__":
  """Starts the guess number game."""
  play_game()
