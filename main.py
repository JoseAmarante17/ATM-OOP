'''
Author: Jose Amarante
Date : 7/14/2021
'''

from Account import *
from AMT import *
import time
import datetime

# used to retireve current date
today = datetime.datetime.now()
totalDay = (today.strftime(f"%I:%M:%S %p on {today.day}, %B the %d,%Y "))


def access():
    # Dictionary containing Pins and Credit Card Numbers. The latter is the key and the former is the value
    cardAccess = {
        "1234 5678 9012 1234": "1234",
        "1478 8523 6985 2314": "2582"
    }

    # We ask user in input card number
    # Check is card number is in dictionary
    print("\n\tBank Of Jose")
    print("-------------------------")
    cardUser = input("\nEnter your Credit/Debit Card or input the numbers: ")

    if cardUser not in cardAccess:
        print("Information is not valid, try again later")

    elif cardUser in cardAccess:
        # Checks if what the user inputed is in the dictionary
        # If not found it ask the user to input it again and checks for that value
        count = 0

        while count < 3:
            pinUser = input("Enter your pin: ")

            if pinUser not in cardAccess[cardUser]:
                print(
                    f"Information not valid. You have {3-(count+1)} tries left.\n")
                count = +1

            elif pinUser in cardAccess[cardUser]:
                break

        if count == 3:
            print(
                "Information was invalid and we have locked your account until further notice.")
        else:
            bank()

def bank():

    # loading
    print("loading...")
    time.sleep(1)
    print("loading...")
    time.sleep(1)
    print("\n")
    # call the classes and pass attributes
    account1 = AMT("Jose Amarnte", "74856",500.00,totalDay,'T1423')

    # Prints
    account1.display()

    print("\nTHANK YOU FOR VISING BANK OF JOSE")
    print("\tPLEASE COME AGAIN\n")



def main():
    # Checks if the user credentials are correct
    access()

main()
