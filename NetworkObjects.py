class Concept:
    def __init__(self, key, name, factList):

        # unique ID
        self.key = key 

        # Concept name is a type.category of concept (e.g. 0001 may be politics)
        self.name = name

        # FactList is the list of Fact classes within this concept
        self.factList = factList

class Edge:
    def __init__(self, key, personOne, personTwo):
        #EdgeName comes from 
        self.key = key


        # Persons that the edge connects to
        self.connections = [personOne, personTwo]

        # Similarity is calculated by comparing two person node variables
        self.similarity 
        
        # Trust is calculated by comparing the two person nodes variables
        self.trust

        # Note that an edge is always multidimensional. HOWEVER, some Person nodes will be so 'stubborn' that they are essentially unidimensions (think preson vs TV)

class Fact:
    def __init__(self, key, value, lastUpdate, weight):
        
        self.key=key

        # Colour spectrum value (RGB for 3 dimensions)
        self.value=value

        # Last Update is the time the fact was created
        self.lastUpdate = lastUpdate

        # Weight is how heavy/reinforced the node is
        self.weight = weight

class Idea:
    #An idea is like a fact, but is not tied to a Person yet.
    def __init__(self, key, value, lastUpdate, weight):
        
        #unique ID
        self.key=key

        # Colour spectrum value
        self.value=value

        # Last Update is the time the fact was created
        self.lastUpdate = lastUpdate

        # Weight is how heavy/reinforced the node is
        self.weight = weight

class Person:
    def __init__(self, key, influenceOpenness, nuance, interactiveness, klout, trustingOthers, changeThreshold, discriminationThreshold):
        
        self.key = key

        # Map of Concept objects 'in the brain'
        self.conceptMap = []
        
        # Map of PersonIDs and their corresponding Edges
        self.personConnMap = []

        # How open someone is to influence (0-100). 0 is no openness, 100 is very open
        self.influenceOpenness=influenceOpenness

        #  How many Fact dimensions can this person have (range 1-3, represented by the RGB in Facts)
        self.nuance=nuance

        # How interactive is this person with others (0-100). Value is number of interactions per 100 timestamps.
        self.interactiveness=interactiveness
        
        # What is the klout of this person to influence others? (0-100)
        self.klout=klout

        # What is the degree to which this person trusts the klout of others to influence them? (0-100)
        self.trustingOthers=trustingOthers

        # What are the threshold for this person changing their mind on a topic?
        # Value is % similar for new data point to be accepted
        
        self.changeThreshold = changeThreshold

        # What is the percentage similarity that a person can differentiate between values?
        # Second value is % similar in order to merge two data points together. 
        self.discriminationThreshold = discriminationThreshold
