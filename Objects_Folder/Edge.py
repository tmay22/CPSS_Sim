class Edge:
    def _init_(self, key, personOne, personTwo):
        #EdgeName comes from 
        self.key = key


        # Persons that the edge connects to
        self.connections = [personOne, personTwo]

        # Similarity is calculated by comparing two person node variables
        self.similarity 
        
        # Trust is calculated by comparing the two person nodes variables
        self.trust

        # Note that an edge is always multidimensional. HOWEVER, some Person nodes will be so 'stubborn' that they are essentially unidimensions (think preson vs TV)