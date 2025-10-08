import random

# List of words
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Randomly choose a word from the list
original_word = random.choice(words)

# Scramble the chosen word
scrambled_word = ''.join(random.sample(original_word, len(original_word)))

print("Welcome to the Game!")
print(f"This is your scrambled word: {scrambled_word}")

# Allow multiple attempts
attempts = 0
for i in original_word :

    player_guess = input("Enter your guess: ").lower()
    attempts += 1

    # Check if guess is correct
    if player_guess == original_word:
        print(f"Correct! The word is '{original_word}'.")
        print(f"You guessed it in {attempts} attempt(s)!")
        break
    else:
        print("Wrong guess. Try again!")
