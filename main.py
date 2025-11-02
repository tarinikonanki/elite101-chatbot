import sys

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
    elif optionChosen == 2:
        print(f"{name}, what type of account would you like to register for? Type the number choice from the following: ")
        problem = int(input("Please choose from the following options: \n 1. Connectivity Issues \n 2. Typos in website"))
        problemOption = int(input("Enter the number of which problem you are facing: "))
    elif optionChosen == 3:
        username = input(f"{name}, what username do you want to log in with?")
        feedback = input("Enter feedback here: ")
    elif optionChosen == 4:
        print("Well, goodbye!  Ending conversation now.")
        isRunning = False
        sys.exit()
