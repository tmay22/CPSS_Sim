class Settings:
    
    def __init__(self, numConcepts, numPeople, numPeopleEdges_mean, numPeopleEdges_scale, numPeopleConcepts_mean, numPeopleConcepts_scale, personInfluenceOpeness_mean, personInfluenceOpeness_scale, personNuance_mean, personNuance_scale, personInteractiveness_mean, personInteractiveness_scale, personKlout_mean, personKlout_scale, personTrustingOthers_mean, personTrustingOthers_scale, changeThreshold_mean, changeThreshold_scale, discriminationThreshold_mean, discriminationThreshold_scale, conceptFactNum_mean, conceptFactNum_scale):

        # This class determines what the Normal Distribution is for various variables and attributes within the sim.
        # It also includes other variable settings that determine the structure

        # NETWORK DESIGN

        # Number of existing concepts (not including new ideas)
        self.numConcepts = numConcepts

        # Number of People in the network
        self.numPeople = numPeople

        # Mean number of Edges between People
        self.numPeopleEdges_mean = numPeopleEdges_mean
        # Scale of number of Edges per Person
        self.numPeopleEdges_scale = numPeopleEdges_scale
        
        # PERSON DESIGN

        # Mean of no. Concepts per Person
        self.numPeopleConcepts_mean = numPeopleConcepts_mean
        # Scale of no. Concepts per Person
        self.numPeopleConcepts_scale = numPeopleConcepts_scale

        # Mean Person Influence Openess value (0-100)
        self.personInfluenceOpeness_mean = personInfluenceOpeness_mean
        # Scale of Person Influence Openess value (SD)
        self.personInfluenceOpeness_scale = personInfluenceOpeness_scale

        # Mean Person Nuance value (1-3)
        # How many dimensions a person can have in a fact  value
        self.personNuance_mean = personNuance_mean
        # Scale of Person Nuance value (SD)
        self.personNuance_scale = personNuance_scale

        # Mean of Persons' Interactiveness value (0-100, val is num of interactions per 100 timestamps)
        self.personInteractiveness_mean = personInteractiveness_mean
        # Scale of Persons' Interactiveness value
        self.personInteractiveness_scale = personInteractiveness_scale

        # Mean of Persons' Klout value (0-100)
        self.personKlout_mean = personKlout_mean
        # Scale of Persons' Klout value
        self.personKlout_scale = personKlout_scale

        # Mean of Persons' Trusting Others value (0-100)
        self.personTrustingOthers_mean = personTrustingOthers_mean
        # Scale of Person's Trusting Others value
        self.personTrustingOthers_scale = personTrustingOthers_scale


        # What are the threshold for this person changing their mind on a topic?
        # Value is % similar for new data point to be accepted
        self.changeThreshold_mean = changeThreshold_mean
        self.changeThreshold_scale = changeThreshold_scale
    
        # What is the percentage similarity that a person can differentiate between values?
        # Second value is % similar in order to merge two data points together
        self.discriminationThreshold_mean = discriminationThreshold_mean
        self.discriminationThreshold_scale = discriminationThreshold_scale

        # FACT DESIGN

        # Mean number of Facts per Concept
        self.conceptFactNum_mean = conceptFactNum_mean
        # Scale of Facts per concept
        self.conceptFactNum_scale = conceptFactNum_scale

        # Notes on SD: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

    def __str__(self):
        stringPrint = f"Number of existing concepts (not including new ideas): {self.numConcepts} \n"
        stringPrint = f"Number of People in network: {self.numPeople} \n"
        stringPrint = f"{stringPrint}Mean edges between people: {self.numPeopleEdges_mean} \n"
        stringPrint = f"{stringPrint}Scale of number of Edges per Person: {self.numPeopleEdges_scale} \n"
        stringPrint = f"{stringPrint}Mean of no. Concepts per Person: {self.numPeopleConcepts_mean} \n"
        stringPrint = f"{stringPrint}Scale of no. Concepts per Person: {self.numPeopleConcepts_scale} \n"
        stringPrint = f"{stringPrint}Mean Person Influence Openess value (0-100): {self.personInfluenceOpeness_mean} \n"
        stringPrint = f"{stringPrint}Scale of Person Influence Openess value (SD): {self.personInfluenceOpeness_scale} \n"
        stringPrint = f"{stringPrint}Mean Person Nuance value (0-100): {self.personNuance_mean} \n"
        stringPrint = f"{stringPrint}Scale of Person Nuance value (SD): {self.personNuance_scale } \n"
        stringPrint = f"{stringPrint}Mean of Persons' Interactiveness value: {self.personInteractiveness_mean } \n"
        stringPrint = f"{stringPrint}Scale of Persons' Interactiveness value: {self.personInteractiveness_scale } \n"
        stringPrint = f"{stringPrint}Mean of Persons' Klout value (0-100): {self.personKlout_mean } \n"
        stringPrint = f"{stringPrint}Scale of Persons' Klout value: {self.personKlout_scale } \n"
        stringPrint = f"{stringPrint}Mean of Persons' Trusting Others value (0-100): {self.personTrustingOthers_mean } \n"
        stringPrint = f"{stringPrint}Scale of Person's Trusting Others value: {self.personTrustingOthers_scale } \n"
        stringPrint = f"{stringPrint}Mean of Person's Change Threshold value: {self.changeThreshold_mean } \n"
        stringPrint = f"{stringPrint}Scale of Person's Change Threshold value: {self.changeThreshold_scale } \n"
        stringPrint = f"{stringPrint}Mean of Person's Discrimination Threshold value: {self.discriminationThreshold_mean } \n"
        stringPrint = f"{stringPrint}Scale of Person's Discrimination Threshold value: {self.discriminationThreshold_scale } \n"

        stringPrint = f"{stringPrint}Mean number of Facts per Concept: {self.conceptFactNum_mean } \n"
        stringPrint = f"{stringPrint}Scale of Facts per concept: {self.conceptFactNum_scale } \n"

        return stringPrint