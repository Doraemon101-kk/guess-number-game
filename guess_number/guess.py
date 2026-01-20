from random import randint
from sys import argv

def guess(min_num, max_num):

    num = randint(min_num, max_num)
    count = 0

    while True:
        print(f"Please give a number between {min_num} and {max_num}:")
        
        guess = get_valid_input()

        count += 1

        if not number_in_range(min_num, guess, max_num):
            print("Out of range")
            continue

        if guess == num:
            print("Bingo!")
            print(f"You played {count} times to guess it.")
            break
        elif guess < num:
            print("Too small")
            
        else:
            print("Too big")

def number_in_range(min_num, num, max_num):
    return min_num <= num <= max_num

def get_valid_input():
    while True:     
        s = input().strip()

        if not s:
            print("Please give a integer number")
            continue

        try:
            return int(s)
        except ValueError:
            print("Please give a integer number")
            continue

def parse_args():
    default_min, default_max = 1, 50
    
    if len(argv) == 3:
        try:
            a = int(argv[1])
            b = int(argv[2]) 
            if a < b:
                return a, b
        except ValueError:
            pass
        
    return default_min, default_max

if __name__ == "__main__":
    min_num, max_num = parse_args()
    guess(min_num, max_num)
