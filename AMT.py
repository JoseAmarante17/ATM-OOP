"""
The ATM Transaction class inherits the Account class attributes
"""

from Account import *


class AMT(Account):
    def __init__(self, name, accountNum, balance, date, transcID):
        super().__init__(name, accountNum, balance)
        self.date = date
        self.transcID = transcID

    # getter
    def get_date(self,date):
        self.date = date
        return self.date

    def get_transcID(self, transcID):
        self.transcID = transcID
        return self.transcID

    # DISPLAYS the in formation

    def display(self):
        count = 0
        while count == 0:
            # Menu
            print("\n\tBank Of Jose")
            print("-------------------------")
            print(f"Transaction ID: {self.transcID}    Date: {self.date}\n")
            print("1) Account Details")
            print("2) View Balance")
            print("3) Deposit")
            print("4) Withdraw")
            print("5) Quit")

            # User Choice
            userChoice = input("\nEnter your choice: ")

            if userChoice == "1":
                print(f"\n\tAccount Details")
                print("--------------------------------")
                print(f"Account Number: {Account.get_accountNum(self)}")
                print(f"Name: {Account.get_name(self)}\n")

            elif userChoice == "2":
                print("\n\tBalance")
                print("-------------------")
                print(f"Balance: ${Account.get_balance(self):,.2f}")
            
            elif userChoice == "3":
                print(f"\n\tDeposit")
                print("--------------------------")
                amount = float(input("\nEnter the amount you want to deposit: $"))
                Account.deposit(self,amount)

                print(f"Your current balance is: ${Account.get_deposit(self,amount):,.2f}\n")

            elif userChoice == "4":
                print(f"\n\tWithdraw")
                print("--------------------------")
                amount = float(input("\nEnter the amount you want to withdraw: $"))
                Account.withdraw(self,amount)
                print(f"Your current balance is: ${Account.get_withdraw(self,amount):,.2f}\n")

            elif userChoice == "5":
                break



            
