import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

guess_the_number()
