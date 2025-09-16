import random

def number_guessing_game():
    """
    A number guessing game. The computer will generate a random number between 1 and 100, and the user will have 7 attempts to guess the number.

    After each guess, the computer will give a hint if the guess is too low or too high. If the user guesses the number within the 7 attempts, the computer will congratulate the user and end the game. If the user does not guess the number within the 7 attempts, the computer will tell the user that they have run out of attempts and what the number was.
    number = random.randint(1, 100)
    attempts = 7

    print("Guess the number between 1 and 100")
    """

    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}/{attempts}: "))
        if guess == number:
            print("🎉 Correct! You guessed it!")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    print(f"Out of attempts! The number was {number}.")
    

if __name__ == "__main__":
    number_guessing_game()
