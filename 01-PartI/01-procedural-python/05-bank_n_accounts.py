# Non-OOP bank
# Version 4
# Any number of accounts - with lists

account_names_list = []
account_balances_list = []
account_passwords_list = []

def new_account(name, password, balance):
    global account_names_list, acccount_balances_list, account_passwords_list
    account_names_list.append(name)
    account_balances_list.append(balance)
    account_passwords_list.append(password)

def show(account_number):
    global account_names_list, account_balances_list
    print("Account number:", account_number)
    print("Name:", account_names_list[account_number])
    print("Balance:", account_balances_list[account_number])
    print("Password:", account_passwords_list[account_number])
    print()
    
def get_balance(account_number, password):
    global account_names_list, account_balances_list, account_passwords_list
    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None
    return account_balances_list[account_number]

# Create two samples accounts
print(f"Joe's account is account number: {len(account_names_list)}")
new_account("Joe", 100, "soup")

print(f"Mary's account is account number: {len(account_names_list)}")
new_account("Mary", 12345, "nuts")

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press n to create a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()
    
    action = input("What do you want to do?: ").lower()[0]
    print()
    
    if action == "b":
        print("Get Balance:")
        user_account_number = int(input("Please enter your account number: "))
        usr_password = input("Please enter your password: ")
        the_balance = get_balance(user_account_number, usr_password)
        
        if the_balance is not None:
            print(f"Your balance is: {the_balance}")
# print("Done")