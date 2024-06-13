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
        path = getSimPath()
        Setup.buildSim(path)
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
    elif simDataOption == "2":
        print("Input a path, with a / at the end")
        pathOption= input("Enter path: ")
        path=pathOption
    else:
        print("Error. Option does not exist")
    return path




if __name__ == "__main__":
    main()