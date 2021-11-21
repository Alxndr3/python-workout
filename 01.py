from random import randint


def guessing_game():
    new_num = randint(0, 100)
    tries = 1

    while tries < 4:
        try:
            guess = int(input("Insert your guess: "))
            if new_num == guess:
                print("Just right!")
                break
            if new_num > guess:
                print("Too low.")
            else:
                print("Too high.")
        except:
            print("Insert an integer number from 0 to 100: ")
            continue
        tries += 1
        if tries == 4:
            print("\nGame over.")


# Book solution
import random


def guessing_game():
    answer = random.randint(0, 100)


    while True:
        user_guess = int(input("What is your guess? "))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')

