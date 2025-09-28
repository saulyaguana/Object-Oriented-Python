# Main program for controlling a Bank made up of Accounts

# Bring in the code of the Bank class
from Bank import Bank

# Create an instance of the Bank
bank = Bank()

# Main code
# Create two instance of the Bank
joes_account_number = bank.create_account("Joe", 100, "JoesPassword")
print(f"Joe's account number is: {joes_account_number}")

marys_account_number = bank.create_account("Mary", 12345, "MarysPassword")
print(f"Marys' account number is: {marys_account_number}")

while True:
    print()
    print("""
        To get an account balance, press b
        To close an account, press c
        To make deposit, press d
        To open a new account, press o
        To quit, press q
        To show all account, press s
        To make a withdrawal, press w  
        """)
    print()
    
    action = input("What do you want to do?: ").lower()[0]
    print()
    
    if action == "b":
        bank.balance()
    elif action == "c":
        bank.close_account()
    elif action == "d":
        bank.deposit()
    elif action == "o":
        bank.open_account()
    elif action == "s":
        bank.show()
    elif action == "q":
        break
    elif action == "w":
        bank.withdraw()
    else:
        print("Sorry, that was not a valid action. Please try again.")
print("Done")