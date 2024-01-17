import numpy as np

class Settings:
    def _init_(self, ):

        # This class determines what the Normal Distribution is for various variables and attributes within the sim.
        # It also includes other variable settings that determine the structure

        # NETWORK DESIGN

        # Number of People in the network
        self.NumPeople

        # Mean number of Edges between People
        self.numPeopleEdges_mean
        # Scale of number of Edges per Person
        self.numPeopleEdges_scale
        
        # PERSON DESIGN

        # Mean centre distribution of Person variable influenceOpeness
        self.influenceOpenness_mean
        #Scale / Standard Deviation of Person variable influenceOpeness
        self.influenceOpenness_scale

        # Mean of no. Concepts per Person
        self.numPeopleConcepts_mean
        # Scale of no. Concepts per Person
        self.numPeopleConcepts_scale

        # Mean Person Influence Openess value (0-100)
        self.personInfluenceOpeness_mean
        # Scale of Person Influence Openess value (SD)
        self.personInfluenceOpeness_scale

        # Mean Person Nuance value (0-100)
        self.personNuance_mean
        # Scale of Person Nuance value (SD)
        self.personNuance_scale

        # Mean of Persons' Interactiveness value (0-100, val is num of interactions per 100 timestamps)
        self.personInteractiveness_mean
        # Scale of Persons' Interactiveness value
        self.personInteractiveness_scale

        # Mean of Persons' Klout value (0-100)
        self.personKlout_mean
        # Scale of Persons' Klout value
        self.personKlout_scale

        # Mean of Persons' Trusting Others value (0-100)
        self.personTrustingOthers_mean
        # Scale of Person's Trusting Others value
        self.personTrustingOthers_scale
        


        # Notes on SD: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html