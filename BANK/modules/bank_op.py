import mysql.connector as connect
from modules.utils import decoration

class bank:
    @decoration
    def __init__(self, *args, **kwargs):
        self.conn = connect.connect(host='localhost', user='root', password='YOUR_PASSWORD', database='bank')
        print('|','WELCOME TO THE BANK APPLICATION',' |')

    def signUp(self, userName, password):
        cur = self.conn.cursor()
        try:
            cur.execute(f"insert into users (userName, userPassword) values('{userName}', '{password}');")
            cur.execute(f"insert into balance (userName) values('{userName}')")
            self.conn.commit()
            print('Sign up successful')
        except connect.Error as e:
            print(f'Error adding the user: {e}')

    def signIn(self, Name, password):
        cur = self.conn.cursor()
        try:
            
            cur.execute(f"Select userName, userPassword FROM users WHERE userName = '{Name}';")
            usrName = False
            usrPass = False
            for row in cur:
                usrName = row[0]
                usrPass = row[1]            
            if usrName:
                while password != usrPass:
                    password = input('Re-enter your password: ')
                print("Signed in successfully")
            
            
            return usrName
        except connect.Error as e:
            print(f'Error logging in: {e}')

    def getBalance(self, userName):
        cur = self.conn.cursor()
        try:
            cur.execute(f"Select b.userBalance from users u JOIN balance b USING (userName) where b.userName = '{userName}';")
            for row in cur:
                bal = row[0]
            return bal
        except connect.Error as e:
            print(f'Error getting balance: {e}')
    
    def withdraw(self, userName, amt):
        cur = self.conn.cursor()
        try:
            cur.execute(f"update balance set userBalance = userBalance - {amt} where userName = '{userName}';")
            self.conn.commit()
            print(f'Amount {amt} withdrew, current balance is: {self.getBalance(userName)}')
        except connect.Error as e:
            print(f'Error withdrawing: {e}')
            
    def deposit(self, userName, amt):
        cur = self.conn.cursor()
        try:
            cur.execute(f"update balance set userBalance = {self.getBalance(userName) + amt} where userName = '{userName}';")
            self.conn.commit()
            print(f'Amount {amt} deposited, current balance is: {self.getBalance(userName)}')
        except connect.Error as e:
            print(f'Error depositing: {e}')

    def logout(self):
        if self.conn:
            self.conn.close()
            print('\nGoodbye')

if __name__ == "__main__":
    b = bank()
    b.signUp('abd', 'abd')
    b.signIn('abd', 'abd')
