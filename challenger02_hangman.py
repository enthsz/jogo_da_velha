import random

# List of Hangman ASCII art representations for different stages
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# List of words for the game
guess_words = ["banana", "apple", "pineapple", "watermelon", "computer", "rice", "bean"]

# Select a random word from the list
random_choice = random.choice(guess_words)

# Create a list to represent the hidden word with underscores
secret_word = ["_"] * len(random_choice)

# Initialize game variables
game_over = False
guess_count = 0  # Track incorrect guesses
guess_limit = 6  # Maximum allowed incorrect guesses

# Function to display the Hangman figure based on incorrect guesses
def display_hangman(num_incorrect_guesses):
    if num_incorrect_guesses < len(HANGMANPICS):
        print(HANGMANPICS[num_incorrect_guesses])

# Main game loop
while not game_over:
    # Display the current state of the secret word
    print("".join(secret_word))

    # Ask the player for a letter guess (convert to lowercase for consistency)
    guess_letter = input("Enter a letter: ").lower()

    if guess_letter in random_choice:
        # Check if the guessed letter is in the random choice
        for i, letter in enumerate(random_choice):
            # Update the secret word if the guessed letter is correct
            if letter != "_" and guess_letter == letter:
                secret_word[i] = letter
    else:
        # Increment the guess count and display the Hangman figure
        guess_count += 1
        display_hangman(guess_count)
        
        if guess_count == guess_limit:
            # End the game if the guess limit is reached
            game_over = True
            print("You lost the game. Try again.")
            print("The correct word was:", random_choice)

    if "".join(secret_word) == random_choice:
        # End the game and display a win message if the word is guessed
        print("Congratulations! You've guessed the word:", random_choice)
        game_over = True

    if game_over:
        # Ask if the player wants to play again and reset the game if they do
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        else:
            # Reset game variables and choose a new random word
            random_choice = random.choice(guess_words)
            secret_word = ["_"] * len(random_choice)
            game_over = False
            guess_count = 0
