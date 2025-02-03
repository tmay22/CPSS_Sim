import Globals
import Lib
import copy
import torch
import torchhd

class Person:

    # Vars:
    #   id: id for Person obj
    #   persVector: vector value that represents this person (atomic)
    #   persBundle: bundle of vector value-pairs assigned to person
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
        self.persVector = "unassigned"
        self.activityList = []

    # Add a data dictionary of descriptors for person. (e.g. hair colour)
    def addDescriptors(self, personDataDict):
        self.descriptors = personDataDict
    
    # Set the person's atomic vector value
    def setPersVector(self, vector):
        self.persVector = vector 



    

class Filters:

    # Filters define how information is processed by a person
    # There are set filter vars
    # If no filter's provided, a default "no filter" set is used

    def __init__(self, filterX):
        #UNFINISHED
        self.filterX = filterX

class Behaviours:
    
    # Behaviours define how a Person interacts with their environment
    # There are set behaviour amounts required
    # If no behaviours are provided, a default "basic behaviour" set is used

    def __init__(self, behaviourX):
        #UNFINISHED
        self.behaviourX = behaviourX

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



