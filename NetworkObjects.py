class Concept:
    def __init__(self, key, name, factList):

        # unique ID
        self.key = key 

        # Concept name is a type.category of concept (e.g. 0001 may be politics)
        self.name = name

        # FactList is the list of Fact classes within this concept
        self.factList = factList

        # The normalised value of all the facts (average fact value)
        self.normalisedVal= [0,0,0]


    def update(self):

        # Updates the normalised value of all the facts by getting the ave for each dimension
        rList=[]
        gList=[]
        bList=[]

        for eachFact in self.factList:
            counter = 1
            while counter <= eachFact.weight:
                rList.append(eachFact.value[0])
                gList.append(eachFact.value[1])
                bList.append(eachFact.value[2])
                counter = counter +1
        if len(rList) >0:
            averageR = sum(rList) / len(rList)
        else:
            averageR = 0
        if len(gList) >0:
            averageG = sum(gList) / len(gList)
        else:
            averageG = 0
        if len(bList) >0:
            averageB = sum(bList) / len(bList)
        else:
            averageB = 0

        self.normalisedVal = [round(averageR), round(averageG), round(averageB)]


class Edge:
    def __init__(self, key, personOne, personTwo, ):
        #EdgeName comes from 
        self.key = key


        # Persons that the edge connects to (one direction)
        self.connections = [personOne, personTwo]

        # Similarity is calculated by comparing two person node variables
        # Note that similarity is used for graph grouping, not nessescarily node/idea spreading
        self.similarity = 0
        
        # Trust is calculated by comparing the two person nodes variables
        self.trust = 0

        # When the edge was last enforced/used
        self.lastInteract = 0

        # Calulate Strength via Trust * (100 - Last Interact)
        self.strength = 0

        # Note that an edge is always single dimensional. For multi dimensional use two edges.
    
    def update(self):
        # Update the trust, similarity, strength variables in an edge
        
        # Person A's trust is a multiplier of Person A's trusting others score, times Person B's Klout (reputation)
        self.trust = round(self.connections[1].klout * self.connections[0].trustingOthers / 100)

        #determine how many dimensions of nuance are shared between the two Persons 
        if self.connections[0].nuance >= self.connections[1].nuance:
            maxNuance = self.connections[1].nuance
        else:
            maxNuance = self.connections[0].nuance
        
        aveValList = []
        numconcepts_A = len(self.connections[0].conceptMap)
        numConceptMatch = 0

        for eachOwnConcept_A in self.connections[0].conceptMap:
            # for each concept in person A, check if match in person B
            checkConcept_B = next((concept_B for concept_B in self.connections[1].conceptMap if concept_B.name == eachOwnConcept_A.name), None)
            if checkConcept_B:
                numConceptMatch = numConceptMatch + 1
                rVal = 0
                gVal = 0
                bVal = 0
                # for each set of coordinates (r1, r2, g1, g2 etc) find length between them
                if maxNuance >= 1:
                    rVal = (abs(eachOwnConcept_A.normalisedVal[0]-checkConcept_B.normalisedVal[0]))
                    rVal = rVal**2
                    dMax = 256
                if maxNuance >= 2:
                    gVal = (abs(eachOwnConcept_A.normalisedVal[1]-checkConcept_B.normalisedVal[1]))
                    gVal = gVal**2
                    dMax = 363
                if maxNuance >= 3:  
                    bVal = (abs(eachOwnConcept_A.normalisedVal[2]-checkConcept_B.normalisedVal[2]))
                    bVal = bVal**2
                    dMax = 444
                # dMax is the maximum distance between points possible, depending on the number of dimensions
                
                # square root lengths (pythagoras) to get the coordinate distance apart
                distance = (rVal + gVal + bVal)**0.5
                aveValList.append(distance)
        # Get the average difference in Value over all concepts overlapped with A and B
        if len(aveValList) > 0:
            conceptValueSimAve = sum(aveValList) / len(aveValList)
            # uses dMax as per nuance dimensions.
            
            conceptValueSimAve = conceptValueSimAve/dMax
            # COnvert low ave to high similarity
            conceptValueSimAve = 1-conceptValueSimAve
            conceptValueSimAve = conceptValueSimAve * 100
        else:
            conceptValueSimAve = 0
        # Find the number of concept name matches that overlap between A and B
        if numconcepts_A == 0:
            numconcepts_A = 1
        conceptOverlap = numConceptMatch/numconcepts_A*100
        # UNSURE if this is the best multiplier or another formula should be used
        tempSimilarity = conceptOverlap*conceptValueSimAve/100
        self.similarity = round(tempSimilarity)
                                

        # Strength re-valuated
        if (100-self.lastInteract) < 1:
            newLastInteract = 1
        else:
            newLastInteract = 100-self.lastInteract

        self.strength = self.trust*newLastInteract/ 100
         

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
        
        #OBSOLETE Map of PersonIDs and their corresponding Edges
        # self.connectionMap = []

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

