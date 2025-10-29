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
        print("Here is a list of the features offered by this application: \n 1. ")
    elif optionChosen == 2:
        print(f"{name}, what problem are you facing today?")
        problem = int(input("Please choose from the following options: \n 1. Connectivity Issues \n 2. Typos in website"))
        problemOption = int(input("Enter the number of which problem you are facing: "))
    elif optionChosen == 3:
        print(f"{name}, what feedback do you have for the app?")
        feedback = input("Enter feedback here: ")
    elif optionChosen == 4:
        print("Well, goodbye!  Ending conversation now.")
        isRunning = False
        sys.exit()
