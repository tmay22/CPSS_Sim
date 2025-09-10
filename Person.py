import Globals
import Lib
import copy
import torch
import torchhd
import VectorFunction_Brain

class Person:

    # Vars:
    #   id: id for Person obj
    #   persVector: vector value that represents this person (atomic)
    #   persBundle: bundle of vector value-pairs assigned to person for brain values
    #   smBundle: social media vector value-pairs assigned to person in one large bundle
    #   descriptors: describing details about person in dict format. e.g. hair colour:brown
    #   filters: see class
    #   behaviours: see class
    #   edgeList: list of edge objects
    #   linkList: Any connection to CyPhy objects
    #   activityList: list of mediaObjects related to that person
    
    # Initialise object with only personID
    def __init__(self, personId):
        self.id = personId
        self.edgeList = []
        self.linkList = []
        zeroOne = torch.zeros(10000)
        zeroTwo = torch.zeros(10000)
        zeroThree = torch.zeros(10000)
        self.persBundle = zeroThree
        self.smBundle = zeroOne
        self.persVector = zeroTwo
        self.activityList = []
        
        # Create Filters as default
        requiredSimilarity = 0.02
        upperInteractThreshhold = 0.03
        lowerInteractThreshhold = -0.01
        newFilter = Filters(requiredSimilarity, upperInteractThreshhold, lowerInteractThreshhold)
        self.filters = newFilter

        # Create Behaviours as default
        edgeCommunication = 50
        newBehaviour = Behaviours(edgeCommunication)
        self.Behaviours = newBehaviour

    # Add a data dictionary of descriptors for person. (e.g. hair colour)
    def addDescriptors(self, personDataDict):
        self.descriptors = personDataDict
    
    # Set the person's atomic vector value
    def setPersVector(self, vector):
        self.persVector = vector 

    def new_empty(self):
        return type(self)
    
    def updateSmBundle(self, newBundle):
        oldBundle = self.smBundle
        newCombined = torchhd.bundle(oldBundle,newBundle)
        self.smBundle = newCombined
        VectorFunction_Brain.updateSpecialSmBundle(self, oldBundle, newCombined)

    def updatePersBundle(self, newBundle):
        oldBundle = self.persBundle
        newCombined = torchhd.bundle(oldBundle,newBundle)
        self.persBundle = newCombined
        VectorFunction_Brain.updateSpecialPersBundle(self, oldBundle, newCombined)


    
class Filters:

    # Filters define how information is processed by a person
    # There are set filter vars
    # Required Similarity is the base similarity threshhold required for influence. Default to 0
    # upper interact threshhold is the cosine similarity value minimum needed for a positive interaction
    # lower interact threshhold is the cosine similarity value maximum needed for a negative interaction 
    def __init__(self, influenceThreshhold, upperInteractThreshhold, lowerInteractThreshhold):
        #UNFINISHED
        self.influenceThreshhold = influenceThreshhold
        self.upperInteractThreshhold = upperInteractThreshhold
        self.lowerInteractThreshhold = lowerInteractThreshhold

class Behaviours:
    
    # Behaviours define how a Person interacts with their environment
    # There are set behaviour amounts required
    # Edge communication is how often the agent is avaliable to interact witht their network
    # Interactiveness is how likely the agent is to interact with something that  the agent interacts in the simulated environment. (0-100)

    def __init__(self, edgeCommunication):
        #UNFINISHED
        
        #(0-100)
        self.edgeCommunication = edgeCommunication

class Edge:
    def __init__(self, personOne, personTwo, type):
        
        #EdgeName comes from 
        personOneId = personOne.id
        personTwoId = personTwo.id

        newEdgeKey = F"{personOneId}-{personTwoId}"
        self.key = newEdgeKey


        # Persons that the edge connects to (one direction)
        self.connections = [personOne, personTwo]

        self.type = "-"

        type = type.lower()

        # Type can be Cyber OR Physical OR Unknown
        if type != "cyber" and type != "physical":
            self.type == "unknown"
        else:
            self.type = type



