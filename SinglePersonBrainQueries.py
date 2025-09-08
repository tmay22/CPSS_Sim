import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import torch.nn.functional as F
import Checks
import math

def personRankedRangePairsGeneral():
    # See the strongest pairs about a operson
    print("----------------------------------------")
    print("Get the strongest value pairs about a person")
    print("----------------------------------------")
   
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)

    # General error check of inputs
    
    if not Checks.checkPersonExists(personId):
        print(f'{personId} does not exist')
        return

    print("----------------------------------------")

    perObj = Globals.personDict[personId]
    bundle = perObj.persBundle
    memory = Globals.integratedBrain_vectorMemory
    myList = []
    count = 0
    
    vectorList = []
    vectorDict = {}
    for key in Globals.pair_VectorDictionary:
        vectorList.append(Globals.pair_VectorDictionary[key])

    torchStack = torch.stack(vectorList)

   

  

    for pairName in Globals.pair_VectorDictionary:
        pairVector = Globals.pair_VectorDictionary[pairName]
        count = VectorFunction_Brain.doesBundleContainBind_count(bundle, pairVector)
        simValue = torchhd.cosine_similarity(pairVector, bundle)
        if count > 0:
            vectorDict[pairName] = simValue


    

    vectorDict = sorted(vectorDict.items(), key=lambda x: x[1])
    vectorDict.reverse()

    finalList = []
    counter = 0
    for entry in vectorDict:
        if counter < 100:
            finalList.append(entry[0])
        counter = counter + 1

    print(f'RESULT: {finalList}')
    return

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

    # Divide by two and round up. This is because most words are bound twice one to the forward and once to the word after it)
    divTwo = result[2] / 2
    divTwo = math.ceil(divTwo)
    print(f'RESULT: Approx Number of Terms is {divTwo}')
    return


def personRangeAtomic():
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
    atomicV = Globals.atomic_VectorDictionary[wordOne]

    result = Globals.VectorFunction_Brain.getNumInstances_atomic(persObj.persBundle, atomicV)

    print(f'RESULT: Unique Terms: {result[0]}')
    return


def personRankedRangeAtomic():
    # What are the strongest feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("What are the strongest feelings a person has about a concept?")
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

    result = Globals.VectorFunction_Brain.getRankedNumInstances_atomic(persObj.persBundle, atomicV)

    print(f'RESULT: Strongest Terms: {result}')
    return


def doesPersContainPair_inputs(personId, wordOne, wordTwo, wordPair):
    # CHeck to see if a person contains a binded pair of topics. e.g. like and horse

    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    
    result = Globals.VectorFunction_Brain.doesPersContPair_bool(persObj, wordPair)
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'RESULT: {result}')
    return


def howManyDoesPersContainPair_inputs(personId, wordOne, wordTwo, wordPair):
    # CHeck to see if a person contains a binded pair of topics and HOW MANY. e.g. like and horse

    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    wordPair = wordOne + "-" + wordTwo
    result = Globals.VectorFunction_Brain.doesPersContPair_numInst(persObj, wordPair)

    print(f'RESULT: {result}')
    return





def personNumAtomic_inputs(personId, wordOne):
    # What is the number of feelings a person feels against an atomic vector concept
    
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    atomicV = Globals.atomic_VectorDictionary[wordOne]

    result = Globals.VectorFunction_Brain.getNumInstances_atomic(persObj.persBundle, atomicV)

    # Divide by two and round up. This is because most words are bound twice one to the forward and once to the word after it)
    divTwo = result[2] / 2
    divTwo = math.ceil(divTwo)
    print(f'RESULT: Approx Number of Terms is {divTwo}')
    return


def personRangeAtomic_inputs(personId, wordOne):
    # What is the range of feelings a person feels against an atomic vector concept
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    atomicV = Globals.atomic_VectorDictionary[wordOne]

    result = Globals.VectorFunction_Brain.getNumInstances_atomic(persObj.persBundle, atomicV)

    print(f'RESULT: Unique Terms: {result[0]}')
    return


def personRankedRangeAtomic_inputs(personId, wordOne):
    # What are the strongest feelings a person feels against an atomic vector concept
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    atomicV = Globals.atomic_VectorDictionary[wordOne]

    result = Globals.VectorFunction_Brain.getRankedNumInstances_atomic(persObj.persBundle, atomicV)

    print(f'RESULT: Strongest Terms: {result}')
    return




