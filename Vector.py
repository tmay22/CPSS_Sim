import Globals
import Lib
import copy

class BrainVector:

    # Vars:
    #   id: id for Person obj
    #   brainVM: vector memory to represent Person's brain
    #   descriptors: describing details about person in dict format. e.g. hair colour:brown
    #   filters: see class
    #   behaviours: see class
    #   edgeList: list of edge objects
    
    def __init__(self):
        
        self.VM = Globals.brain_vectorMemory