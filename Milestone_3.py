def check_guess(guess, word):
    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    while True:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Check if the guess is a single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            # Call check_guess to check if the guess is in the word
            check_guess(guess, word)
            break  # Exit the loop after a valid guess
        else:
            # If the guess is invalid, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Example word to guess
word = "python"

# Call ask_for_input to test the code
ask_for_input(word)
