import random

# Predefined list of words
words = ["apple", "banana", "cherry", "grape", "orange"]

# Randomly choose a word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(word))  # Blank spaces for the word

# Game loop
while incorrect_guesses < max_attempts:
    guess = input("\nGuess a letter: ").lower()

    # Check for valid single letter
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess in word
    if guess in word:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    # Display current state of the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check if player won
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"\n💀 Game Over! The word was '{word}'.")
