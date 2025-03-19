import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks
import math

def getNetworkBeliefOnTopic():
    # Get strongest feelings network feels against an atomic topic 
    print("----------------------------------------")
    print("What are the strongest feelings the network has about a topic?")
    print("----------------------------------------")
    # COllect inputs
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    
   
    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()

    # General error check of inputs
    if not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    
    
    # CHeck and call vector function
    atomicV = Globals.atomic_VectorDictionary[wordOne]
    result = VectorFunction_Brain.getRankedNetworkBelief_sm(atomicV)

        # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for item in result:
        if count >= 5:
            break
        else:
            name = item[0]
            num = item[1]
            resData[name]=num 
        count = count + 1 

    print(f'RESULT: Strongest Terms: {resData}')
    print("----------------------------------------")
    return

def getNetworkSDBeliefOnTopic_Val():
    # Get the  variability of the entire network's feeling on a topic

    print("----------------------------------------")
    print("What is the standard deviation range value of feelings on a topic? By number of instances (not vector values)")
    print("----------------------------------------")
    # COllect inputs
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    
   
    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()

    # General error check of inputs
    if not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    
    # CHeck and call vector function
    atomicV = Globals.atomic_VectorDictionary[wordOne]
    result = VectorFunction_Brain.getStandardDeviationBelief_sm(atomicV)
    print(f'RESULT: Variance is: {result}')
    print("----------------------------------------")
    return


def getNetworkBeliefOnTopic_inputs(wordOne):
    # Get strongest feelings network feels against an atomic topic 
    
    
    # CHeck and call vector function
    atomicV = Globals.atomic_VectorDictionary[wordOne]
    result = VectorFunction_Brain.getRankedNetworkBelief_sm(atomicV)

    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for item in result:
        if count >= 5:
            break
        else: 
            name = item[0]
            num = item[1]
            resData[name]=num 
        count = count + 1 

    print(f'RESULT: Strongest Terms: {resData}')
    print("----------------------------------------")
    return

def getNetworkSDBeliefOnTopic_Val_inputs(wordOne):
    # Get the  variability of the entire network's feeling on a topic

    # CHeck and call vector function
    atomicV = Globals.atomic_VectorDictionary[wordOne]
    result = VectorFunction_Brain.getStandardDeviationBelief_sm(atomicV)


    print(f'RESULT: Variance is: {result}')
    print("----------------------------------------")
    return

def getPeopleAssociatedWithBind_sm():
    # Get the people most associated with a bind
    print("----------------------------------------")
    print("What are the strongest feelings the social media network has about two topics?")
    print("----------------------------------------")
    # COllect inputs
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give word: ")
    print("You input: " + wordTwo)
    

    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()

    # General error check of inputs
    if not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    if not Checks.checkAtomicExists(wordTwo):
        print(f'{wordTwo} does not exist')
        return
    
    vectorPairName = f'{wordOne}-{wordTwo}'
    vectorPair = Globals.pair_VectorDictionary[vectorPairName]

    personDict = {}

    for personId, personObj in Globals.personDict.items():
        personBundle= personObj.smBundle
        # Get Cosine Similarity
         # Get Cosine Similarity
        if not isinstance(personBundle, int):
            similarity = torchhd.cosine_similarity(personBundle, vectorPair)
            personDict[personId] = similarity
    
    personDict_sorted = sorted(personDict.items(), key=lambda x:x[1], reverse=True)

    count = 0
    resultData = {}
    for item in personDict_sorted:
        if count<5:
            resultData[item[0]]=item[1]
            count=count+1
        else:
            count = count + 1
            break
    
    print(f'Social media profiles most strongly associated with {wordOne} and {wordTwo} (top 5): {resultData}')
    return

def getPeopleAssociatedWithBind_sm_inputs(wordOne, wordTwo):
    # Get the people most associated with a bind
    
    vectorPairName = f'{wordOne}-{wordTwo}'
    vectorPair = Globals.pair_VectorDictionary[vectorPairName]

    personDict = {}

    for personId, personObj in Globals.personDict.items():
        personBundle= personObj.smBundle
        # Get Cosine Similarity
        # Get Cosine Similarity
        if not isinstance(personBundle, int):
            similarity = torchhd.cosine_similarity(personBundle, vectorPair)
            personDict[personId] = similarity
    
    personDict_sorted = sorted(personDict.items(), key=lambda x:x[1], reverse=True)

    count = 0
    resultData = {}
    for item in personDict_sorted:
        if count<5:
            resultData[item[0]]=item[1]
            count=count+1
        else:
            count = count + 1
            break
    
    print(f'Social media profiles most strongly associated with {wordOne} and {wordTwo} (top 5): {resultData}')
    return

def howSimilarArePeopleWithBind():
    # Find out how similar people are on SOcial Media  who contain a bind 
    print("----------------------------------------")
    print("Find out how similar people are on Social Media based on a common topical opinion?")
    print("----------------------------------------")
    # COllect inputs
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give word: ")
    print("You input: " + wordTwo)
    
   
    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()

    # General error check of inputs
    if not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    if not Checks.checkAtomicExists(wordTwo):
        print(f'{wordTwo} does not exist')
        return
    
    vectorPairName = f'{wordOne}-{wordTwo}'
    vectorPair = Globals.pair_VectorDictionary[vectorPairName]

    personList = []

    for personId, personObj in Globals.personDict.items():
        personBundle= personObj.smBundle
        # 
        if not isinstance(personBundle, int):
            numResults = VectorFunction_Brain.doesBundleContainBind_count(personBundle,vectorPair)
            if numResults > 0:
                # get cosine sim
                personList.append(personObj)

    length = len(personList)
    sum = 0

    for personObjOne in personList:
        for personObjTwo in personList:
            if personObjOne != personObjTwo:
                similarity = torchhd.cosine_similarity(personObjOne.smBundle, personObjTwo.smBundle)
                sum = sum + similarity
    
    if length > 0:
        average = sum / length
    else:
        average = 0
    
    print(f'Average similarity of people containing {wordOne} and {wordTwo} is: {average}')
    return

def howSimilarArePeopleWithBind_inputs(wordOne, wordTwo):
    # Find out how similar people are on SOcial Media who contain a bind 
    
    vectorPairName = f'{wordOne}-{wordTwo}'
    vectorPair = Globals.pair_VectorDictionary[vectorPairName]

    personList = []

    for personId, personObj in Globals.personDict.items():
        personBundle= personObj.smBundle
        # 
        if not isinstance(personBundle, int):
            numResults = VectorFunction_Brain.doesBundleContainBind_count(personBundle,vectorPair)
            if numResults > 0:
                # get cosine sim
                personList.append(personObj)

    length = len(personList)
    sum = 0

    for personObjOne in personList:
        for personObjTwo in personList:
            if personObjOne != personObjTwo:
                similarity = torchhd.cosine_similarity(personObjOne.smBundle, personObjTwo.smBundle)
                sum = sum + similarity
    
    if length > 0:
        average = sum / length
    else:
        average = 0
    
    print(f'Average similarity of people containing {wordOne} and {wordTwo} is: {average}')
    return