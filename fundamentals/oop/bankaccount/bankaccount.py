class BankAccount:
    # all_balance = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        #default parameters
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.all_balance.append(self)

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

    # @classmethod
    # def all_balances(cls):
    #     sum = 0
    #     for account in cls.all_balance:
    #         sum += account1.balance
    #     return sum 


account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.03, 50)

account1.deposit(10).deposit(20).deposit(30).withdraw(5).yield_interest().display_account_info()
account2.deposit(10).deposit(20).withdraw(5).withdraw(10).withdraw(15).withdraw(20).yield_interest().display_account_info()

# print(BankAccount.all_balances())