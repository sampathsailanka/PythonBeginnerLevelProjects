#NESTED LOOPS
#NESTED WHILE LOOPS
#SIMULATING A BANK ATM
print('WELCOME TO ATM')
restart =('y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Enter the 4 digit pin\t'))
    if pin == (3333):
        print('You Entered the pin correctly\n')
        while restart not in ['n','NO','no','N']:
            print('Press 1 for Checking Balance\t')
            print('Press 2 for Making Withdrawl\t')
            print('Press 3 for Pay in\t')
            print('Press 4 for Returning card\t')
            option = int(input('Enter the option\t'))
            if option == 1:
                print('Your Balance is',balance)
                restart = input('Would you like to go back\t')
                if restart in ['n','NO','no','N']:
                    print('Thank You')
                    break
            elif option == 2:
                current_amount = float(input('Enter the amount you want to withdrawl\t'))
                if current_amount in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                    balance = balance - current_amount
                    print('Your current balance is ',balance)
                    restart = input('Would you like to go back\t')
                    if restart in ['n','NO','no','N']:
                        print('Thank You')
                        break
                elif current_amount != [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                    print('INVALID')
                    restart = ('y')
            elif option == 3:
                pay_in = float(input('Enter the amount you pay\t'))
                balance = balance + pay_in
                print('The balance amount is ',balance)
                restart = input('Would you like to go back\t')
                if restart in ['n', 'NO', 'no', 'N']:
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait your card is being returned\t')
                print('Your card is returned')
                print('Thank you')
                break
            else :
                print('Enter the correct number\t')
                restart = ('y')
    elif pin != ('3333'):
        print('pin is incorrect')
        chances = chances-1
        if chances == 0:
            print('Your chances are over\n')
            break
