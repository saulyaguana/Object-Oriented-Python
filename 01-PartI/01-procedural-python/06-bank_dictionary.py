# NON-OOP Bank
# Version 5
# Any number of accounts - with a list of dictionaries

accounts_list = []

def new_account(name, balance, password):
    global accounts_list
    new_account_dict = {"name": name, "balance": balance, "password": password}
    accounts_list.append(new_account_dict)
    
def show(account_number):
    global accounts_list
    print(f"Account: {account_number}")
    this_account_dict = accounts_list[account_number]
    
    print(f"Name: {this_account_dict["name"]}")
    print(f"Balance: {this_account_dict["balance"]}")
    print(f"Password: {this_account_dict["password"]}")
    print()
    
def get_balance(account_number, password):
    global accounts_list
    this_account_dict = accounts_list[account_number]
    if password != this_account_dict["password"]:
        print("Incorrect password")
        return None
    return this_account_dict["balance"]

def deposit(account_number, amount, password):
    global accounts_list
    this_account_dict = accounts_list[account_number]
    if amount < 0:
        print("You cannot deposit a negative amount!")
        return None
    if password != this_account_dict["password"]:
        print("Incorrect password")
        return None
    this_account_dict["balance"] += amount
    return this_account_dict["balance"]

def withdraw(account_number, amount, password):
    global accounts_list
    this_account_dict = accounts_list[account_number]
    if password != this_account_dict["password"]:
        print("Incorrect password")
        return None
    if amount < 0 or amount > this_account_dict["balance"]:
        print("You cannot withdraw that amount!")
        return None
    
    this_account_dict["balance"] -= amount
    return this_account_dict["balance"]

# Create two sample accounts
print(f"Joe's account is account number: {len(accounts_list)}")
new_account("Joe", 1000, "joepassword")

print(f"Mary's account is account number: {len(accounts_list)}")
new_account("Mary", 2000, "marypassword")

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press n to create a new account")
    print("Press w to make a withdrawal")
    print("Press s to show account details")
    print("Press q to quit")
    print()
    
    action = input("What do you want to do?: ").lower()[0]
    
    if action == "b":
        print("Get Balance:")
        user_account_number = int(input("Enter your account number: "))
        user_password = input("Enter your password: ")
        the_balance = get_balance(user_account_number, user_password)
        if the_balance is not None:
            print(f"Your balance is {the_balance}")
    elif action == "d":
        print("Deposit:")
        user_account_number = int(input("Enter your account number: "))
        user_password = input("Enter your password: ")
        user_deposit_amount = int(input("Enter the amount to deposit: "))
        
        new_balance = deposit(user_account_number, user_deposit_amount, user_password)
        
        if the_balance is not None:
            print(f"Your new balance is {new_balance}")
    elif action == "q":
        break
print("Done")