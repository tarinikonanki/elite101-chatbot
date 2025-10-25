import sys

print("Welcome to the app! Are you ready to learn information about this application?")

name = input("Enter your name: ")
feedback = ""

print(f"Well, {name}, it's great to meet you! How can I help you today?")

print("Please choose from the following options: \n 1. Check application features \n 2. Ask questions \n 3. Submit feedback \n 4. Exit conversation")

optionChosen = int(input("Enter the number of which option you choose: "))

if optionChosen == 1:
    print("Here is a list of the features offered by this application: \n 1. ")
elif optionChosen == 2:
    print(f"{name}, what problem are you facing today?")
    problem = int(input("Please choose from the following options: "))
elif optionChosen == 3:
    print(f"{name}, what feedback do you have for the app?")
    feedback = input("Enter feedback here: ")
elif optionChosen == 4:
    print("Well, goodbye!  Ending conversation now.")
    sys.exit()