import Globals
import torch


class CyberPhysical:

    def __init__(self, cyPhyId, name, isCyber, isPhysical):
        self.id = cyPhyId
        self.name = name
        self.linkList = []
        self.isCyber = isCyber
        self.isPhysical = isPhysical
        zeroOne = torch.zeros(10000)
        self.cyPhyVector = zeroOne
        
    # Set the obj's atomic vector value
    def setCyPhyVector(self, vector):
        self.cyPhyVector = vector 

# A link connects two Objects
class Link:
    def __init__(self, objOne, objTwo, type):
        
        #EdgeName comes from 
        #EdgeName comes from 
        objOneId = objOne.id
        objTwoId = objTwo.id

        newEdgeKey = F"{objOneId}-{objTwoId}"
        self.key = newEdgeKey


        # Persons that the edge connects to (one direction)
        self.connections = [objOne, objTwo]

        self.type = "-"

        type = type.lower()

        # Type 
        if type != "integrated" and type != "networked" and type != "internet"and type != "physical":
            self.type == "unknown"
        else:
            self.type = type
