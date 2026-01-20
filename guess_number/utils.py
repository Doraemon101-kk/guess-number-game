def is_in_range(min_num, num, max_num):
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