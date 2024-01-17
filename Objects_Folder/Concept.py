class Concept:
    def _init_(self, key, name, factList):

        # unique ID
        self.key = key 

        # Concept name is a type of concept (e.g. 0001 may be politics)
        self.name = name

        # FactList is the list of Fact classes within this concept
        self.factList = factList

