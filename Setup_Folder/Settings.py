import numpy as np

class Settings:
    def _init_(self, ):

        # This class determines what the Normal Distribution is for various variables and attributes within the sim.
        # It also includes other variable settings that determine the structure

        # NETWORK DESIGN

        # Number of People in the network
        self.NumPeople

        # Mean number of Edges between People
        self.numPeopleEdgesMean
        # Scale of number of Edges per Person
        self.numPeopleEdgesScale
        
        # PERSON DESIGN

        # Mean centre distribution of Person variable influenceOpeness
        self.influenceOpennessMean
        #Scale / Standard Deviation of Person variable influenceOpeness
        self.influenceOpennessScale

        # Mean of no. Concepts per Person
        self.numPeopleConceptsMean
        # Scale of no. Concepts per Person
        self.numPeopleConceptsScale

        # Mean Person Influence Openess value (0-100)
        self.personInfluenceOpenessMean
        # Scale of Person Influence Openess value (SD)
        self.personInfluenceOpenessScale

        


        # Notes on SD: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html