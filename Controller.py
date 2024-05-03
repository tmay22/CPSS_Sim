import Globals
import Setup

# The Person.py, Filters.py, Comms.py and Network.py modules SHOULD be changeable/modular as long as they can process these controller calls.

# The controller should be the main glue between all the other py modules.

# ----------------------------------------------
# Main Controller
# ----------------------------------------------


def mainMenu():
    print("Post-setup, Run sends you here.")


# ----------------------------------------------
# Setup.py Pointers
# ----------------------------------------------

def createBaseBrain():
    Setup.createBrainVectorBase()

def setupNetwork():
    print("setupNetwork")

def createTestSim():
    Setup.createTestSim()

# ----------------------------------------------
# Person.py Pointers
# ----------------------------------------------


# ----------------------------------------------
# Comms.py Pointers
# ----------------------------------------------


# ----------------------------------------------
# Filters.py Pointers
# ----------------------------------------------


# ----------------------------------------------
# Network.py Pointers
# ----------------------------------------------


# ----------------------------------------------
# Uncategorised
# ----------------------------------------------

def main():
    print("Controller main")

if __name__ == "__main__":
    main()