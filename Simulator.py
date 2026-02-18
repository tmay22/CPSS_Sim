import Globals
import random
import Checks
import VectorFunction_Brain
import torch
import torchhd
import numpy
import MediaObjects
import copy
import Visualise

# RUns the simulations
def simulatorBackbone():
    running = True
    while running == True:

        # Find active people
        persOnList = []
        for persId, personObj in Globals.personDict.items():
            edgeCommRate = personObj.Behaviours.edgeCommunication
            edgeCommRate = edgeCommRate/100
            randomCommRate = random.random()
            # If the person is active, add them to the personOnList
            if edgeCommRate >= randomCommRate:
                persOnList.append(personObj)
        
        # Find active edges
        edgeOnList = []
        for person in persOnList:
            persEdgeList = person.edgeList
            for edge in persEdgeList:
                personOne = edge.connections[0]
                personTwo = edge.connections[1]
                personOneObj = Globals.personDict[personOne]
                personTwoObj = Globals.personDict[personTwo]
                if personOneObj in persOnList and personTwoObj in persOnList:
                    if edge not in edgeOnList:
                        edgeOnList.append(edge)



        Globals.currentTime = Globals.currentTime + 1

# RUns the simulations
def simulator_directMessage():
    # CHeck general similarity between two people
    print("----------------------------------------")
    print("Send a direct message between two people and see outcome")
    print("----------------------------------------")
    # COllect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
    message = input("Give message ")
    print("Your input: " + message)

    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    
    messageVector = VectorFunction_Brain.convertStringToBundleOfBinds(message)

    print("----------------------------------------")
    running = True
    while running == True:

        # SETUP
        
        
        personOne = Globals.personDict[f1_personId]
        personTwo = Globals.personDict[f2_personId]

        # Create media
        newMessage = MediaObjects.Media(None, Globals.currentTime, f1_personId,message)

        personOneBrain_original = personOne.persBundle.clone().detach()
        personTwoBrain_original = personTwo.persBundle.clone().detach()

        # NEXT TIMESTEP
        Globals.currentTime = Globals.currentTime + 1

        # Create interaction
        newInteraction = MediaObjects.Interaction(None, Globals.currentTime, f1_personId, newMessage, f2_personId, None, "Message")

        influenceThreshhold = personTwo.filters.influenceThreshhold
        upperInteractThreshhold = personTwo.filters.upperInteractThreshhold
        lowerInteractThreshhold = personTwo.filters.lowerInteractThreshhold

        # get cosine similarity of message vers person's brain bundle
        cosine = VectorFunction_Brain.compareVectors(personTwoBrain_original, messageVector)
        cosine=cosine.item()
        
        print(f'Cosine of message and person inner state is {cosine}')
        
        # Make changes based on influence
        if cosine >= influenceThreshhold:
            personTwo = influencePerson(personTwo, messageVector)
            print(f'Meets positive influence threshold of {influenceThreshhold} ') 
        
        else:
            print(f'Did not meet positive influence threshold of {influenceThreshhold} ') 
        if cosine >= upperInteractThreshhold:
            print(f'Meets upper interaction threshold of {upperInteractThreshhold}')
            positiveLike(f2_personId, newMessage)
            positiveMessage()
        else:
            print(f'Did not meet upper interaction threshold of {upperInteractThreshhold}')
        if cosine <= lowerInteractThreshhold:
            print(f'Meets lower interaction threshold of {lowerInteractThreshhold}')
            negativeMessage()
            negativeComment()
        else:
            print(f'Did not meet lower interaction threshold of {lowerInteractThreshhold}')

        print('First order of consequence i.e. receiving the message complete.')
        personOneBrain_new = personOne.persBundle
        personTwoBrain_new = personTwo.persBundle

        persOneChanges = VectorFunction_Brain.compareVectors(personOneBrain_new, personOneBrain_original)
        persTwoChanges = VectorFunction_Brain.compareVectors(personTwoBrain_new, personTwoBrain_original)

        print(f'{f1_personId} Brain changes: {persOneChanges}')
        print(f'{f2_personId} Brain changes: {persTwoChanges}')

        preDict = {}
        postDict = {}
        
        preDict[f1_personId] = personOneBrain_original
        preDict[f2_personId] = personTwoBrain_original
        postDict[f1_personId] = personOneBrain_new
        postDict[f2_personId] = personTwoBrain_new
        

        Visualise.visualiseCauseEffect(preDict, postDict)

        running = False

# Adds the messageVector to a person's brain bundle.
def influencePerson(person, messageBundle):
    
    person.updatePersBundle(messageBundle)
    return person

def positiveComment():
    commentRate = 0.25
    chanceComment = random.random()
    if chanceComment <= commentRate:
    # Do positive comment post ->> not sure how to get this data
        print("Positive Comment")
        print("to do positive comment posting")


def positiveMessage():
    messageRate = 0.75
    chanceMessage = random.random()
    if chanceMessage <= messageRate:
    # Do positive message post ->> not sure how to get this data
        print("Positive Message")
        print("to do positive Message posting")

# Have a positive reaction
def positiveLike(sourcePerson, destMedia):
    likeRate = 1.00
    chanceLike = random.random()
    if chanceLike <= likeRate:
        ("Like")
        newInteraction = MediaObjects.Interaction(None, Globals.currentTime, sourcePerson, None, None, destMedia, "Like" )

# Have a negative reaction
def negativeComment():
    commentRate = 0.25
    chanceComment = random.random()
    if chanceComment <= commentRate:
        # Do negative comment post ->> not sure how to get this data
        print("Negative Comment")
        print("to do negative comment posting")

# Have a negative reaction
def negativeMessage():
    rateMessage = 0.50
    chanceMessage = random.random()
    if chanceMessage <= rateMessage:
        # Do negative message  ->> not sure how to get this data
        print("Negative Message")
        print("to do negative message sending ")