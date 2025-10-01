# Bank that manages a dictinoary of Account objects
from datetime import datetime, time
from Account import Account, AbortTransaction

class Bank():
    def __init__(self, hours, address, phone):
        self.accounts_dict = {}
        self.next_account_number = 0
        
        self.hours = hours
        self.address = address
        self.phone = phone
        
        self.start_hour = time(9, 0)
        self.end_hour = time(18, 0)
        self.current_hour = datetime.now().time()
        
    def ask_for_valid_account_number(self):
        try:
            account_number = int(input("What is your account number?: "))
        except ValueError:
            raise AbortTransaction("The account must be an integer")
        if account_number not in self.accounts_dict:
            raise AbortTransaction(f"There is no account {account_number}")
        return account_number
    
    def get_users_account(self):
        account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[account_number]
        self.ask_for_valid_password(account)
        return account
            
        
    def ask_for_valid_password(self, account):
        password = input("Please enter your password: ")
        account.check_password_match(password)
    
    def create_account(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.next_account_number
        self.accounts_dict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.next_account_number += 1
        return newAccountNumber

    def open_account(self):
        print('*** Open Account ***')
        userName = input('What is your name? ')
        userStartingAmount = input('How much money to start your account ? ')
        user_password = input('What password would you like to use for this account? ')
        user_account_number = self.create_account(userName, userStartingAmount, user_password)
        print('Your new account number is:', user_account_number)

    def close_account(self):
        print('*** Close Account ***')
        user_account_number = self.askForValidAccountNumber()
        oAccount = self.accounts_dict[user_account_number]
        self.ask_for_valid_password(oAccount)
        theBalance = oAccount.get_balance()
        print('You had', theBalance, 'in your account, which is being returned to you.')
        del self.accounts_dict[user_account_number]
        print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        oAccount = self.get_users_account()
        theBalance = oAccount.get_balance()
        print('Your balance is:', theBalance)
            
    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.get_users_account()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.get_users_account()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)

    def get_info(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accounts_dict), 'account(s) open.')

    # Special method for Bank administrator only
    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for user_account_number in self.accounts_dict:
            oAccount = self.accounts_dict[user_account_number]
            print('Account:', user_account_number)
            oAccount.show()
            print()