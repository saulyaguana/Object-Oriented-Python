# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring in all the code from the Account class file
from Account import Account

# Create another account with information from the user
print()
user_name = input("What is the name for the new user account?: ")
user_balance = int(input("What is the starting balance for this account?: "))
user_password = input("What is the password you want to use for this account?: ")

new_account = Account(user_name, user_balance, user_password)

# Show the newly created user account
new_account.show()

# Let's deposit 100 into the new account
new_account.deposit(100, user_password)
user_balance = new_account.get_balance(user_password)
print()
print(f"After depositing 100, the user's balance is: {user_balance}")

# Show the new account
new_account.show()

# Create two accounts
joes_account = Account("Joe", 100, "joesPassword")
print("Created an account for Joe")

marys_account = Account("Mary", 12345, "marysPassword")
print("Created an account for Mary")

joes_account.show()
marys_account.show()
print()

# Call some methods on the different accounts
print("Calling methods of the  two accounts...")
joes_account.deposit(50, "joesPassword")
marys_account.withdraw(345, "marysPassword")
marys_account.deposit(100, "marysPassword")

# Show the accounts
joes_account.show()
marys_account.show()