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
    