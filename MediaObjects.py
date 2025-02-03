import Globals
import uuid
import VectorFunction_Brain
import Person


class Media:

    # Vars:
    #   id: id for Media 
    #   inputTime: simCounter when media was inputted into Simulation
    #   contentString: string of content
    #   contentVector: bundle of all pair binds in content
    #   interactionList[] = List of interactions

    def __init__(self, id, time, authorId, contentString):
        self.id = 0
        if id == None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.inputTime = time
        self.authorId = authorId
        self.contentString = contentString
        self.contentVector = VectorFunction_Brain.convertStringToBundleOfBinds(contentString)
        self.interactionList = []
        parentPerson = Globals.personDict[authorId]
        parentPerson.activityList.append(self)
        Globals.mediaDict[self.id]=self


class Interaction:

    #   Vars:
    #   id: id for Interaction
    #   occuranceTime: simCounter when interaction took place
    #   sourceObject: id of first Object in interaction. Can be a Person or Media obj.
    #   ObjectTwo: id of second Object in interaction (if exists) Can be a Person or Media obj.
    #   type: type of interaction that took place (may have to make options)


    def __init__(self, id, time, sourceObject, destinationObject, type):
        self.id = 0
        if id == None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.occurranceTime = time
        # id of first Object in interaction 
        self.sourceObject = sourceObject
        # id of second Object in interaction (if exists)
        self.destinationObject = destinationObject
        # Comments, posts or messages
        interactionOpts = ["SendMedia", "ReceiveMedia", "ReinforceMedia"]
        # interactionType can be SendMedia OR ReceiveMedia OR ReinforceMedia OR Unknown
        if type != "SendMedia" and type != "ReceiveMedia" and type != "ReinforceMedia":
            self.type == "unknown"
        else:
            self.type = type

        if sourceObject in Globals.mediaDict:
            parentMedia = Globals.mediaDict[sourceObject]
            parentMedia.interactionList.append(self)
        if destinationObject in Globals.mediaDict:
            parentMedia = Globals.mediaDict[destinationObject]
            parentMedia.interactionList.append(self)

        if sourceObject in Globals.personDict:
            parentPerson = Globals.personDict[sourceObject]
            parentPerson.activityList.append(self)
        if destinationObject in Globals.personDict:
            parentPerson = Globals.personDict[destinationObject]
            parentPerson.activityList.append(self)     

