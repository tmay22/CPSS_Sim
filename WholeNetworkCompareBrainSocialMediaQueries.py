import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks
import math
import WholeNetworkBrainQueries
import WholeNetworkSocialMediaQueries

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
    
    
    print(f'(*) Brain Results:')
    WholeNetworkBrainQueries.getNetworkBeliefOnTopic_inputs(wordOne)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    WholeNetworkSocialMediaQueries.getNetworkBeliefOnTopic_inputs(wordOne)

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
    
    print(f'(*) Brain Results:')
    WholeNetworkBrainQueries.getNetworkSDBeliefOnTopic_Val_inputs(wordOne)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    WholeNetworkSocialMediaQueries.getNetworkSDBeliefOnTopic_Val_inputs(wordOne)

    return

def getPeopleAssociatedWithBind():
    # Get the people most associated with a bind
    # Get the people most associated with a bind
    print("----------------------------------------")
    print("What are the strongest feelings the network has about two topics?")
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
    
    print(f'(*) Brain Results:')
    WholeNetworkBrainQueries.getPeopleAssociatedWithBind_brain_inputs(wordOne, wordTwo)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    WholeNetworkSocialMediaQueries.getPeopleAssociatedWithBind_sm_inputs(wordOne, wordTwo)

    return
