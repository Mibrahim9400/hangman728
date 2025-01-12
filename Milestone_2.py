# Step 1: Importing the random module
import random

# Step 2: Chosing a random word from list using a define function
def get_random_word_from_list(word_list):
    return random.choice(word_list)

# Step 3: Validating iser input using a define function
def validate_user_input(guess):
    if len(guess) == 1 and guess.isalpha():
        return True
    return False

# Step 2: Assigning this list to a variable called word_list.
word_list = ["Mango", "Apple", "Banana", "Cherry", "Grapes"]

# Step 3: Using Random.choice method to choose random word from the word_list,
word = get_random_word_from_list(word_list)

# Step 4: Print out the newly created list to the standard output.
print(f"Selected word: {word}")

# Step 5: Ask the user to enter a single letter.
guess = input("Enter a single letter: ")

# Step 6: Validate the user input.
if validate_user_input(guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")