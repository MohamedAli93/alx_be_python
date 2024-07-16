class BankAccount:
    def __init__(self, account_balance=0.0):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        while self.account_balance-amount >= 0:
            return True
        else:
            return False
    def display_balance(self):
        print(f"the current available balance is {self.account_balance}")    

