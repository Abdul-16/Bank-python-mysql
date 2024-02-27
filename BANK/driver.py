from modules.bank_op import bank
from modules.utils import u_choice, logic

bankUser = bank()

choice = u_choice(3)


if choice == 1:
    userName = input('Enter Username: ')
    
    password = input('Enter Password: ')
    
    usrId = bankUser.signIn(userName, password)
    
    if usrId:
        logic(bankUser, usrId)
    else:
        print('username does not exist')

elif choice == 2:
    userName = input('Enter username: ')
    password = input('Enter password: ')
    
    bankUser.signUp(userName, password)
    
    usrId = bankUser.signIn(userName, password)
    
    if usrId:
        logic(bankUser, usrId)

elif choice == 3:
    print('Goodbye!')