class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        if float(dep_amount):
            self.balance += dep_amount
            return self.balance
        else:
            return "Please enter valid amount"

    def withdraw(self, with_amount):
        if float(with_amount):
            if (self.balance - with_amount) < 0:
                return "Insufficient funds available"
            self.balance -= with_amount
            return self.balance
        else:
            return "Please enter valid amount"


acc = BankAccount("Tshepo")
acc.deposit(20)
print(acc.balance)
print(acc.withdraw(25))
print(acc.balance)
