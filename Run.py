import torch
import torchhd
import numpy
import random
import Controller
import Globals
# import matplotlib
# matplotlib.use('TkAgg',force=True)
# from matplotlib import pyplot as plt
# print("Switched to:",matplotlib.get_backend())



def main():
    # Preamble and initial option selection
    print("")
    print("----------------------------------------")
    print("----------------------------------------")
    print("Welcome to CPSS Sim!")
    print("----------------------------------------")
    print("What would you like to do?")
    print("# (1) Generate random people and social network with random interests")
    print("# (2) Generate based on SM data - Note empty integrated brains")
    print("(3) Generate based on Test data - Mini5 Test & Dictionary")
    print("(4) Generate based on Test SM + Brain data - AI20 Test, no dictionary")
    setupOption= input("Choose Setup Option: ")
    print("You Selected " + setupOption)
    print("----------------------------------------")

    # Setup Option division
    if setupOption == "1":
        # Create Random Network
        print("Unfinished. Not avail.")
        main()
    elif setupOption == "2":
        # Create Network from Input
        print("Unable to do option 2 at this time")
        main()
    elif setupOption == "3":
        # Create Network from Test Input
        Controller.createMiniTestSim()
        print("SUCCESS: Test Sim Setup")
    elif setupOption == "4":
        # Create Network from AI20 Dataset with no dictionary file
        Controller.createAI20TestSim()
        print("SUCCESS: Test Sim Setup")
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