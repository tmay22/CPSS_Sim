import torch
import torchhd
import numpy
import random
import Controller



def main():
    # Preamble and initial option selection
    print("Welcome to CPSS Sim!\n")
    print("(1) Generate random people and social network with random interests")
    print("(2) Generate based on SM data")
    print("(3) Generate based on Test data")
    setupOption= input("Choose Setup Option: \n 1. Random \n 2. SM Data \n 3. Test Data \n...etc \n")
    print("You Selected " + setupOption)

    # Setup Option division
    if setupOption == "1":
        # Create Random Network
        print("Unfinished but sure")
    elif setupOption == "2":
        # Create Network from Input
        print("Unable to do option 2 at this time")
        exit()
    elif setupOption == "3":
        # Create Network from Input
        Controller.createBaseBrain()
        Controller.createTestSim()
        print("Working on atm!")
    else:
        print("Error with setup option selected. Try again")
        main() 

    # Do setup

    

    # If OP 1

    # If OP 2

    

    Controller.mainMenu()

    print("Run END")


if __name__ == "__main__":
    main()