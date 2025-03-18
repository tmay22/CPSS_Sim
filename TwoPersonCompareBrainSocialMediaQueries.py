import Globals
import VectorFunction_Brain
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import torch
import torchhd
import Checks
import TwoPersonBrainQueries
import TwoPersonSocialMediaQueries

def twoPersSimilarityVal():
    # CHeck general similarity between two people
    print("----------------------------------------")
    print("Compare the similarity between two people in their brain vs on social media")
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
    
    print(f'(*) Brain Results:')
    TwoPersonBrainQueries.twoPersSimilarityVal_inputs(f1_personId, f2_personId)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    TwoPersonSocialMediaQueries.twoPersSimilarityVal_inputs(f1_personId, f2_personId)
    

    return

# *NotE for below function: need to remove outliers somewhere!!! E.g. such as using a 'outliers' file
def twoPersCommonTopic():
    # Get the strongest Atomic similarity between two people
    print("----------------------------------------")
    print("Compare the most common topics between two people in their brain vs on social media")
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
        
    print(f'(*) Brain Results:')
    TwoPersonBrainQueries.twoPersCommonTopic_inputs(f1_personId, f2_personId)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    TwoPersonSocialMediaQueries.twoPersCommonTopic_inputs(f1_personId, f2_personId)
    



def twoPersCommonBelief():
    # Get the strongest Atomic similarity between two people
    print("----------------------------------------")
    print("Get the belief similarity between two people in their brain vs on social media")
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
       
    print(f'(*) Brain Results:')
    TwoPersonBrainQueries.twoPersCommonBelief_inputs(f1_personId, f2_personId)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    TwoPersonSocialMediaQueries.twoPersCommonBelief_inputs(f1_personId, f2_personId)
    

def getBeliefDifference_Val():
    # Get the difference in belief score given a topic
    print("----------------------------------------")
    print("Get the difference in belief score given a topic within a brain vs on social media")
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
    
        
    print(f'(*) Brain Results:')
    TwoPersonBrainQueries.getBeliefDifference_Val_inputs(f1_personId, f2_personId, topic)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    TwoPersonSocialMediaQueries.getBeliefDifference_Val_inputs(f1_personId, f2_personId, topic)
    



def twoPersPairSimilarity_strong():
    # Get the strongest pair belief similarities between two people
    print("----------------------------------------")
    print("Get the strongest pair belief similarity between two people in their brains and on social media")
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
        
    print(f'(*) Brain Results:')
    TwoPersonBrainQueries.twoPersPairSimilarity_strong_inputs(f1_personId, f2_personId)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    TwoPersonSocialMediaQueries.twoPersPairSimilarity_strong_inputs(f1_personId, f2_personId)
    

def getBeliefSimilarity_Topic():
    # Get the similarities in beliefs given a topic, if any
    print("----------------------------------------")
    print("Get the similarities in beliefs given a topic and compare in their brains vs on social Media, if there are any")
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
    
        
    print(f'(*) Brain Results:')
    TwoPersonBrainQueries.getBeliefSimilarity_Topic_inputs(f1_personId, f2_personId, topic)
    print("----------------------------------------")
    print(f'(*) Social Media Results:')
    TwoPersonSocialMediaQueries.getBeliefSimilarity_Topic_inputs(f1_personId, f2_personId, topic)
    