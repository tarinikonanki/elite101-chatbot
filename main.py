import sys
import time

login_list = {}

def register(accountType):
    username = input("Enter username: ")
    password = input("Enter password: ")
    starting_balance = float(input("Enter how much money you want to initially input: "))
    login_list[username] = [password,accountType,starting_balance]
    return f"You have created a {login_list[username][1]} with a balance of ${login_list[username][2]}."

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if (username) in login_list and login_list[username][0] == password:
        print("You are successfully logged in!")
    return f"You have a {login_list[username][1]} with a balance of ${login_list[username][2]}."

print("Welcome to the bank! Are you ready to learn information about this banking institution?")

name = input("Enter your name: ")
age = int(input("How old are you? "))
feedback = ""
isRunning = True

print(f"Well, {name}, it's great to meet you! How can I help you today?")

time.sleep(1)

while(isRunning):
    print("Please choose from the following options: \n 1. Get account type information \n 2. Register for an account \n 3. Access your preexisting account \n 4. Exit conversation")

    optionChosen = int(input("Enter the number of which option you choose: "))

    time.sleep(1)

    if optionChosen == 1:
        print("Here is a list of the account types offered by this bank: \n 1. Checking Account \n 2. Savings Account \n 3. Money Market Account \n 4. Certificate of Deposit")
        infoOption = int(input("Choose a number from the options above to get more information on the type of account: "))
        if infoOption == 1:
            print("Checking Accounts are accounts where the money you put in can be withdrawn later to spend easily.")
        elif infoOption == 2:
            print("Savings Accounts are accounts where you deposite money that earns a small amount of interest, allowing you to save for emergencies or long-term goals.")
        elif infoOption == 3:
            print("Money Market Accounts are accounts that are hybrids of savings and checkings accounts, having limited checking account features like debit card access while having higher interest rates than regular savings accounts.")
        elif infoOption == 4:
            print("Certificates of Deposit are savings accounts that hold money for a certain specified amount of time and have fixed interest rates.")
    elif optionChosen == 2:
        if age >= 18:
            print(f"{name}, what type of account would you like to register for?")
            account_num = int(input("Type the number choice from the following: \n 1. Checking Account \n 2. Savings Account \n 3. Money Market Account \n 4. Certificate of Deposit \n"))
            account_type = ""
            if account_num == 1:
                account_type = "Checking Account"
            elif account_num == 2:
                account_type = "Savings Account"
            elif account_num == 3:
                account_type = "Money Market Account"
            elif account_num == 4:
                account_type = "Certificate of Deposit"
            time.sleep(1)
            print("Create login to register your account.")
            print(register(account_type))
            print("You have successfully registered for an account!")
        elif age < 18:
            print(f"{name}, since you are only {age} years old, you are ineligible to register for an account.")
    elif optionChosen == 3:
        if age >= 18:
            print(f"Login to your account, {name}!")
            print(login())
        elif age < 18:
            print(f"{name}, since you are only {age} years old, you are too young to have an account and cannot log in.")
    elif optionChosen == 4:
        print("Well, goodbye and have a great day!  Ending conversation now.")
        isRunning = False
        sys.exit()
    time.sleep(1)
    print(f"{name}, how else can I help you today?")
    time.sleep(1)
