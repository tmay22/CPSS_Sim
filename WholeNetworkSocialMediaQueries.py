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
    if not Checks.checkPairExists(vectorPairName):
        print(f'{vectorPairName} does not exist')
        return
    
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

    length = len(personList) * len(personList) - len(personList)
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

    #Compare the semantics of two time periods
def getTwoTimePeriodComparison():

    # Find out how similar people are on SOcial Media  who contain a bind 
    print("----------------------------------------")
    print("How different is a semantic population change over two time periods?")
    print("----------------------------------------")
    # COllect inputs
    dateOneStart= input("Give numerical representation of first time period start ")
    print("You input: " + dateOneStart)

    dateOneEnd= input("Give numerical representation of first time period end ")
    print("You input: " + dateOneEnd)

    dateTwoStart= input("Give numerical representation of second time period start ")
    print("You input: " + dateTwoStart)

    dateTwoEnd= input("Give numerical representation of second time period end ")
    print("You input: " + dateTwoEnd)
   

    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to double
    dateOneStart = float(dateOneStart)
    dateOneEnd = float(dateOneEnd)
    dateTwoStart = float(dateTwoStart)
    dateTwoEnd = float(dateTwoEnd)

    dateOneDict = {}
    dateTwoDict = {}



    
    # Iterate through posts and collect those within date range... might have to convert time to float if not already.
    for postId, postObj in Globals.mediaDict.items():
        postTime = postObj.inputTime
        postTime = float(postTime)
        if postTime >= dateOneStart and postTime <= dateOneEnd:
            dateOneDict[postId] = postObj.contentVector
        elif postTime >= dateTwoStart and postTime <= dateTwoEnd:
            dateTwoDict[postId] = postObj.contentVector
    

    return dateOneDict, dateTwoDict

def idsGetTwoTimePeriodComparison():
    
    # Find out how similar people are on SOcial Media  who contain a bind 
    print("----------------------------------------")
    print("How different are given IDs over two time periods?")
    print("----------------------------------------")
    # COllect inputs
    userIdString= input("Give user IDs. Separate with no spaces, only by ; ")
    print("You input: " + userIdString)

    dateOneStart= input("Give numerical representation of first time period start ")
    print("You input: " + dateOneStart)

    dateOneEnd= input("Give numerical representation of first time period end ")
    print("You input: " + dateOneEnd)

    dateTwoStart= input("Give numerical representation of second time period start ")
    print("You input: " + dateTwoStart)

    dateTwoEnd= input("Give numerical representation of second time period end ")
    print("You input: " + dateTwoEnd)
   

    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to double
    dateOneStart = float(dateOneStart)
    dateOneEnd = float(dateOneEnd)
    dateTwoStart = float(dateTwoStart)
    dateTwoEnd = float(dateTwoEnd)

    userIdArray = userIdString.split(";")

    #error check
    for personId in userIdArray:    
        if not Checks.checkPersonExists(personId):
            print(f'{personId} does not exist')
            return


    dateOneDict = {}
    dateTwoDict = {}



    
    # Iterate through posts and collect those within date range... might have to convert time to float if not already.
    for postId, postObj in Globals.mediaDict.items():
        postTime = postObj.inputTime
        postTime = float(postTime)
        for userId in userIdArray:
            if userId == postObj.author.id:
                if postTime >= dateOneStart and postTime <= dateOneEnd:
                    dateOneDict[userId] = postObj.contentVector
                elif postTime >= dateTwoStart and postTime <= dateTwoEnd:
                    dateTwoDict[userId] = postObj.contentVector

    return dateOneDict, dateTwoDict