import random

print("Welcome to the number guessing game!!")

playAgain = True

while playAgain:
    print("\nGuess a number from 0 to 50")
    randomNumber = random.randint(0, 50)
    count = 0
    max_guesses = 5

    while count < max_guesses:
        try:
            guess = int(input("Enter a number from 0 to 50: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess > randomNumber:
            print("Too high!")
        elif guess < randomNumber:
            print("Too low!")
        else:
            print("That is the correct number! You win!")
            break  # Exit the guess loop

        count += 1

    if count == max_guesses and guess != randomNumber:
        print(f"Out of guesses. The correct number was {randomNumber}.")

    option = input("Would you like to play again? (Y/N): ").strip().lower()
    if option != 'y':
        playAgain = False
        print("Thanks for playing!")
