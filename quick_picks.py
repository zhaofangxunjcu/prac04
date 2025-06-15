import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

main()
