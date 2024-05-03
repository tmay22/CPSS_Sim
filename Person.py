import Globals
import Lib
import copy
import torch
import torchhd

class Person:

    # Vars:
    #   id: id for Person obj
    #   brainVM: vector memory to represent Person's brain
    #   descriptors: describing details about person in dict format. e.g. hair colour:brown
    #   filters: see class
    #   behaviours: see class
    #   edgeList: list of edge objects
    
    def __init__(self, personId):
        
        self.id = personId
        self.brainVM = torchhd.structures.Memory(0.0)
        self.edgeList = []

    def addDescriptors(self, personDataDict):
        self.descriptors = personDataDict
    
    # USed if for whatever reason there is no memory added to person.
    def newVM(self):
        # Creates a copy of hte base brain VM in Globals
        baseVM = Globals.brain_vectorMemory
        newVM = torchhd.structures.Memory(0.0)
        
        for key in baseVM.keys:
            value = baseVM.__getitem__(key)
            newKey = torch.clone(key)
            newValue = copy.deepcopy(value[1])
            newVM.add(newKey, newValue)

        self.brainVM = newVM


    

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

        # Type can be Cyber OR Physical OR Unknown
        if type != "Cyber" and type != "Physical":
            self.type == "Unknown"
        else:
            self.type = type



