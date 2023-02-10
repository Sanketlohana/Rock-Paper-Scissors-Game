import random

# This is a simple Rock , Paper and Scissor Game built using Python
Win = 0
Lose = 0

for count in range(5):

    user_input = int(input("\nRock : 1\nPaper : 2\nScissor : 3\n\nEnter respective number From above Choices : "))

    if user_input > 3 or user_input < 1:
        print("\nPlease enter a valid number")
    elif user_input == 1:
        choice_name = 'Rock'
    elif user_input == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    print("\nYour Choice was", choice_name)
    print("\nNow its System's turn to select... ")

    sys_choice = random.randint(1, 3)

    if sys_choice == 1:
        choice_name = 'Rock'
    elif sys_choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("\nSystem Choice : ", choice_name, "\n")
    if sys_choice == user_input:
        print("\nDraw")

    elif user_input == 1 and sys_choice == 2:
        print("You Lose ")
        Lose += 1
    elif user_input == 1 and sys_choice == 3:
        print("You Win ")
        Win += 1

    elif user_input == 2 and sys_choice == 3:
        print("You Lose ")
        Lose += 1
    elif user_input == 2 and sys_choice == 1:
        print("You Win ")
        Win += 1

    elif user_input == 3 and sys_choice == 1:
        print("You Lose ")
        Lose += 1
    elif user_input == 3 and sys_choice == 2:
        print("You Win ")
        Win += 1
print("Final Score : \nWins = ", Win)
print("Loses = ", Lose)
if Win == Lose:
    print("\n It's a Draw")
elif Win > Lose:
    print("\nCongratulations You Win ")
else:
    print("\nBetter Luck Next Time ^_^ ")
