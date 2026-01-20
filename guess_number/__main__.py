from .guess import *
from sys import argv

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
    round = 0
    attempts = 0
    while True:
        
        attempts += guess_single_round(min_num, max_num)
        round += 1
        
        reply = input("Do you want to play one more time? If not, input No")
        if reply in {"No", "no", "NO"}:
            break

    if round > 0:
        print(f"You played {round} rounds, with an average of {(attempts/round):.1f} guesses per round.")