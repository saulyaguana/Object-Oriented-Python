# Non-OOP
# Bank 2
# Single account

account_name = ""
account_balance = 0
account_password = ""

def new_account(name, balance, password):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password
    
def show():
    global account_name, account_balance, account_password
    print(f"Name: {account_name}")
    print(f"Balance: {account_balance}")
    print(f"Password: {account_password}")
    print()
    
def get_balance(password):
    global account_name, account_balance, account_password
    if password != account_password:
        print("Incorrect password")
        return None
    return account_balance

def deposit(amount_to_deposit, password):
    global account_name, account_balance, account_password
    if amount_to_deposit < 0:
        print("You cannot deposit a negative amount")
        return None
    if password != account_password:
        print("Incorrect password")
        return None
    account_balance += amount_to_deposit
    return account_balance

def withdraw(amount_to_withdraw, password):
    global account_name, account_balance, account_password
    if amount_to_withdraw < 0:
        print("You cannot withdraw a negative amount")
        return None
    if password != account_password:
        print("Incorrect password")
        return None
    if amount_to_withdraw > account_balance:
        print("You cannot withdraw more than your balance")
        return None
    account_balance -= amount_to_withdraw
    return account_balance

new_account("Joe", 100, "soup")  # Create an account

while True:
    print()
    print("Press b to get balance")
    print("Press d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()
    
    action = input("What do you want to do? ").lower()[0]
    print()
    
    if action == "b":
        print("Get Balance")
        user_password = input("What is the password?: ")
        the_balance = get_balance(user_password)
        if the_balance is not None:
            print("Your balance is: {the_balance}")
    elif action == "d":
        print("Deposit")
        user_deposit_amount = int(input("Please enter the amount to deposit: "))
        user_password = input("Please enter the password: ")
        
        new_balance = deposit(user_deposit_amount, user_password)
        
        if new_balance is not None:
            print(f"Your new balance is: {new_balance}")
            
    elif action == "q":
        break
            
print("Done")