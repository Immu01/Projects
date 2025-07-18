# Number Guessing Game

import random

print("\n"+"="*40)
print("  Welcome to the Number Guessing Game")
print("="*40+"\n")
number = random.randint(1,20)

while True:
    try:
        max_chances = int(input("Choose the maximum number of chances (1 to 5) = "))
        if 1 <=max_chances<= 5:
            break
        else:
            print("Invalid input, Please enter a number between 1 and 5")
    except ValueError:
        print("Invalid input, Please enter a number")

print(f"\nThink of a number between 1 and 20")
print(f"You have {max_chances} chances to guess it\n")

def give_clue(num_to_guess,attempts_left):
    print("\n--- CLUE ---")
    if attempts_left == 3:
        if num_to_guess%2 == 0:
            print("Clue : The number is EVEN")
        else:
            print("Clue : The number is ODD")
    elif attempts_left == 2:
        primes = [2,3,5,7,11,13,17,19]
        if num_to_guess in primes:
            print("Clue : The number is a PRIME number")
        else:
            print("Clue : The number is a COMPOSITE number (or 1)")
    elif attempts_left == 1:
        perfect_squares = [1,4,9,16]
        if num_to_guess in perfect_squares:
            print("Clue : The number is a PERFECT SQUARE")
        else:
            print("Clue : The number is NOT a perfect square")
    print("--------------------\n")
chances_taken = 0
while chances_taken < max_chances:
    try:
        guess = int(input(f"Attempt {chances_taken+1}/{max_chances} - Enter your guess = "))
    except ValueError:
        print("Invalid input, Please enter a whole number")
        continue
    if guess == number:
        if chances_taken == 0:
            print("\n"+"*"*50)
            print(f"  PERFECT! YOU GUESSED THE NUMBER {number} ON YOUR FIRST ATTEMPT")
            print("*"*50+"\n")
        else:
            print("\n"+"*"*50)
            print(f"  CONGRATULATIONS, YOU GUESSED THE NUMBER {number} IN {chances_taken+1} ATTEMPTS")
            print("*"*50+"\n")
        break
    elif guess < number:
        print(f"Your guess was too low, Try a higher number than {guess}")
    else:
        print(f"Your guess was too high, Try a lower number than {guess}")
    chances_taken += 1
    if max_chances-chances_taken<=3 and chances_taken<max_chances:
        give_clue(number,max_chances-chances_taken)
    if chances_taken < max_chances:
        print(f"You have {max_chances-chances_taken} chance(s) left\n")
else:
    print("\n"+"-"*50)
    print(f"  GAME OVER, You ran out of chances")
    print(f"  The number was {number}")
    print("-"*50+"\n")