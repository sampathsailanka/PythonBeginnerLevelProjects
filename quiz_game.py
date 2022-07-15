print(" ``````````````````` WELCOME TO THE QUIZ GAME! ```````````````````")
interest = input('Are you intrested to play the Game \n').lower()

if (interest) in ['no','NO','n','N','nO','No']:
    quit()
print('That\'s Great...Lets start the game :)')
score = 0

question_1 = input('What is CPU stands for? \n').lower()
if question_1 == 'central processing unit':
    print("Yeah! You got right")
    score += 1
else:
    print("OOPS ! You got wrong")

question_2 = input('Who is the father of Computer science? \n').lower()
if question_2 == 'charles babbage':
    print("Yeah! You got right")
    score += 1
else:
    print("OOPS ! You got wrong")

question_3 = input('In a computer, most processing takes place in _______? \n').lower()
if question_3 == 'cpu':
    print("Yeah! You got right")
    score += 1
else:
    print("OOPS ! You got wrong")

question_4 = input('What is GPU stands for? \n').lower()
if question_4 == 'graphics processing unit':
    print("Yeah! You got right")
    score += 1
else:
    print("OOPS ! You got wrong")

question_5 = input('What converts an entire program into machine language? \n').lower()
if question_5 == 'compiler':
    print("Yeah! You got right")
    score += 1
else:
    print("OOPS ! You got wrong")


print('The Quiz Game has ended the Scores are \n')

print('You secured '+ str(score) + ' out of 5 Questions' + ' in the Quiz')

print('You secured ' + str((score/4) * 100) + '%. ')

print("___________________Thanks for PLaying the Game___________________")