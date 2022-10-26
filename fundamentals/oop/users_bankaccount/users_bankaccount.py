# bank account class

class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
        else:
            print('Insufficient funds')

# user class

class User:

    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, balance)
    
    # methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'Your current balance is {self.account.balance}')

account1 = User('Chris','email',0.02, 100)

account1.make_deposit(10).make_withdrawal(5).display_user_balance()

