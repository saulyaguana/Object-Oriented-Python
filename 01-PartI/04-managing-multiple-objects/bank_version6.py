# Main program for controlling a Bank made up of Accounts
from Bank import Bank, AbortTransaction

# Create an instance of the Bank
bank = Bank("9 to 5", "123 Main Street, Anytown, USA", "(650) 555-1212")

# Main code
while True:
    print()
    print(
        """
        To get an account balance, press b
        To close an account, press c
        To make a deposit, press d
        To get bank information, press i
        To open a new account, press o
        To quit, press q
        To show all accounts, press s
        To make a withdrawal, press w
        """
    )
    print()
    
    action = input("What do you want to do?: ").lower()[0]
    print()
    
    try:
        if action == "b":
            bank.balance()
        elif action == "c":
            bank.closeAccount()
        elif action == "d":
            bank.deposit()
        elif action == "i":
            bank.get_info()
        elif action == "o":
            bank.open_account()
        elif action == "q":
            break
        elif action == "s":
            bank.show()
        elif action == "w":
            bank.withdraw()
    except AbortTransaction as error:
        print(error)
print("Done")