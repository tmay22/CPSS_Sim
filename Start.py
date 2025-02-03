import torch
import torchhd
import numpy
import random
import Globals
import Setup
import Controller

def main():
    print("")
    print("----------------------------------------")
    print("----------------------------------------")
    print("Welcome to CPSS Sim!")
    print("----------------------------------------")
    print("What would you like to do?")
    print("(1) Create Sim from Input Data")
    print("(2) Generate Ficticious Sim - UNFINISHED / STRETCH")
    setupOption= input("Choose Setup Option: ")
    print("You Selected " + setupOption)
    print("----------------------------------------")

    # Setup Option division
    if setupOption == "1":
        # Create Sim from Data
        path, historyOption = getSimPath()
        Setup.buildSim(path,historyOption)
        Controller.mainMenu()

    elif setupOption == "2":
        # Generate Sim
        print("Unable to do option 2 at this time")
        
    
def getSimPath():
    print("Would you like to create the default sim or provide custom data")
    print("(1) Default")
    print("(2) Custom Data - UNTESTED?")
    simDataOption= input("Choose Data Option: ")
    print("You Selected " + simDataOption)
    print("----------------------------------------")

    if simDataOption == "1":
        path = "DataSets/20AI/"
        historyOption = True
    elif simDataOption == "2":
        print("Input a path, with a / at the end")
        pathOption= input("Enter path: ")
        path=pathOption
        print("Do you have historical social media data to import?")
        print("(0) NO")
        print("(1) YES")
        histOp= input("Choose Option: ")
        print("You Selected " + histOp)
        print("----------------------------------------")
        if histOp == 1:
            historyOption == True
        else:
            historyOption == False
    else:
        print("Error. Option does not exist")
    return path, historyOption




if __name__ == "__main__":
    main()