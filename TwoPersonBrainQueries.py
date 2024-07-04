import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd

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
   
    if not checkPersonExists(f1_personId):
        print(f'{f1_personId} does not exist')
        return
    elif not checkPersonExists(f2_personId):
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



# ----------------------------------------------
# Utils / Checks
# ----------------------------------------------

def checkPersonExists(personId):
    if personId not in Globals.personDict.keys():
        print(f'ERROR: PersonID {personId} does not exist in dictionary')
        return False
    else:
        return True

def checkAtomicExists(word):
    if word not in Globals.atomic_VectorDictionary.keys():
        print(f'ERROR, second word {word} does not exist in dictionary')
        return False
    else:
        return True

def checkPairExists(wordPair):
    if wordPair not in Globals.pair_VectorDictionary.keys():
        print(f'ERROR, second word {wordPair} does not exist in dictionary')
        return False
    else:
        return True
    
def checkTrioExists(wordTrio):
    if wordTrio not in Globals.trio_VectorDictionary.keys():
        print(f'ERROR, second word {wordTrio} does not exist in dictionary')
        return False
    else:
        return True