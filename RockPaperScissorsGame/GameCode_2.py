import random

print("\n")
print("="*40)
print("\tRock Paper Scissor Game")
print("="*40)

while True:
    print("\nHow many rounds would you like to play ?")
    while True:
        rounds = input("Enter number of rounds = ")
        if rounds.isdigit() and int(rounds) > 0:
            rounds = int(rounds)
            break
        print("Please enter a valid positive number")

    print("\nLet's begin...")
    print("-"*40)

    user_score = 0
    comp_score = 0
    draw_score = 0

    for r in range(1,rounds+1):
        print(f"\n--> Round {r}/{rounds}")
        print("Choices : 1) Rock  |  2) Paper  |  3) Scissor")
        while True:
            user_choice = input("Your choice = ")
            if user_choice == "1":
                user = "rock"
                break
            elif user_choice == "2":
                user = "paper"
                break
            elif user_choice == "3":
                user = "scissor"
                break
            else:
                print("Invalid choice, Enter 1/2/3 only")

        comp = random.choice(["rock", "paper", "scissor"])
        print(f"\nYour choice      : {user}")
        print(f"Computer choice  : {comp}")
        if user == comp:
            print("Result           : Draw")
            draw_score += 1

        elif (user == "rock" and comp == "scissor") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissor" and comp == "paper"):
            user_score += 1
            print("Result           : You win this round")
        else:
            comp_score += 1
            print("Result           : Computer wins this round")

    print("\n" + "="*38)
    print("\t       Score Board")
    print("="*38)
    print(f"Total Rounds   = {rounds}")
    print(f"Your Score     = {user_score}")
    print(f"Computer Score = {comp_score}")
    print(f"Draw Score     = {draw_score}")
    print("-"*38)

    if user_score > comp_score:
        print("Result   : You are the winner of this game")
    elif comp_score > user_score:
        print("Result   : Computer is the winner of this game")
    else:
        print("Result   : This game is Draw")
    print("="*38)

    while True:
        play_again = input("\nDo you want to play again ? (y/n) : ").lower()
        if play_again in ['y','yes','n','no']:
            break
        print("Please enter 'y' for yes or 'n' for no")

    if play_again in ['n','no']:
        print("\nThank you for playing\n")
        break
    print("\n" + "="*40)