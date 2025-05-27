import random

secret_num = random.randint(1, 100)
guess = None

print("Guess the number (between 1 and 100):")

while guess != secret_num:
    guess = int(input("Your guess: "))
    if guess < secret_num:
        print("Too Low! Try again.")
    elif guess > secret_num:
        print("Too High! Try again.")
    else:
        print("Correct! You guessed the number.")
