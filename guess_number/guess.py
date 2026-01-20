from random import randint
from .utils import *

def guess_single_round(min_num, max_num):

    num = randint(min_num, max_num)
    count = 0

    while True:
        print(f"Please give a number between {min_num} and {max_num}:")
        
        guess = get_valid_input()

        count += 1

        if not is_in_range(min_num, guess, max_num):
            print("Out of range")
            continue

        if guess == num:
            print("Bingo!")
            print(f"You played {count} times to guess it.")
            return count
        
        elif guess < num:
            print("Too small")
            
        else:
            print("Too big")
