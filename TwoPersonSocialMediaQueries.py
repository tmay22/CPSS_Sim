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
    print("Check general similarity between two people's Social Media accounts")
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
    f1_bundle = f1_bundle.smBundle
    f2_bundle = Globals.personDict[f2_personId]
    f2_bundle = f2_bundle.smBundle
    result = Globals.VectorFunction_Brain.compareVectors(f1_bundle, f2_bundle)
    print(f'Comparing {f1_personId} and {f2_personId}...')
    print(f'RESULT: {result}')
    return

# *NotE for below function: need to remove outliers somewhere!!! E.g. such as using a 'outliers' file
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

    bundleOne = personOne.smBundle
    bundleTwo = personTwo.smBundle
    result = Globals.VectorFunction_Brain.getCommonAtomic(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for key, value in result.items():
        if count >= 5:
            break
        name = key
        temp=value
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common topics {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")



def twoPersCommonBelief():
    # Get the strongest Atomic similarity between two people
    print("----------------------------------------")
    print("Get the belief similarity between two people's Social Media accounts")
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

    bundleOne = personOne.smBundle
    bundleTwo = personTwo.smBundle
    result = Globals.VectorFunction_Brain.getCommonAtomic(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for key, value in result.items():
        if count >= 5:
            break
        name = key
        temp=value
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common topics {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")


def getBeliefDifference_Val():
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
    bundleOne=persObjOne.smBundle
    bundleTwo=persObjTwo.smBundle
    topicV=VectorFunction_Brain.getAtomicVector_fromLabel(topic)

    # Specific check if both people contain topic:
    CheckOne = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjOne.smBundle, topicV)
    CheckTwo = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjTwo.smBundle, topicV)

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
    print("Get the strongest pair belief similarity between two people on Social Media (Warning: slow)")
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

    bundleOne = persObjOne.smBundle
    bundleTwo = persObjTwo.smBundle

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



def getBeliefSimilarity_Topic():
    # Get the similarities in beliefs given a topic, if any
    print("----------------------------------------")
    print("Get the similarities in beliefs given a topic on SOcial Media, if there are any")
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
    bundleOne=persObjOne.smBundle
    bundleTwo=persObjTwo.smBundle
    topicV=VectorFunction_Brain.getAtomicVector_fromLabel(topic)

    # Specific check if both people contain topic:
    CheckOne = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjOne.smBundle, topicV)
    CheckTwo = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjTwo.smBundle, topicV)

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


    # Create a bundle for each person of the associated word

    persOnePairArray = VectorFunction_Brain.getNumInstances_atomic(bundleOne,topicV)
    persTwoPairArray = VectorFunction_Brain.getNumInstances_atomic(bundleTwo,topicV)

    persOnePairArray = persOnePairArray[0]
    persTwoPairArray = persTwoPairArray[0]

    # Use a string to force a data type change
    persOneBundle = 'empty'
    persTwoBundle = 'empty'

    #convert array to bundles
    for pair in persOnePairArray:
        addVector = VectorFunction_Brain.getPairVector_fromLabel(pair)
        if persOneBundle == 'empty':
            persOneBundle = addVector 
        else:
            persOneBundle = torchhd.bundle(persOneBundle, addVector)
    
    for pair in persTwoPairArray:
        addVector = VectorFunction_Brain.getPairVector_fromLabel(pair)
        if persTwoBundle == 'empty':
            persTwoBundle = addVector 
        else:
            persTwoBundle = torchhd.bundle(persTwoBundle, addVector)


    # Go through BundleOne and compare the vector pairs with bundleTwo
    # See if there are any that match. If so, how many matches (i.e. strength of matches)
    # You don't need to go through bundleTwo to One because you are finding similarities
    # Use a string to force a data type change
    similarityList = {}
    for vectorName in persOnePairArray:
            vectorVal =  VectorFunction_Brain.getPairVector_fromLabel(vectorName)
            calc = VectorFunction_Brain.doesBundleContainBind_count(persTwoBundle,vectorVal)
            if calc > 0:
                similarityList[vectorName] = calc

    # CHeck if there are any similar matches and sort and print
    if len(similarityList) < 1:
        print(f'No similar beliefs on chosen topic {topic}.')
        print("----------------------------------------")
    else:
        # Sort the list to find the highest number of matches
        updatedList = sorted(similarityList.items(), key=lambda x:x[1], reverse=True)
        finalList = {}
        count = 0
        for item in updatedList:
            if count < 5:
                
                name = item[0]
                value = item[1]
                finalList[name]=value
            else:
                return
        print(f'RESULT: Top 5 beliefs ranked most similar on topic "{topic}" are: \n {finalList}')
        print("----------------------------------------")

def twoPersSimilarityVal_inputs(f1_personId, f2_personId):
    # CHeck general similarity between two people
    

    # Vector Function to compare two vector bundles representing each person
    f1_bundle = Globals.personDict[f1_personId]
    f1_bundle = f1_bundle.smBundle
    f2_bundle = Globals.personDict[f2_personId]
    f2_bundle = f2_bundle.smBundle
    result = Globals.VectorFunction_Brain.compareVectors(f1_bundle, f2_bundle)
    print(f'Comparing {f1_personId} and {f2_personId}...')
    print(f'RESULT: {result}')
    return

# *NotE for below function: need to remove outliers somewhere!!! E.g. such as using a 'outliers' file
def twoPersCommonTopic_inputs(f1_personId, f2_personId):
    # Get the strongest Atomic similarity between two people
    
    personOne = Globals.personDict[f1_personId]
    personTwo = Globals.personDict[f2_personId]

    bundleOne = personOne.smBundle
    bundleTwo = personTwo.smBundle
    result = Globals.VectorFunction_Brain.getCommonAtomic(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for key, value in result.items():
        if count >= 5:
            break
        name = key
        temp=value
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common topics {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")



def twoPersCommonBelief_inputs(f1_personId, f2_personId):
    # Get the strongest Atomic similarity between two people
   
  
    personOne = Globals.personDict[f1_personId]
    personTwo = Globals.personDict[f2_personId]

    bundleOne = personOne.smBundle
    bundleTwo = personTwo.smBundle
    result = Globals.VectorFunction_Brain.getCommonAtomic(bundleOne, bundleTwo)
    
    # Show the top 5
    resLength = len(result)
    resData = {}
    count = 0
    for key, value in result.items():
        if count >= 5:
            break
        name = key
        temp=value
        ave = temp[0]
        resData[name] = ave
        count = count + 1

    print(f'RESULT: Total common topics {resLength}. \nTop 5 most common with average strength: {resData}')
    print("----------------------------------------")


def getBeliefDifference_Val_inputs(f1_personId, f2_personId, topic):
    # Get the difference in belief score given a topic
    
    
    persObjOne = Globals.personDict[f1_personId]
    persObjTwo = Globals.personDict[f2_personId]
    bundleOne=persObjOne.smBundle
    bundleTwo=persObjTwo.smBundle
    topicV=VectorFunction_Brain.getAtomicVector_fromLabel(topic)

    # Specific check if both people contain topic:
    CheckOne = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjOne.smBundle, topicV)
    CheckTwo = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjTwo.smBundle, topicV)

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




def twoPersPairSimilarity_strong_inputs(f1_personId, f2_personId):
    # Get the strongest pair belief similarities between two people
    
    
    persObjOne = Globals.personDict[f1_personId]
    persObjTwo = Globals.personDict[f2_personId]

    bundleOne = persObjOne.smBundle
    bundleTwo = persObjTwo.smBundle

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



def getBeliefSimilarity_Topic_inputs(f1_personId, f2_personId, topic):
    # Get the similarities in beliefs given a topic, if any
    
    
    persObjOne = Globals.personDict[f1_personId]
    persObjTwo = Globals.personDict[f2_personId]
    bundleOne=persObjOne.smBundle
    bundleTwo=persObjTwo.smBundle
    topicV=VectorFunction_Brain.getAtomicVector_fromLabel(topic)

    # Specific check if both people contain topic:
    CheckOne = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjOne.smBundle, topicV)
    CheckTwo = Globals.VectorFunction_Brain.getNumInstances_atomic(persObjTwo.smBundle, topicV)

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


    # Create a bundle for each person of the associated word

    persOnePairArray = VectorFunction_Brain.getNumInstances_atomic(bundleOne,topicV)
    persTwoPairArray = VectorFunction_Brain.getNumInstances_atomic(bundleTwo,topicV)

    persOnePairArray = persOnePairArray[0]
    persTwoPairArray = persTwoPairArray[0]

    # Use a string to force a data type change
    persOneBundle = 'empty'
    persTwoBundle = 'empty'

    #convert array to bundles
    for pair in persOnePairArray:
        addVector = VectorFunction_Brain.getPairVector_fromLabel(pair)
        if persOneBundle == 'empty':
            persOneBundle = addVector 
        else:
            persOneBundle = torchhd.bundle(persOneBundle, addVector)
    
    for pair in persTwoPairArray:
        addVector = VectorFunction_Brain.getPairVector_fromLabel(pair)
        if persTwoBundle == 'empty':
            persTwoBundle = addVector 
        else:
            persTwoBundle = torchhd.bundle(persTwoBundle, addVector)


    # Go through BundleOne and compare the vector pairs with bundleTwo
    # See if there are any that match. If so, how many matches (i.e. strength of matches)
    # You don't need to go through bundleTwo to One because you are finding similarities
    # Use a string to force a data type change
    similarityList = {}
    for vectorName in persOnePairArray:
            vectorVal =  VectorFunction_Brain.getPairVector_fromLabel(vectorName)
            calc = VectorFunction_Brain.doesBundleContainBind_count(persTwoBundle,vectorVal)
            if calc > 0:
                similarityList[vectorName] = calc

    # CHeck if there are any similar matches and sort and print
    if len(similarityList) < 1:
        print(f'No similar beliefs on chosen topic {topic}.')
        print("----------------------------------------")
    else:
        # Sort the list to find the highest number of matches
        updatedList = sorted(similarityList.items(), key=lambda x:x[1], reverse=True)
        finalList = {}
        count = 0
        for item in updatedList:
            if count < 5:
                
                name = item[0]
                value = item[1]
                finalList[name]=value
            else:
                return
        print(f'RESULT: Top 5 beliefs ranked most similar on topic "{topic}" are: \n {finalList}')
        print("----------------------------------------")