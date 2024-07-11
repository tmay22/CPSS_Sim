import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks

def doesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics. e.g. like and horse
    print("----------------------------------------")
    print("Does Person Contain Paired Association?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give first word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give second word: ")
    print("You input: " + wordTwo)
   
    # Convert words to lower case
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()

    # General error check of inputs
    wordPair = wordOne + "-" + wordTwo
    if not Checks.checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    elif not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    elif not Checks.checkAtomicExists(wordTwo):
        print(f'{wordTwo} does not exist')
        return
    elif not Checks.checkPairExists(wordPair):
        print(f'RESULT: {personId} does not contain {wordPair}')
        return
    
    print("----------------------------------------")

    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    
    result = Globals.VectorFunction_Brain.doesPersContPair_bool(persObj, wordPair)
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'RESULT: {result}')
    return


def howManyDoesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics and HOW MANY. e.g. like and horse
    print("----------------------------------------")
    print("How Many Results Does a Person Contain of a Paired Association?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give first word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give second word: ")
    print("You input: " + wordTwo)
   
    print("----------------------------------------")
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()

    # General error check of inputs
    wordPair = wordOne + "-" + wordTwo
    if not Checks.checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    elif not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    elif not Checks.checkAtomicExists(wordTwo):
        print(f'{wordTwo} does not exist')
        return
    elif not Checks.checkPairExists(wordPair):
        print(f'RESULT: {personId} does not contain {wordPair}')
        return
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    wordPair = wordOne + "-" + wordTwo
    result = Globals.VectorFunction_Brain.doesPersContPair_numInst(persObj, wordPair)

    print(f'RESULT: {result}')
    return



def personRangeFeelings():
    # What is the range of feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("What is the range of feelings a person has about a concept?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    
   
    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()

    # General error check of inputs
    if not Checks.checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    elif not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    atomicV = Globals.atomic_VectorDictionary(wordOne)

    result = Globals.VectorFunction_Brain.getRangeOfBinds(persObj, atomicV)

    print(f'RESULT: {result}')
    return





def personNumAtomic():
    # What is the number of feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("What is the number of feelings a person has about a concept?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    
   
    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()

    # General error check of inputs
    if not Checks.checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    elif not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    atomicV = Globals.atomic_VectorDictionary[wordOne]

    result = Globals.VectorFunction_Brain.getNumInstances_atomic(persObj.persBundle, atomicV)

    print(f'RESULT: Number of Unique Terms is {result[1]} \nUnique Terms: {result[0]}')
    return




# Old - Stretch
# def graphPerson():
#     # Graph a person
#     print("----------------------------------------")
#     print("Graph a Person")
#     print("----------------------------------------")
#     # COllect inputs
#     personId= input("Give PersonId: ")
#     print("Your input: " + personId)
#     # General error check of inputs
#     if not checkPersonExists(personId):
#         print(f'{personId} does not exist')
#        return
#    # Build graph
#     personObj = Globals.personDict[personId]
#     personBundle = personObj.persBundle
#     personVector = personObj.persVector
#     tempVectors = Globals.integratedBrain_vectorMemory.index(personVector)
#     print("here")
