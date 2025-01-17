import Globals
import Setup
import SinglePersonBrainQueries
import TwoPersonBrainQueries

# The Person.py, Filters.py, Comms.py and Network.py modules SHOULD be changeable/modular as long as they can process these controller calls.

# The controller should be the main glue between all the other py modules.

# ----------------------------------------------
# Main Controller
# ----------------------------------------------


def mainMenu():
    run = True
    while run:
        # Preamble and initial option selection
        print("----------------------------------------")
        print("What would you like to do?")
        print("----------------------------------------")
        print("(1) Query Brain Data")
        print("# (2) Query Social Media Data")
        print("# (3) Query Brain & Social Media Data")
        print("# (4) Get Structural Data")
        print("# (5) Run Simulation")
        mainMenuOp= input("Choose Option: ")
        print("You Selected " + mainMenuOp)

        # Setup Option division
        if mainMenuOp == "1":
            # Query Vector Data
            menu_1_vectorQueryBrainData()
        elif mainMenuOp == "2":
            print("Not started")
        elif mainMenuOp == "3":
            print("Not started")
        elif mainMenuOp == "4":
            print("Not started")
        elif mainMenuOp == "5":
            # Create Network from Input
            print("Not started")
        else:
            print("Error with setup option selected. Try again")
            

# ----------------------------------------------
# 1. Vector Query Brain Data Menus
# ----------------------------------------------

def menu_1_vectorQueryBrainData():
    print("----------------------------------------")
    print(" Vector Query Brain Data Menu")
    print("----------------------------------------")
    # Preamble and initial option selection
    print("What would you like to Query?\n")
    print("(1) Single Person Queries")
    print("(2) Two Person Queries")
    print("# (3) Whole Network Queries")
    print("# (B) Back ")
    # print("-- Subset of Network Queries INCOMPLETE / STRETCH --")
    # print("# (S1) What does this network subset think about a topic?")
    # print("#(S2) What is the variability of the network subset's feeling on a topic? ")
    
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    # Setup Option division
    if queryData == "1":
        menu_1_1_singlePersonBrainQuery()
    elif queryData == "2":
        menu_1_2_twoPersonBrainQuery()
        print("Not started.")
    elif queryData == "3":
        menu_1_3_wholeNetworkBrainQuery()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

def menu_1_1_singlePersonBrainQuery():
    # for querying one person
    print("----------------------------------------")
    print("Single Person Queries")
    print("----------------------------------------")
    print("(1) Check if a person contains a paired association. e.g. likes AND horse")
    print("(2) How many paired associations for a person? e.g. likes AND horse")
    print("(3) How many instances of an atomic concept in a person. e.g. horse")
    print("(4) What is the range of feelings a person has about a concept? e.g. horse")
    print("(5) What are the strongest feelings a person has about a concept? e.g. horse")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)
    
    if queryData == "1":
        SinglePersonBrainQueries.doesPersContainPair()
    elif queryData == "2":
        SinglePersonBrainQueries.howManyDoesPersContainPair()
    elif queryData == "3":
        SinglePersonBrainQueries.personNumAtomic()
    elif queryData == "4":
        SinglePersonBrainQueries.personRangeAtomic()
    elif queryData == "5":
        SinglePersonBrainQueries.personRankedRangeAtomic()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

    print("----------------------------------------")

def menu_1_2_twoPersonBrainQuery():
    # For querying two people
    print("----------------------------------------")
    print("Two Person Brain Queries")
    print("----------------------------------------")
    print("(1) What is the general belief similarity between two people? Return value")
    print("(2) What topic is the most similar between two people? Return topic")
    print("(3) For a given topic, what is the similarity in belief between two people? Return value")
    print("(4) For a given topic, what associations are the most similar between two people? Return topic")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)


    if queryData == "1":
        TwoPersonBrainQueries.twoPersSimilarityVal()
    elif queryData == "2":
        TwoPersonBrainQueries.twoPersCommonTopic()
    elif queryData == "3":
        TwoPersonBrainQueries.getBeliefDifference_Val()
    elif queryData == "4":
        TwoPersonBrainQueries.getBeliefSimilarity_Topic()
        print("In prog.")
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")
    
def menu_1_3_wholeNetworkBrainQuery():
    # Menu for querying the whole network
    print("----------------------------------------")
    print("Whole Network Brain Queries")
    print("----------------------------------------")
    print("# (1) What does the entire network feel about a topic? on average")
    print("# (2) What is the variability of the entire network's feeling on a topic? ")
    print("# (B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    if queryData == "1":
        print("tbc")
    elif queryData == "2":
        print("tbc")
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")
    print("NOT COMPLETED")





    # print("-- Subset of Network Queries INCOMPLETE / STRETCH --")
    # print("# (S1) What does this network subset think about a topic?")
    # print("#(S2) What is the variability of the network subset's feeling on a topic? ")
    
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    # Setup Option division

# ----------------------------------------------
# 2. Query Social Media Data
# ----------------------------------------------


# ----------------------------------------------
# 3. Query Brain and Social Media Data
# ----------------------------------------------

# ----------------------------------------------
# 4. Get Structural Data 
# ----------------------------------------------
def menu_getStructuralData():
    print("To do")

def getNetworkData():
    # Returns the network
    print("To do")


def exportNetworkData():
    # Returns a file representing the network
    print("to do")

def getAllPersonData():
    # Returns all Persons
    print("To do")

def exportAllPersonData():
    # Returns a file representing all Persons
    print("to DO")



# ----------------------------------------------
# 5. Run Simulation 
# ----------------------------------------------




# ----------------------------------------------
# Add Person Data - Stretch Goal
# ----------------------------------------------

# def AddNewPersonsEdgesDescriptorsPairs():
#     # Add new Persons, then Data, then Edges, then Pairs
#     print("to do")
#     AddNewPersons()
#     AddNewPersonDescriptors()
#     AddNewNetworkEdges()
#     AddNewVectorPairs()

# def AddPersonFilters():
#     # Add person filters to specified Person objects
#     print("To Do")

# def AddNewNetworkEdges():
#     # Add network edges to existing Person objects
#     print("To Do")

# def AddNewPersons():
#     # Add new 
#     print("To Do")

# def AddNewPersonDescriptors():
#     # Add new descriptors to Person objs
#     print("to do")

# def AddNewVectorPairs():
#     # Add new vector pairs to Person Objs
#     print("to do")

# ----------------------------------------------
# Edit Person Data - Stretch Goal
# ----------------------------------------------



# ----------------------------------------------
# Uncategorised
# ----------------------------------------------

def main():
    print("Controller main")

if __name__ == "__main__":
    main()