import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks
import math

def doesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics. e.g. like and horse
    print("----------------------------------------")
    print("Does Person Contain Paired Association in their Social Media Data?")
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
    bindVal = VectorFunction_Brain.getPairVector_fromLabel(wordPair)
    result = VectorFunction_Brain.doesBundleContainBind_count(persObj.smBundle, bindVal)
    
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'Number of instances: {result}')
    return


def howManyDoesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics and HOW MANY. e.g. like and horse
    print("----------------------------------------")
    print("How Many Results Does a Person Contain of a Paired Association on SOcial Media?")
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
    bindVal = VectorFunction_Brain.getPairVector_fromLabel(wordPair)
    result = VectorFunction_Brain.doesBundleContainBind_count(persObj.smBundle, bindVal)
    
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'Number of instances: {result}')
    return





def personNumAtomic():
    # What is the number of feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("What is the number of feelings a person has about a concept on Social Media?")
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

    result = Globals.VectorFunction_Brain.getNumInstances_atomic(persObj.smBundle, atomicV)

    # Divide by two and round up. This is because most words are bound twice one to the forward and once to the word after it)
    divTwo = result[2] / 2
    divTwo = math.ceil(divTwo)
    print(f'RESULT: Approx Number of Terms is {divTwo}')
    return


def personRangeAtomic():
    # What is the range of feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("What is the range of feelings a person has about a concept on Social Media?")
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

    result = Globals.VectorFunction_Brain.getNumInstances_atomic(persObj.smBundle, atomicV)

    print(f'RESULT: Unique Terms: {result[0]}')
    return


def personRankedRangeAtomic():
    # What are the strongest feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("What are the strongest feelings a person has about a concept on SOcial Media?")
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

    result = Globals.VectorFunction_Brain.getRankedNumInstances_atomic(persObj.smBundle, atomicV)

    print(f'RESULT: Strongest Terms: {result}')
    return



