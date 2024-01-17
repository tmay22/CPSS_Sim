class Fact:
    def __init__(self, key, value, lastUpdate, weight):
        
        self.key=key

        # Colour spectrum value
        self.value=value

        # Last Update is the time the fact was created
        self.lasyUpdate = lastUpdate

        # Weight is how heavy/reinforced the node is
        self.weight = weight
