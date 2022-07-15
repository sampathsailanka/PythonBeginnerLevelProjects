import random

print(" ``````````````````` WELCOME TO ROCK,PAPER,SCISSORS GAME ```````````````````")

list = ['rock','paper','scissors']

user_points = 0
computer_points = 0

while True:
    user_input = input('Enter rock/paper/scissors or "Q": ').lower()
    if user_input == 'q':
        break

    if user_input not in list:
        print('Enter the correct option ')
        continue

    random_pick = random.randint(0,2)

    computer_choice = list[random_pick]

    if user_input == 'rock' and computer_choice == 'scissprs':
        print('User Wins!')
        user_points += 1
    elif user_input == 'paper' and computer_choice == 'rock':
        print('User Wins!')
        user_points += 1
    elif user_input == 'scissors' and computer_choice == 'paper':
        print('User Wins!')
        user_points += 1

    else:
        print('Computer Wins!')
        computer_points += 1
print('Scores secured by User is',user_points)
print('Scores secured by Computer is',computer_points)
if(user_points > computer_points):
    print('User Wins the Game!')
elif user_points < computer_points :
    print('Computer Wins!')
else:
    print('Match TIED')
print("___________________Thanks for PLaying the Game___________________")