# Define a base class called Account
# - This class represents a generic bank account with basic functionalities
class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number  # Account number for identification
        self.balance = balance  # Initial balance of the account
    
    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
    
    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
    
    # Method to display the account balance
    def display_balance(self):
        print(f"Account {self.account_number} Balance: ${self.balance:.2f}")

# Define a derived class called SavingsAccount that inherits from Account
# - This class represents a savings account with an added interest rate
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, balance)  # Initialize base class attributes
        self.interest_rate = interest_rate  # Interest rate for the savings account
    
    # Method to apply interest to the balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied ${interest:.2f} interest. New balance: ${self.balance:.2f}")

# Define another derived class called CheckingAccount that also inherits from Account
# - This class represents a checking account with overdraft protection
class CheckingAccount(Account):
    def __init__(self, account_number, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, balance)  # Initialize base class attributes
        self.overdraft_limit = overdraft_limit  # Maximum overdraft limit for the account
    
    # Override the withdraw method to account for overdraft protection
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal denied: exceeds overdraft limit")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

# Define a derived class from SavingsAccount called PremiumSavingsAccount
# - This account type has a higher interest rate for premium users
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance=0.0, interest_rate=0.05):
        super().__init__(account_number, balance, interest_rate)  # Higher interest rate
        self.premium_features = ["Priority Support", "Higher Interest Rate"]
    
    # Additional method specific to PremiumSavingsAccount
    def display_premium_features(self):
        print("Premium Features: ", ", ".join(self.premium_features))

# Example Usage:
# Creating and interacting with different types of accounts

# Standard Savings Account
savings = SavingsAccount("SA123", 1000.0)
savings.display_balance()       # Account SA123 Balance: $1000.00
savings.apply_interest()        # Applies interest based on standard rate
savings.display_balance()       # Updated balance after interest

# Checking Account with Overdraft
checking = CheckingAccount("CA456", 500.0, overdraft_limit=200.0)
checking.display_balance()       # Account CA456 Balance: $500.00
checking.withdraw(600.0)         # Withdrawal within overdraft limit
checking.display_balance()       # Updated balance
checking.withdraw(200.0)         # Withdrawal denied due to overdraft limit

# Premium Savings Account
premium_savings = PremiumSavingsAccount("PS789", 2000.0)
premium_savings.display_balance()  # Account PS789 Balance: $2000.00
premium_savings.apply_interest()   # Applies higher interest rate
premium_savings.display_balance()  # Updated balance after interest
premium_savings.display_premium_features()  # Displays premium features

# Explanation of multi-level inheritance and method overriding:
# - The Account class is a base class providing basic deposit, withdrawal, and balance features.
# - SavingsAccount and CheckingAccount inherit from Account but add unique features:
#     - SavingsAccount has an interest rate and apply_interest method.
#     - CheckingAccount overrides the withdraw method to add overdraft protection.
# - PremiumSavingsAccount inherits from SavingsAccount with a higher interest rate
#   and additional premium features, demonstrating multi-level inheritance.
# - Each class adds or overrides methods, making the system extensible and reusable.
