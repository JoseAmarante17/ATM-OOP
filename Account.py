"""
The Account class is what lets the user decide on what do to in the account.
Lets user pick which account they want to do something to
"""

# creates the class Account


class Account():
    def __init__(self, name, accountNum, balance):
        self.name = name
        self.accountNum = accountNum
        self.balance = balance

    # Sets value
    def deposit(self, depositAmt):
        self.depositAmt = depositAmt

    def withdraw(self, withdrawAmt):
        self.withdrawAmt = withdrawAmt

    # get values
    def get_deposit(self,depositAmt):
        self.balance = (depositAmt) + (self.balance)
        return (self.balance)

    def get_withdraw(self,withdrawAmt):
        self.balance = self.balance - withdrawAmt  
        return self.balance

    def get_balance(self):
        return self.balance

    def get_accountNum(self):
        return self.accountNum

    def get_name(self):
        return self.name
