
def decoration(func):
    def wrapper(*args, **kwargs):
        print('\n+', '----'*8, '+')
        value = func(*args, **kwargs)
        print('+', '----'*8, '+\n')
        return value
    return wrapper

@decoration
def u_choice(num):
    if num == 4:
        choice = int(input('\nSELECT OUR SERVICES:\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Logout\nYour Choice: '))
        while choice not in {1,2,3,4}:
            choice = int(input('Re-enter your choice, between 1, 2, 3 and 4: '))
    elif num == 3:
        choice = int(input('1. Login\n2. Sign up\n3. Exit\nEnter your desired option: '))
        while choice not in {1,2,3}:
            choice = int(input('Re-enter your choice, between 1, 2 and 3: '))
    return choice

def logic(bankUser, usrId):
    choice = u_choice(4)
    while True:
        if choice == 1:
            print(f"Current balance: {bankUser.getBalance(usrId)}")
            choice = u_choice(4)

        elif choice == 2:
            amt = float(input('Enter amount to withdraw: '))
            if bankUser.getBalance(usrId) <= 0:
                print(f"Cannot withdraw {amt} if balance is 0")
            else:
                bankUser.withdraw(usrId, amt)
            choice = u_choice(4)
        
        elif choice == 3:
            amt = float(input('Enter the amount to deposit: '))
            bankUser.deposit(usrId, amt)
            choice = u_choice(4)
        
        elif choice == 4:
            bankUser.logout()
            break
        
if __name__ == "__main__":
    a = u_choice(3)
    print(a)