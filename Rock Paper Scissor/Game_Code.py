# Rock, Paper, Scissor Game

import random

def decision(val1,val2,your_score,computer_score,draw_score):
    if val1==val2:
        print("The game is draw")
        draw_score += 1
    elif val1 == 1 and val2 == 2 or val1 == 2 and val2 == 3 or val1 == 3 and val2 == 1 :
        print("You Win this round")
        your_score += 1
    else:
        print("Computer Wins this round")
        computer_score += 1
    return your_score,computer_score,draw_score

round = int(input("\nEnter the number of rounds you want to play = "))
draw_score = 0
your_score = 0
computer_score = 0
list = [1,2,3]
print("""
1. Rock
2. Paper
3. Scissor
      """)
numbers = {1:"Rock",
           2:"Paper",
           3:"Scissor"}
for i in range(round):
    computer = random.choice(list)
    print(f"            Round = {i+1}\n")
    print("The computer made a choice")
    your_choice = int(input("\nEnter your choice = "))
    if your_choice > 3:
        print("Choose the correct option\n\n")
        continue
    print(f"\nYour Choice = {numbers.get(your_choice)}\nComputer's Choice = {numbers.get(computer)}")
    print("\n----------Result--------------->",end=" ")
    your_score, computer_score, draw_score = decision(computer, your_choice, your_score, computer_score, draw_score)
    print(f"\nYour Score = {your_score} --- Computer score = {computer_score} --- Draw Score = {draw_score}")
    print(f"\n----------END OF THE ROUND {i+1}----------\n\n")

print("\n--------------------END OF THE GAME--------------------")

print("\nFinal Scores :\n")
print(f"Your Score = {your_score}")
print(f"Computer Score = {computer_score}")
print(f"Draw matches = {draw_score}")
if your_score == computer_score:
    print("\nBoth scored same score, It's a DRAW")
elif your_score > computer_score:
    print("\nYOU WON!!")
else:
    print("\nCOMPUTER WON!!")