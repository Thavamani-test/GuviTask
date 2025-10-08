import random  # To generate a random number

print("Welcome to the Game!")  # Displaying Welcome message

# Set the range for the random number
low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

# Generate a random number within the specified range
random_number = random.randrange(low, high)

player = None  # player value is None initially
attempts = 0
for i in range(random_number):
    # random number stores the player’s current guess and keeps looping until the correct number is guessed
    player = int(input("Enter your guess: "))
    attempts += 1

    if player < low or player > high:  # tells the player the guess is out of the given input range
        print(f"Your guess is out of the range ({low}-{high}). Try again.")
    elif player < random_number:  # tells the player the guess is too low.
        print("Too low! Try again.")
    elif player > random_number:  # tells the player the guess is too high.
        print("Too high! Try again.")

    else:  # runs when the guess is correct
        print(f"Great! You guessed the number {random_number} correctly in {attempts} attempts.")
        break