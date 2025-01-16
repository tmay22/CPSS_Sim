import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks

def twoPersSimilarityVal():
    # CHeck general similarity between two people
    print("----------------------------------------")
    print("Check general similarity between two people")
    print("----------------------------------------")
    # COllect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
   
    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    
    print("----------------------------------------")

    # Vector Function to compare two vector bundles representing each person
    f1_bundle = Globals.personDict[f1_personId]
    f1_bundle = f1_bundle.persBundle
    f2_bundle = Globals.personDict[f2_personId]
    f2_bundle = f2_bundle.persBundle
    result = Globals.VectorFunction_Brain.compareVectors(f1_bundle, f2_bundle)
    print(f'Comparing {f1_personId} and {f2_personId}...')
    print(f'RESULT: {result}')
    return

# NotE: need to remove outliers somewhere!!!
def twoPersCommonTopic():
    # Get the strongest Atomic similarity between two people
    print("----------------------------------------")
    print("Get the most common topics between two people (Note this is a slow function)")
    print("----------------------------------------")
    # COllect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
   
    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    
    personOne = Globals.personDict[f1_personId]
    personTwo = Globals.personDict[f2_personId]

    bundleOne = personOne.persBundle
    bundleTwo = personTwo.persBundle
    result = Globals.VectorFunction_Brain.getCommonAtomic(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for item in result:
        if count >= 5:
            break
        name = item[0]
        temp=item[1]
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common topics {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")



def twoPersCommonBelief():
    # Get the strongest Atomic similarity between two people
    print("----------------------------------------")
    print("Get the belief similarity between two people")
    print("----------------------------------------")
    # COllect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
   
    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    
    print("----------------------------------------")

  
    personOne = Globals.personDict[f1_personId]
    personTwo = Globals.personDict[f2_personId]

    bundleOne = personOne.persBundle
    bundleTwo = personTwo.persBundle
    result = Globals.VectorFunction_Brain.getCommonAtomic(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for item in result:
        if count >= 5:
            break
        name = item[0]
        temp=item[1]
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common topics {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")


def getBeliefDifference():
    # Get the difference in belief score given a topic
    print("----------------------------------------")
    print("Get the difference in belief score given a topic")
    print("----------------------------------------")
    
    # Collect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
    topic= input("Give topic: ")
    print("Your input: " + topic)
    # Convert words to lower case
    topic = topic.lower()


    # General error check of inputs
    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    elif not Checks.checkAtomicExists(topic):
        print(f'RESULT: {topic} does not exist')
        return
    
    
    persObjOne = Globals.personDict[f1_personId]
    persObjTwo = Globals.personDict[f2_personId]
    bundleOne=persObjOne.persBundle
    bundleTwo=persObjTwo.persBundle
    topicV=VectorFunction_Brain.getAtomicVector_fromLabel(topic)

    # Specific check if both people contain topic:
    CheckOne = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjOne.persBundle, topicV)
    CheckTwo = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjTwo.persBundle, topicV)

    CheckOne = CheckOne[2]
    CheckTwo = CheckTwo[2]
    if CheckOne == 0:
        print(f'{f1_personId} has no opinion on this topic.')
        print(f'Exiting to Main Menu.')
        print("----------------------------------------")
        return
    elif CheckTwo == 0:
        print(f'{f2_personId} has no opinion on this topic.')
        print(f'Exiting to Main Menu.')
        print("----------------------------------------")
        return
    

    print("----------------------------------------")

   
    # Calc

    


    # Create a bundle for each person of the associated word

    persOnePairArray = VectorFunction_Brain.getNumInstances_atomic(bundleOne,topicV)
    persTwoPairArray = VectorFunction_Brain.getNumInstances_atomic(bundleTwo,topicV)

    persOnePairArray = persOnePairArray[0]
    persTwoPairArray = persTwoPairArray[0]

    # Use a string to force a data type change
    persOneBundle = 'empty'
    persTwoBundle = 'empty'

    #split up array based on pair splits
    for pair in persOnePairArray:
        words = pair.split('-')
        for word in words:
            if topic not in word:
                wordV = VectorFunction_Brain.getAtomicVector_fromLabel(word)
                if persOneBundle == 'empty':
                    persOneBundle = wordV 
                else:
                    persOneBundle = torchhd.bundle(persOneBundle, wordV)
    
    for pair in persTwoPairArray:
        words = pair.split('-')
        for word in words:
            if topic not in word:
                wordV = VectorFunction_Brain.getAtomicVector_fromLabel(word)
                if persTwoBundle == 'empty':
                    persTwoBundle = wordV 
                else:
                    persTwoBundle = torchhd.bundle(persTwoBundle, wordV)


    # Compare the cosine of bundleOne and bundleTwo to see how different they are
    result=VectorFunction_Brain.compareVectors(persOneBundle, persTwoBundle)
    print(f'RESULT: Similarity score between {f1_personId} and {f2_personId} by cosine is: {result}')
    print("----------------------------------------")


   
    


def twoPersPairSimilarity_strong():
    # Get the strongest pair belief similarities between two people
    print("----------------------------------------")
    print("Get the strongest pair belief similarity between two people (Warning: slow)")
    print("----------------------------------------")
    # COllect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
   
    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    
    print("----------------------------------------")
    
    persObjOne = Globals.personDict[f1_personId]
    persObjTwo = Globals.personDict[f2_personId]

    bundleOne = persObjOne.persBundle
    bundleTwo = persObjTwo.persBundle

    result = VectorFunction_Brain.getCommonPairs(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for item in result:
        if count >= 5:
            break
        name = item[0]
        temp=item[1]
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common pairs {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")



def twoPersBeliefSimilarity_weak():
    # Get the weakest belief similarity between two people
    print("----------------------------------------")
    print("Get the strongest Atomic similarity between two people")
    print("----------------------------------------")
    # COllect inputs
    f1_personId= input("Give first PersonId: ")
    print("Your input: " + f1_personId)
    f2_personId= input("Give second PersonId: ")
    print("Your input: " + f2_personId)
   
    if not Checks.checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not Checks.checkPersonExists(f2_personId):
        print(f'{f2_personId} does not exist')
        return
    
    print("----------------------------------------")
# ----------------------------------------------
# Utils / Checks
# ----------------------------------------------

# def checkPersonExists(personId):
#     if personId not in Globals.personDict.keys():
#         print(f'ERROR: PersonID {personId} does not exist in dictionary')
#         return False
#     else:
#         return True

# def checkAtomicExists(word):
#     if word not in Globals.atomic_VectorDictionary.keys():
#         print(f'ERROR, second word {word} does not exist in dictionary')
#         return False
#     else:
#         return True

# def checkPairExists(wordPair):
#     if wordPair not in Globals.pair_VectorDictionary.keys():
#         print(f'ERROR, second word {wordPair} does not exist in dictionary')
#         return False
#     else:
#         return True
    
# def checkTrioExists(wordTrio):
#     if wordTrio not in Globals.trio_VectorDictionary.keys():
#         print(f'ERROR, second word {wordTrio} does not exist in dictionary')
#         return False
#     else:
#         return True