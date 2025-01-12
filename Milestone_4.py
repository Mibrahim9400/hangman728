import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initializes the game with a list of possible words and a specified number of lives."""
        self.word_list = word_list
        self.secret_word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.secret_word]
        self.num_unique_letters = len(set(self.secret_word))  # Count unique letters in the word
        self.num_lives = num_lives
        self.guesses_made = []

    def _is_guess_valid(self, guess):
        """Checks if the guessed character is valid (single letter and not repeated)."""
        return len(guess) == 1 and guess.isalpha() and guess not in self.guesses_made

    def _update_word_guessed(self, guess):
        """Updates the guessed word with the correct letters for the given guess."""
        for index, letter in enumerate(self.secret_word):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_unique_letters -= 1  # Reduce unique letters count when the guess is correct

    def _decrease_lives(self, guess):
        """Reduces the number of lives when a guess is incorrect."""
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _check_game_over(self):
        """Checks whether the game is over, either because the player has lost or guessed the word."""
        if self.num_lives == 0:
            print(f"Game over! The word was: {self.secret_word}")
            return True
        elif self.num_unique_letters == 0:
            print("Congratulations! You've guessed the word!")
            return True
        return False

    def _prompt_for_input(self):
        """Prompts the user for a guess, validating and processing it."""
        guess = input("Please guess a letter: ").lower()
        if not self._is_guess_valid(guess):
            print("Invalid letter. Please, enter a single alphabetical character that you haven't guessed before.")
        else:
            self.guesses_made.append(guess)
            return guess
        return None

    def play(self):
        """Runs the main game loop, asking for input and updating the game state."""
        while not self._check_game_over():
            print("Current word: ", " ".join(self.word_guessed))
            guess = None
            while guess is None:
                guess = self._prompt_for_input()
            if guess in self.secret_word:
                print(f"Good guess! {guess} is in the word.")
                self._update_word_guessed(guess)
            else:
                self._decrease_lives(guess)  # Pass guess to _decrease_lives

if __name__ == "__main__":
    word_list = ["mango", "apple", "banana", "cherry", "grapes"]
    game = Hangman(word_list)
    game.play()
