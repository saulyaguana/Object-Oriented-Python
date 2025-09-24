# Test program using accounts
# Version 1, using explicit variables for each Account object

# Bring in all the code from the Account class file
from Account import Account

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