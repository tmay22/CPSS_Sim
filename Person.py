import Globals
import Lib
import copy
import torch
import torchhd

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
    #   activityList: list of mediaObjects related to that person
    
    # Initialise object with only personID
    def __init__(self, personId):
        self.id = personId
        self.edgeList = []
        self.persBundle = 0
        self.smBundle = "unassigned"
        self.persVector = "unassigned"
        self.activityList = []
        
        # Create Filters as default
        requiredSimilarity = 0
        newFilter = Filters(requiredSimilarity)
        self.filter = newFilter

        # Create Behaviours as default
        requiredBehaviour = 20
        newBehaviour = Behaviours(requiredBehaviour)
        self.Behaviour = newBehaviour

    # Add a data dictionary of descriptors for person. (e.g. hair colour)
    def addDescriptors(self, personDataDict):
        self.descriptors = personDataDict
    
    # Set the person's atomic vector value
    def setPersVector(self, vector):
        self.persVector = vector 


    

class Filters:

    # Filters define how information is processed by a person
    # There are set filter vars
    # Required Similarity is the base similarity threshhold required for influence. Default to 0

    def __init__(self, reqSim):
        #UNFINISHED
        self.requiredSimilarity = reqSim

class Behaviours:
    
    # Behaviours define how a Person interacts with their environment
    # There are set behaviour amounts required
    # Interactiveness is how often the agent interacts in the simulated environment. (0-100)

    def __init__(self, newInteract):
        #UNFINISHED
        
        #(0-100)
        self.interactiveness = newInteract

class Edge:
    def __init__(self, personOneId, personTwoId, type):
        
        #EdgeName comes from 

        newEdgeKey = F"{personOneId}-{personTwoId}"
        self.key = newEdgeKey


        # Persons that the edge connects to (one direction)
        self.connections = [personOneId, personTwoId]

        self.type = "-"

        type = type.lower()

        # Type can be Cyber OR Physical OR Unknown
        if type != "cyber" and type != "physical":
            self.type == "unknown"
        else:
            self.type = type



