#dice roll 

#to do:
    #

import random

#number of sides (max):
max=20
min=1

#amount of die rolled (rolls):
rolls=2

for rolls in range(rolls):
    roll=random.randint(min,max)
    print(f"You rolled {roll}!")