class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        """Deposit the given amount into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw the given amount from the account."""
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")
    def get_balance(selve):
        """Get the current balance."""
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):

        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Apply interest to the balance based on the interest rate."""
        self.balance *= (1 + self.interest_rate)

    def print(self):
        """Override the print method to display balance and interest rate."""
        print(f"Account Holder:{self.account_holder}")
        print(f"Account Number:{self.account_number}")
        print(f"Balance:${self.balance:.2f}")
        print(f"Interest Rate:{self.interest_rate * 100:.2f}%")

#creat an instance of SavingsAccount
savings_account = SavingsAccount(account_number="123456", account_holder="John Doe", interest_rate=0.02)

#Perform a deposit of $1000
savings_account.deposit(1000)

#Perform a deposit of $500
savings_account.withdraw(500)

#Apply interest
savings_account.apply_interest()

#print the current balance and interest rate
savings_account.print()
