import random

print("\n")
print("="*36)
print("\tNumber guessing game")
print("="*36)

while True:
    target = random.randint(1,100)
    attempts = 0
    max_attempts = 10
    print(f"\nI'm thinking of a number between 1 and 100...")
    print(f"You have {max_attempts} attempts to guess it!")
    
    for attempt in range(1,max_attempts+1):
        attempts = attempt
        while True:
            try:
                guess = int(input(f"\nAttempt {attempts}/{max_attempts} | Your guess = "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 - 100")
            except ValueError:
                print("Invalid input, Please enter a valid number")
        
        if guess == target:
            print(f"\nCorrect, The number was {target}")
            print(f"You found it in {attempts} attempts")
            break
        elif guess < target:
            print("--> Too low, Try a higher number <--")
        else:
            print("--> Too high, Try a lower number <--")
        if target%2 == 0:
            print("--> The number is even")
        else:
            print("--> The number is odd")
            
        remaining = max_attempts-attempts
        if remaining > 0:
            print(f"{remaining} attempts remaining")

    else:
        print(f"\nGAME OVER, The number was {target}")
        print("You've used all your attempts")

    while True:
        play_again = input("\nDo you want to play again? (y/n) : ").lower()
        if play_again in ['y','yes','n','no']:
            break
        print("Please enter 'y' for yes or 'n' for no")

    if play_again in ['n','no']:
        print("\nThank you for playing\n")
        break
    print("\n" + "=" * 40)