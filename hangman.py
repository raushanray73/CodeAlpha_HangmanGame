import random

# List of predefined words
words = ["python", "coding", "program", "computer", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
max_attempts = 6
wrong_attempts = 0

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 wrong attempts.")

# Main game loop
while wrong_attempts < max_attempts:

    # Display current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_attempts += 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", max_attempts - wrong_attempts)

# Game over
if wrong_attempts == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)