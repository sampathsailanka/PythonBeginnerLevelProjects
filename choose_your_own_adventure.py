print(" ``````````````````` WELCOME TO ROCK,PAPER,SCISSORS GAME ```````````````````")

name = input('Enter your name ')

print('You are in the Game... :) ')

way = input('Imagine you are at teh END of the road which was having Two Ways Left and Right, Which One would you choose (Left/Right) ').lower()

if way == 'left':
    way = input('Now you have reached to a road on the banks of river, You should either swim or walk on the road, Which one do you choose(swim/walk) ').lower()

    if way == 'swim':
        print('You have swam and eaten by the alligator,You LOST')
    elif way == 'walk':
        print('You walk on the Road and ran out of water,You LOST')
    else:
        print('You have\'nt entered the correct option')

elif way == 'right':
    way = input('Now you are at the Bridge which is Woobly, Would you go on the Bridge or Go back (go/back) ').lower()

    if way == 'back':
        print("You went Back to the road,so you LOST the Game ")
    elif way == 'go':
        ans = input('You walked on the bridge and met an stranger,He was injured ,Would you rather help him or ignore him (help/ignore) ').lower()
        
        if ans == 'help':
            print('You have met and help him.He gave the gold to you,You WON!')
        elif ans == 'ignore':
            print('You haven\'t helped him so you wont get money,You LOST! ' )
        else:
            print('You have\'nt entered the correct option. You LOST')

    else:
        print('You have\'nt entered the correct option. You LOST')

else:
    print('You have\'nt entered the correct option, Please Enter the correct option ')

print('Thank you for Trying',name)

print("___________________Thanks for PLaying the Game___________________")