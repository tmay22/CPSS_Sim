import Globals
import Setup
import SinglePersonBrainQueries
import TwoPersonBrainQueries
import WholeNetworkBrainQueries
import VectorFunction_Brain
import SinglePersonSocialMediaQueries
import TwoPersonSocialMediaQueries
import WholeNetworkSocialMediaQueries
import SinglePersonCompareBrainSocialMediaQueries
import TwoPersonCompareBrainSocialMediaQueries
import WholeNetworkCompareBrainSocialMediaQueries
import Visualise
import Simulator
# I WANT TO ADD A COMPARE SM AND BRAIN DATA FOR FUNSIES

# The Person.py, Filters.py, Comms.py and Network.py modules SHOULD be changeable/modular as long as they can process these controller calls.

# The controller should be the main glue between all the other py modules.

# ----------------------------------------------
# Main Controller
# ----------------------------------------------

# THERES SOMETHING STILL WRONG WITH INTERATCIONS
# I THINK YOU NEED TO RE-WRITE TO HAVE SOURCE, DATAFLOW, DESTINATION.
def mainMenu():
    run = True
    while run:
        # Preamble and initial option selection
        print("----------------------------------------")
        print("What would you like to do?")
        print("----------------------------------------")
        print("(1) Query Brain Data")
        print("(2) Query Social Media Data")
        print("(3) Compare Brain & Social Media Data")
        print("(4) Visualise")
        print("# (5) Run Simulation")
        print("# (6) Test")
        mainMenuOp= input("Choose Option: ")
        print("You Selected " + mainMenuOp)

        # Setup Option division
        if mainMenuOp == "1":
            # Query Vector Data
            menu_1_vectorQueryBrainData()
        elif mainMenuOp == "2":
            menu_2_vectorQuerySocialMedia()
        elif mainMenuOp == "3":
            menu_3_vectorQueryCompareBrainSocialMedia()
        elif mainMenuOp == "4":
            menu_4_visualise()
        elif mainMenuOp == "5":
            menu_5_Simulate()
            print("Not started")
        elif mainMenuOp == "6":
            # Test
            menu_6_Test()
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
    print("(3) Whole Network Queries")
    print("(B) Back ")
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
    print("(6) What are the strongest feelings a person has generally?")
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
    elif queryData == "6":
        SinglePersonBrainQueries.personRankedRangePairsGeneral()
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
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")
    
def menu_1_3_wholeNetworkBrainQuery():
    # Menu for querying the whole network
    print("----------------------------------------")
    print("Whole Network Brain Queries")
    print("----------------------------------------")
    print("(1) What does the entire network feel about a topic? Show top 5 strongest")
    print("(2) What is the standard deviation of the entire network's variant feelings on a topic? ")
    print("(3) What people are most strongly associated with two topics? ")
    print("(4) What is the average similarity of people who share a common topic pair?")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    if queryData == "1":
        WholeNetworkBrainQueries.getNetworkBeliefOnTopic()
    elif queryData == "2":
        WholeNetworkBrainQueries.getNetworkSDBeliefOnTopic_Val()
    elif queryData == "3":
        WholeNetworkBrainQueries.getPeopleAssociatedWithBind_brain()
    elif queryData == "4":
        WholeNetworkBrainQueries.howSimilarArePeopleWithBind()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

# :)




    # Setup Option division

# ----------------------------------------------
# 2. Query Social Media Data
# ----------------------------------------------

def menu_2_vectorQuerySocialMedia():
    print("----------------------------------------")
    print(" Vector Query Social Media Data Menu")
    print("----------------------------------------")
    # Preamble and initial option selection
    print("What would you like to Query?\n")
    print("(1) Single Person Social Media Queries")
    print("(2) Two Person Social Media Data Queries")
    print("(3) Whole Social Media Network Queries")
    print("(B) Back ")
    # print("-- Subset of Network Queries INCOMPLETE / STRETCH --")
    # print("# (S1) What does this network subset think about a topic?")
    # print("#(S2) What is the variability of the network subset's feeling on a topic? ")
    
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    # Setup Option division
    if queryData == "1":
        menu_2_1_singleSocialMediaQueries()
    elif queryData == "2":
        menu_2_2_twoPersonSocialMediaQueries()
    elif queryData == "3":
        menu_2_3_wholeNetworkSocialMediaQueries()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

def menu_2_1_singleSocialMediaQueries():
    # for querying one person
    print("----------------------------------------")
    print("Single Person Social Media Queries")
    print("----------------------------------------")
    print("(1) Check if a person contains a paired association. e.g. likes AND horse")
    print("(2) How many paired associations for a person? e.g. likes AND horse")
    print("(3) How many instances of an atomic concept in a person. e.g. horse")
    print("(4) What is the range of feelings a person has about a concept? e.g. horse")
    print("(5) What are the strongest feelings a person has about a concept? e.g. horse")
    print("(6) What are the strongest feelings a person has generally on social media?")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)
    
    if queryData == "1":
        SinglePersonSocialMediaQueries.doesPersContainPair()
    elif queryData == "2":
        SinglePersonSocialMediaQueries.howManyDoesPersContainPair()
    elif queryData == "3":
        SinglePersonSocialMediaQueries.personNumAtomic()
    elif queryData == "4":
        SinglePersonSocialMediaQueries.personRangeAtomic()
    elif queryData == "5":
        SinglePersonSocialMediaQueries.personRankedRangeAtomic()
    elif queryData == "6":
        SinglePersonSocialMediaQueries.personRankedRangePairsGeneral_sm()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

    print("----------------------------------------")

def menu_2_2_twoPersonSocialMediaQueries():
    # For querying two people
    print("----------------------------------------")
    print("Two Person Social Media Queries")
    print("----------------------------------------")
    print("(1) What is the general belief similarity between two people? Return value")
    print("(2) What topic is the most similar between two people? Return topic")
    print("(3) For a given topic, what is the similarity in belief between two people? Return value")
    print("(4) For a given topic, what associations are the most similar between two people? Return topic")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)


    if queryData == "1":
        TwoPersonSocialMediaQueries.twoPersSimilarityVal()
    elif queryData == "2":
        TwoPersonSocialMediaQueries.twoPersCommonTopic()
    elif queryData == "3":
        TwoPersonSocialMediaQueries.getBeliefDifference_Val()
    elif queryData == "4":
        TwoPersonSocialMediaQueries.getBeliefSimilarity_Topic()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")
    
def menu_2_3_wholeNetworkSocialMediaQueries():
    # Menu for querying the whole network
    print("----------------------------------------")
    print("Whole Network Social Media Queries")
    print("----------------------------------------")
    print("(1) What does the entire network feel about a topic? Show top 5 strongest")
    print("(2) What is the standard deviation of the entire network's variant feelings on a topic? ")
    print("(3) What people are most strongly associated with two topics? ")
    print("(4) What is the average similarity of people who share a common topic pair?")
    
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    if queryData == "1":
        WholeNetworkSocialMediaQueries.getNetworkBeliefOnTopic()
    elif queryData == "2":
        WholeNetworkSocialMediaQueries.getNetworkSDBeliefOnTopic_Val()
    elif queryData == "3":
        WholeNetworkSocialMediaQueries.getPeopleAssociatedWithBind_sm()
    elif queryData == "4":
        WholeNetworkSocialMediaQueries.howSimilarArePeopleWithBind()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

# :)



# ----------------------------------------------
# 3. Query Brain and Social Media Data
# ----------------------------------------------

def menu_3_vectorQueryCompareBrainSocialMedia():
    print("----------------------------------------")
    print(" Vector Query Compare Brain and Social Media Data Menu")
    print("----------------------------------------")
    # Preamble and initial option selection
    print("What would you like to Query?\n")
    print("(1) Single Person Queries")
    print("(2) Two Person  Queries")
    print("(3) Whole Network Queries")
    print("(B) Back ")

    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    # Setup Option division
    if queryData == "1":
        menu_3_1_singleCompareBrainSocialMediaQueries()
    elif queryData == "2":
        menu_3_2_twoPersonCompareBrainSocialMediaQueries()
    elif queryData == "3":
        menu_3_3_wholeNetworkCompareBrainSocialMediaQueries()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

def menu_3_1_singleCompareBrainSocialMediaQueries():
    # for querying one person
    print("----------------------------------------")
    print("Single Person Brain vs Social Media Queries")
    print("----------------------------------------")
    print("(1) Check if a person contains a paired association. e.g. likes AND horse")
    print("(2) How many paired associations for a person? e.g. likes AND horse")
    print("(3) How many instances of an atomic concept in a person. e.g. horse")
    print("(4) What is the range of feelings a person has about a concept? e.g. horse")
    print("(5) What are the strongest feelings a person has about a concept? e.g. horse")
    print("(6) Compare the difference between a person's personal profile and their social media profile")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)
    
    if queryData == "1":
        SinglePersonCompareBrainSocialMediaQueries.doesPersContainPair()
    elif queryData == "2":
        SinglePersonCompareBrainSocialMediaQueries.howManyDoesPersContainPair()
    elif queryData == "3":
        SinglePersonCompareBrainSocialMediaQueries.personNumAtomic()
    elif queryData == "4":
        SinglePersonCompareBrainSocialMediaQueries.personRangeAtomic()
    elif queryData == "5":
        SinglePersonCompareBrainSocialMediaQueries.personRankedRangeAtomic()
    elif queryData == "6":
        SinglePersonCompareBrainSocialMediaQueries.comparePersonalSm()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

    print("----------------------------------------")

def menu_3_2_twoPersonCompareBrainSocialMediaQueries():
    # For querying two people
    print("----------------------------------------")
    print("Two Person Brain vs Social Media Queries")
    print("----------------------------------------")
    print("(1) What is the general belief similarity between two people? Return value")
    print("(2) What topic is the most similar between two people? Return topic")
    print("(3) For a given topic, what is the similarity in belief between two people? Return value")
    print("(4) For a given topic, what associations are the most similar between two people? Return topic")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)


    if queryData == "1":
        TwoPersonCompareBrainSocialMediaQueries.twoPersSimilarityVal()
    elif queryData == "2":
        TwoPersonCompareBrainSocialMediaQueries.twoPersCommonTopic()
    elif queryData == "3":
        TwoPersonCompareBrainSocialMediaQueries.getBeliefDifference_Val()
    elif queryData == "4":
        TwoPersonCompareBrainSocialMediaQueries.getBeliefSimilarity_Topic()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")
    
def menu_3_3_wholeNetworkCompareBrainSocialMediaQueries():
    # Menu for querying the whole network
    print("----------------------------------------")
    print("Whole Network Brain vs Social Media Queries")
    print("----------------------------------------")
    print("(1) What does the entire network feel about a topic? Show top 5 strongest")
    print("(2) What is the standard deviation of the entire network's variant feelings on a topic? ")
    print("(3) What people are most strongly associated with two topics? ")
    print("(4) What is the average similarity of people who share a common topic pair?")
    print("(B) Back ")
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    if queryData == "1":
        WholeNetworkCompareBrainSocialMediaQueries.getNetworkBeliefOnTopic()
    elif queryData == "2":
        WholeNetworkCompareBrainSocialMediaQueries.getNetworkSDBeliefOnTopic_Val()
    elif queryData == "3":
        WholeNetworkCompareBrainSocialMediaQueries.getPeopleAssociatedWithBind()
    elif queryData == "4":
        WholeNetworkCompareBrainSocialMediaQueries.howSimilarArePeopleWithBind()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")

# :)


# ----------------------------------------------
# 4. Visualise
# ----------------------------------------------
def menu_4_visualise():
    print("----------------------------------------")
    print(" Visualise your Vectors")
    print("----------------------------------------")
    # Preamble and initial option selection
    print("What would you like to Visualise?\n")
    print("(1) People's Brain Distribution")
    print("(2) People's Social Media Distribution")
    print("(3) People's Brain and Social Media Distribution")
    print("(B) Back ")
 
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    # Setup Option division
    if queryData == "1":
        Visualise.visualiseAllPersons_brain()
    elif queryData == "2":
        Visualise.visualiseAllPersons_sm()
    elif queryData == "3":
        Visualise.compareAllPersonsBrainVsSm()
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")


# ----------------------------------------------
# X. Get Structural Data 
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

def menu_5_Simulate():
    print("----------------------------------------")
    print(" Simulation")
    print("----------------------------------------")
    # Preamble and initial option selection
    print("What would you like to Visualise?\n")
    print("(1) Test Backbone")
    print("(2) Direct message")
    print("(3) vvvn")
    print("(B) Back ")
 
    queryData= input("Choose Option: ")
    print("You Selected " + queryData)

    # Setup Option division
    if queryData == "1":
        Simulator.simulatorBackbone()
    elif queryData == "2":
        Simulator.simulator_directMessage()
    elif queryData == "3":
        print(f"Make a post and see effect - NOT DONE YET")
    elif queryData == "B" or queryData == "b":
        return 
    else:
        print("Error with setup option selected. Try again")



def menu_6_Test():
    myString = "I love riding horses, they are so fun and make me happy!"
    VectorFunction_Brain.convertStringToBundleOfBinds(myString)
    print("here")


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