# Test program using accounts
# Version 3, using a dictionary of accounts

# Bring in all the code from the Account class file
from Account import Account

accounts_dict = {}
next_account_number = 0

# Create two accounts:
account = Account("Joe", 100, "joesPassword")
joes_account_number = next_account_number
accounts_dict[joes_account_number] = account
print(f"Account number for Joe is: {joes_account_number}")
next_account_number += 1

account = Account("Mary", 12345, "marysPassword")
marys_account_number = next_account_number
accounts_dict[marys_account_number] = account
print(f"Account number for Mary is: {marys_account_number}")
next_account_number += 1

accounts_dict[joes_account_number].show()
accounts_dict[marys_account_number].show()
print()

# Call some methods on the different accounts
print("Calling methods of the two accounts...")
accounts_dict[joes_account_number].deposit(50, "joesPassword")
accounts_dict[marys_account_number].withdraw(345, "marysPassword")
accounts_dict[marys_account_number].deposit(100, "marysPassword")

# Show the accounts
accounts_dict[joes_account_number].show()
accounts_dict[marys_account_number].show()

# Create another account with information from the user
print()
user_name = input("What is the namefor the new user account?: ")
user_balance = int(input("What is the starting balance for this account?: "))
user_password = input("What is the password you want to use for this account?: ")

account = Account(user_name, user_balance, user_password)
new_account_number = next_account_number
accounts_dict[new_account_number] = account
print(f"Account number for new account is: {new_account_number}")
next_account_number += 1

# Show the newly created user account
accounts_dict[new_account_number].show()

# Let's deposit 100 into the new account
accounts_dict[new_account_number].deposit(100, user_password)
users_balance = accounts_dict[new_account_number].get_balance(user_password)
print()
print(f"After depositing 100,the user's balance is: {users_balance}")

# Show the new account
accounts_dict[new_account_number].show()