import torch
import torchhd
import numpy
import random
import Controller
import Globals
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
print("Switched to:",matplotlib.get_backend())



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
        #Controller.createBaseBrain()
        Controller.createTestSim()
        print("Working on atm!")
    else:
        print("Error with setup option selected. Try again")
        main() 


    # Note that in this current model we keep the number of atomic vectors (i.e. people and words) static.

    #tessTest()


    Controller.mainMenu()

    print("Run END")


def tessTest():
    # bindTop = torch.max(Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"])
    # bundleTop= torch.max(Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"])
    # print("here")
    print("hi")


if __name__ == "__main__":
    main()