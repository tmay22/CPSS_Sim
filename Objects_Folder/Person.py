class Person:
    def _init_(self, key, influenceOpenness, nuance, interactiveness, klout, trustingOthers):
        
        self.key = key

        # Map of Concept objects 'in the brain'
        self.conceptMap = {}
        
        # Map of PersonIDs and their corresponding Edges
        self.personConnMap = {}

        # How open someone is to influence (0-100). 0 is no openness, 100 is very open
        self.influenceOpenness=influenceOpenness

        # How nuanced is this person (0-100). 0 is no nuance (limited Concept Facts), 100 is very nuanced (many Concept Facts)
        self.nuance=nuance

        # How interactive is this person with others (0-100). Value is number of interactions per 100 timestamps.
        self.interactiveness=interactiveness
        
        # What is the klout of this person to influence others? (0-100)
        self.klout=klout

        # What is the degree to which this person trusts the klout of others to influence them? (0-100)
        self.trustingOthers=trustingOthers

