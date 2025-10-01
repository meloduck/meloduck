#number guessing game 

#to do:
    #

import random

#minimum and maximum(for easy configuration)
min=1
max=100

tries=0

number=random.randint(min, max)
while True:
    guess=input(f"Guess a number between {min} and {max}: ")
    if not guess.isdigit():
        print("Please input a number.")
        continue
    guess=int(guess)
    tries+=1
    if guess>max:
        print(f"Pick a number {min}-{max}!")
    elif guess<number:
        print("Too low!")
    elif guess>number:
        print("Too high!")
    else:
        print(f"You guessed it in {tries} tries!")
        break