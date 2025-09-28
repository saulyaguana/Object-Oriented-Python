# Bank that manages a dictinoary of Account objects
from datetime import datetime, time
from Account import Account

class Bank():
    def __init__(self):
        self.accounts_dict = {}
        self.next_account_number = 0
        
        self.start_hour = time(9, 0)
        self.end_hour = time(18, 0)
        self.current_hour = datetime.now().time()
        
    def create_account(self, the_name, the_starting_amount, the_password):
        account = Account(the_name, the_starting_amount, the_password)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = account
        # Increment to prepare for the next account to be created
        self.next_account_number += 1
        return new_account_number
    
    def open_account(self):
        print("*** Open Account ***")
        user_name = input("What is the name for the new user account?: ")
        user_starting_amount = int(input("What is the starting balance for this account?: "))
        user_password = input("What is the password you want to use for this account?: ")
        
        user_account_number = self.create_account(user_name, user_starting_amount, user_password)
        print(f"Your new account is: {user_account_number}")
        print()
        
    def close_account(self):
        print("*** Close Account ***")
        user_account_number = int(input("What is your account number?: "))
        user_password = input("What is your password?: ")
        
        account = self.accounts_dict[user_account_number]
        the_balance = account.get_balance(user_password)
        
        if the_balance is not None:
            print(f"You had {the_balance} in your account, which is being returned to you.")
            # Remove user's account from  the dictionary of accounts
            del self.accounts_dict[user_account_number]
            print("Your account is now closed.")
            
    def balance(self):
        print("*** Balance ***")
        user_account_number = int(input("Please enter your account number: "))
        user_account_password = input("Please enter the password: ")
        
        account = self.accounts_dict[user_account_number]
        
        the_balance = account.get_balance(user_account_password)
        
        if the_balance is not None:
            print(f"Your balance is: {the_balance}")
            
    def deposit(self):
        print("*** Deposit ***")
        account_num= int(input("Please enter the account number: "))
        deposit_amount = int(input("Please enter the amount to deposit: "))
        user_account_password = input("Pleaseenther the password: ")
        
        account = self.accounts_dict[account_num]
        
        the_balance = account.deposit(deposit_amount, user_account_password)
        
        if the_balance is not None:
            print(f"Your new balance is: {the_balance}")
            
    def show(self):
        print("*** Show Accounts ***")
        for user_account_number in self.accounts_dict:
            account = self.accounts_dict[user_account_number]
            print(f"Account number: {user_account_number}")
            account.show()
            
    def withdraw(self):
        print("*** Withdraw ***")
        
        def current_hour():
            return self.current_hour < self.start_hour or self.current_hour > self.end_hour
        
        if current_hour():
            print("You are after hours. Please try again later.")
            return
        user_account_number = int(input("Please enter your account number: "))
        user_amount = int(input("Please enter the amount to withdraw: "))
        user_account_password = input("Please enter the password: ")
        
        account = self.accounts_dict[user_account_number]
        
        the_balance = account.withdraw(user_amount, user_account_password)
        
        if the_balance is not None:
            print(f"Withdrew: {user_amount}")
            print(f"Your new balance is: {the_balance}")