import Globals
import uuid
import VectorFunction_Brain

class Media:

    # Vars:
    #   id: id for Media 
    #   inputTime: simCounter when media was inputted into Simulation
    #   contentString: string of content
    #   contentVector: bundle of all pair binds in content
    #   interactionList[] = List of interactions

    def __init__(self, contentString):
        self.id = uuid.uuid4()
        self.inputTime = Globals.currentTime
        self.contentString = contentString
        self.contentVector = VectorFunction_Brain.convertStringToBundleOfBinds(contentString)
        self.interactionList = []

class Interaction:

    #   Vars:
    #   id: id for Interaction
    #   occuranceTime: simCounter when interaction took place
    #   inputObject: name of Object that was interacted with
    #   type: type of interaction that took place (may have to make options)


    def __init__(self,inputObject,interactionType):
        self.id = uuid.uuid4()
        self.occurranceTime = Globals.SimCounter
        self.inputObject = inputObject
        # Comments, posts or messages
        interactionOpts = ["SendMedia", "ReceiveMedia", "ReinforceMedia"]

        
        # interactionType can be SendMedia OR ReceiveMedia OR ReinforceMedia OR Unknown
        if type != "SendMedia" and type != "ReceiveMedia" and type != "ReinforceMedia":
            self.type == "unknown"
        else:
            self.type = type


