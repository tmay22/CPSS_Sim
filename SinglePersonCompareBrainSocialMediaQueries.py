import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks
import math
import SinglePersonBrainQueries
import SinglePersonSocialMediaQueries

def doesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics. e.g. like and horse
    print("----------------------------------------")
    print("See the difference between a person's pair associations from brain to social media")
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

    print(f'(*) Brain Results:')
    SinglePersonBrainQueries.doesPersContainPair_inputs(personId, wordOne, wordTwo, wordPair)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    SinglePersonSocialMediaQueries.doesPersContainPair_inputs(personId, wordOne, wordTwo, wordPair)

    return


def howManyDoesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics and HOW MANY. e.g. like and horse
    print("----------------------------------------")
    print("See the difference in whether a person contains a pair in their brain vs their social media?")
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
    
    print(f'(*) Brain Results:')
    SinglePersonBrainQueries.howManyDoesPersContainPair_inputs(personId, wordOne, wordTwo, wordPair)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    SinglePersonSocialMediaQueries.howManyDoesPersContainPair_inputs(personId, wordOne, wordTwo, wordPair)
    


    return





def personNumAtomic():
    # What is the number of feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("See the difference in feelings shown by a person in their brain vs on social media")
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
   
    
    print(f'(*) Brain Results:')
    SinglePersonBrainQueries.personNumAtomic_inputs(personId, wordOne)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    SinglePersonSocialMediaQueries.personNumAtomic_inputs(personId, wordOne)
    

    return


def personRangeAtomic():
    # What is the range of feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("Show the different range of feelings shown by a person in their brain vs on social media")
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

    
    print(f'(*) Brain Results:')
    SinglePersonBrainQueries.personRangeAtomic_inputs(personId, wordOne)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    SinglePersonSocialMediaQueries.personRangeAtomic_inputs(personId, wordOne)
    

    return


def personRankedRangeAtomic():
    # What are the strongest feelings a person feels against an atomic vector concept
    print("----------------------------------------")
    print("Rank the strongest feelings a person has on a topic and show the difference in their brain vs social media")
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
    
    
    print(f'(*) Brain Results:')
    SinglePersonBrainQueries.personRankedRangeAtomic_inputs(personId, wordOne)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    SinglePersonSocialMediaQueries.personRankedRangeAtomic_inputs(personId, wordOne)
    

    return

def comparePersonalSm():
    # Compare the difference between a person's personal profile and their social media profile. 
    print("----------------------------------------")
    print("Compare the difference between a person's personal profile and their social media profile")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")

    # General error check of inputs

    if not Checks.checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    
    person = Globals.personDict[personId]
    diff = VectorFunction_Brain.compareVectors(person.persBundle, person.smBundle)
    print(f'Similarity between profiles is: {diff}')
