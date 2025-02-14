class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Php{amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: Php{amount:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def display_balance(self):
        print(f"Account Balance: Php{self.balance:.2f}")

# Create a bank account
account = BankAccount("12345678", "James Pelimon")

# Perform transactions
account.deposit(500)   # Deposit $500
account.withdraw(200)  # Withdraw $200
account.display_balance()  # Display the balance

account.withdraw(400)  # Attempt to withdraw $400, should fail due to insufficient balance
account.display_balance()  # Display the updated balance