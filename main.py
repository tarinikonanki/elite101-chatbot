import sys

login_list = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_list.add(username,password)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if (username,password) in login_list:
        print("You are successfully logged in!")

print("Welcome to the bank! Are you ready to learn information about this banking institution?")

name = input("Enter your name: ")
feedback = ""
isRunning = True

print(f"Well, {name}, it's great to meet you! How can I help you today?")

while(isRunning):
    print("Please choose from the following options: \n 1. Get account type information \n 2. Register for an account \n 3. Access your preexisting account \n 4. Exit conversation")

    optionChosen = int(input("Enter the number of which option you choose: "))

    if optionChosen == 1:
        print("Here is a list of the account types offered by this bank: \n 1. Checking Account \n 2. Savings Account \n 3. Money Market Account \n 4. Certificate of Deposit")
        infoOption = int(input("Choose a number from the options above to get more information on the type of account: "))
        if infoOption == 1:
            print("Checking Accounts are accounts")
        elif infoOption == 2:
            print("Checking Accounts are accounts")
        elif infoOption == 3:
            print("Checking Accounts are accounts")
        elif infoOption == 4:
            print("Checking Accounts are accounts")
    elif optionChosen == 2:

        print(f"{name}, what type of account would you like to register for?")
        account_type = int(input("Type the number choice from the following: \n 1. Checking Account \n 2. Savings Account \n 3. Money Market Account \n 4. Certificate of Deposit"))
        problemOption = int(input("Enter the number of which problem you are facing: "))
    elif optionChosen == 3:
        login()

    elif optionChosen == 4:
        print("Well, goodbye!  Ending conversation now.")
        isRunning = False
        sys.exit()
