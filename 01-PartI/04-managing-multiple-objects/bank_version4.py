# Interactive test program creating a dictionary of accounts
# Version 4, with an interactive menu

from Account import Account

accounts_dict = {}
next_account_number = 0

while True:
    print("""
          Press b to get the balance
          Press d to make a deposit
          Press o to open a new account
          press w to make a withdrawal
          Press s to show all accounts
          Press q to quit
          """)
    print()
    
    action = input("What do you want to do?: ").lower()[0]
    print()
    
    if action == "b":
        print("*** Get Balance ***")
        user_account_number = int(input("Please enter your account number: "))
        user_account_password = input("Please enter the password: ")
        
        account = accounts_dict[user_account_number]
        the_balance = account.get_balance(user_account_password)
        
        if the_balance is not None:
            print(f"Your balance is {the_balance}")
            
    elif action == "d":
        print("*** Deposit ***")
        user_account_number = int(input("Please enter your account number: "))
        user_deposit_amount = int(input("Please enter the amount to deposit: "))
        user_password = input("Please enter the password: ")
        
        account = accounts_dict[user_account_number]
        the_balance = account.deposit(user_deposit_amount, user_password)
        
        if the_balance is not None:
            print(f"Your new balance is {the_balance}")
            
    elif action == "o":
        print("*** Open Account ***")
        user_name = input("What is the name for the new user account?: ")
        user_starting_amount = int(input("What is the starting amount for this account?: "))
        user_password = input("What is the password you want to use for this account?: ")
        
        account = Account(user_name, user_starting_amount, user_password)
        accounts_dict[next_account_number] = account
        print(f"Your new account number is {next_account_number}")
        next_account_number += 1
        print()
        
    elif action == "s":
        print("*** Show All Accounts ***")
        for user_account_number in accounts_dict:
            account = accounts_dict[user_account_number]
            print(f"Account number: {user_account_number}")
            account.show()
            
    elif action == "q":
        break
    
    elif action == "w":
        print("*** Withdraw ***")
        user_account_number = int(input("Please enter your account number: "))
        user_withdrawal_amount = int(input("Please enter the amount to withdraw: "))
        user_password = input("Please enter the password: ")
        
        account = accounts_dict[user_account_number]
        the_balance = account.withdraw(user_withdrawal_amount, user_password)
        
        if the_balance is not None:
            print(f"Whithdrawal: {user_withdrawal_amount}")
            print(f"Your new balance is {the_balance}")
            
    else:
        print("Sorry, that was not a valid action. Please try again.")
        
print("Done")