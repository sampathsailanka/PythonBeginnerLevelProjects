#COLOR CHOICES GAME CODING IN PYTHON

import random as r
print('Welcome to Colors Choices Game')
print('THe WINNING rules for this game are there are five colors red,yellow,orange,green,blue')

computer_score = 0
player_score = 0

while True:
    print('----------')
    player_choice = int(input('Enter your choice: '))
    while player_choice>5 or player_choice<1:
        player_choice = int(input('Enter the valid pick: '))
    if player_choice == 1:
        choice_col = 'red'
    elif player_choice == 2:
        choice_col = 'yellow'
    elif player_choice == 3:
        choice_col = 'orange'
    elif player_choice == 4:
        choice_col = 'green'
    else:
        choice_col = 'blue'
    print('Your choice is '+str(choice_col))

    print("Now it's computer's turn......")
    computer_choice = r.randint(1,5)
    
    if computer_choice == 1:
        computer_choice_col = 'red'
    elif computer_choice == 2:
        computer_choice_col = 'yellow'
    elif computer_choice == 3:
        computer_choice_col = 'orange'
    elif computer_choice == 4:
        computer_choice_col = 'green'
    else:
        computer_choice_col = 'blue'
    print('computer\'s choice is ' + str(computer_choice_col))
    
    if(choice_col == computer_choice_col):
        player_score+=1
        print('Player score ='+str(player_score))
        print('computer score ='+str(computer_score))
    else:
        computer_score+=1
        print('computer score ='+str(computer_score))
        print('Player score =' + str(player_score))
    
    print('Do You Want To Play Again? (Y/N) OR (y/n)')
    answer = input()
    
    if answer == 'n' or answer == 'N':
        print('Thanks for playing the game')
        break

if (player_score == computer_score):
    print("<== Game was TIED ==>")
    print('Better luck next time')
elif (player_score > computer_score):
    print("<== Great! YOU'VE WON ==>")
    print('Keep Rocking')
else:
    print('<== Computer have WON the match ==>')
    print('Better Luck Next Time')
