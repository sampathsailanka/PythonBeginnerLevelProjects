import random


print(" ``````````````````` WELCOME TO THE NUMBER GUESSER! ```````````````````")

range = input('Enter the Range For Guessing ')

if range.isdigit():
    range =  int(range)
    if range <= 0:
        print('The Number you have Entered is less than Zero')
        quit()
else:
    print('Please Enter a Number Next Time')
    quit()

random_number = random.randint(0,range)

guesses = 1

while True:
    user_guess = input('Make a Guess ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Make it next time')
        continue

    if user_guess == random_number:
        print('You have Got it')
        break

    elif user_guess < random_number:
        print('Your Guess is Lesser than the Random Number ')
        guesses += 1

    else:
        print('Your Guess is Greater than the Random Number ')
        guesses += 1

print('You have completed the Game in',guesses,'Guessses .\n')

print("___________________Thanks for PLaying the Game___________________")