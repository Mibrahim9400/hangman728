import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with a word list and number of lives.

        Parameters:
        word_list (list): List of words to choose from.
        num_lives (int): Number of lives the player starts with.
        """
        self.word_list = word_list
        self.secret_word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.secret_word]
        self.num_unique_letters = len(set(self.secret_word))  # Number of unique letters in the word
        self.num_lives = num_lives
        self.guesses_made = []

    def _is_valid_guess(self, guess):
        """
        Checks if the guess is valid (single letter and not previously guessed).

        Parameters:
        guess (str): The letter guessed by the player.

        Returns:
        bool: True if the guess is valid, False otherwise.
        """
        return len(guess) == 1 and guess.isalpha() and guess not in self.guesses_made

    def _update_word_progress(self, guess):
        """
        Updates the guessed word with the correct letter positions for the given guess.

        Parameters:
        guess (str): The letter guessed by the player.
        """
        for index, letter in enumerate(self.secret_word):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_unique_letters -= 1  # Reduce the unique letter count when a correct guess is made

    def _decrease_lives(self, guess):
        """
        Decreases the number of lives when an incorrect guess is made.

        Parameters:
        guess (str): The incorrect guess made by the player.
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_game_over(self):
        """
        Checks if the game is over, either because the player lost or won.

        Returns:
        bool: True if the game is over, False otherwise.
        """
        if self.num_lives == 0:
            print(f"Game over! The word was: {self.secret_word}")
            return True
        elif self.num_unique_letters == 0:
            print("Congratulations! You've guessed the word!")
            return True
        return False

    def _get_user_input(self):
        """
        Prompts the user for a valid letter guess and returns it.

        Returns:
        str: The letter guessed by the player.
        """
        while True:
            guess = input("Please guess a letter: ").lower()
            if self._is_valid_guess(guess):
                self.guesses_made.append(guess)
                return guess
            else:
                print("Invalid input! Please enter a single alphabetical character that you haven't guessed before.")

    def display_current_word(self):
        """
        Displays the current state of the word with underscores for unguessed letters.
        """
        print("Current word: ", " ".join(self.word_guessed))

def play_game(word_list):
    """
    Manages the flow of the Hangman game, including prompting for guesses and checking win/loss conditions.

    Parameters:
    word_list (list): List of words to choose from for the game.
    """
    num_lives = 5  # Set the number of lives
    game = Hangman(word_list, num_lives)  # Create a game instance
    
    while True:
        game.display_current_word()  # Display the current state of the word
        
        if game._is_game_over():
            break
        
        guess = game._get_user_input()  # Get a valid guess from the player
        
        if guess in game.secret_word:
            print(f"Good guess! {guess} is in the word.")
            game._update_word_progress(guess)
        else:
            game._decrease_lives(guess)

if __name__ == "__main__":
    word_list = ["mango", "apple", "banana", "cherry", "grapes"]
    play_game(word_list)  # Start the game
