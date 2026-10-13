class bank:
    def __init__(self, balance):
        self.balance = balance  #main amount
        self.max_withdraw = 10000
        self.min_withdraw = 100

    def get_balance(self):
        return self.balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"You cannot withdraw it. you cannot withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"this is maximum withdraw, you cannot do {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"here is your amount {amount}")
            print(f'your balance after withdraw {self.balance}')
brac = bank(15000)
brac.withdraw(25)   
brac.withdraw(5000000)
brac.withdraw(1000)
    