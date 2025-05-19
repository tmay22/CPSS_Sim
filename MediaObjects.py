import Globals
import uuid
import VectorFunction_Brain
import Person
import torchhd
import torch


class Media:

    # Vars:
    #   id: id for Media 
    #   inputTime: simCounter when media was inputted into Simulation
    #   contentString: string of content
    #   contentVector: bundle of all pair binds in content
    #   interactionList[] = List of interactions
    #   authpor : link to author

    def __init__(self, id, time, author, contentString):
        self.id = 0
        if id == None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.inputTime = time
        if author in Globals.personDict:
            self.author = Globals.personDict[author]
        else:
            self.author = author
        
        self.contentString = contentString
        newContentVector = VectorFunction_Brain.convertStringToBundleOfBinds(contentString)
        if newContentVector == None:
            print("Oh No! ERROR")
            newContentVector = VectorFunction_Brain.convertStringToBundleOfBinds(contentString)
        self.contentVector = newContentVector
        self.interactionList = []
        parentPerson = Globals.personDict[author]
        parentPerson.activityList.append(self)
        Globals.mediaDict[self.id]=self

        # Add to the Globals smBundle
        if "SPECIAL_caseBundle_smBundle" in Globals.special_VectorDictionary:
            existingV = Globals.special_VectorDictionary["SPECIAL_caseBundle_smBundle"]
            newBundle = torchhd.bundle(existingV,newContentVector)
            Globals.special_VectorDictionary['SPECIAL_caseBundle_smBundle'] = newBundle
        else:
            Globals.special_VectorDictionary['SPECIAL_caseBundle_smBundle'] = newContentVector

class Interaction:

    #   Vars:
    #   id: id for Interaction
    #   occuranceTime: simCounter when interaction took place
    #   sourcePerson: source person related to the interaction
    #   sourceMedia: source media related to the interaction
    #   destPerson: destination person related to the interaction
    #   destMedia: destination media related to the interaction
    #   sourceObject: id of first Object in interaction. Can be a Person or Media obj.
    #   ObjectTwo: id of second Object in interaction (if exists) Can be a Person or Media obj.
    #   type: type of interaction that took place (may have to make options)


    def __init__(self, id, time, inSourcePerson, inSourceMedia, inDestPerson, inDestMedia, type):
        self.id = 0
        if id == None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.occurranceTime = time
        
        # Comments, posts or messages
        interactionOpts = ["Post", "Comment", "Like", "Read", "Message", "unknown"]
        # interactionType can be Post OR Comment OR Like OR Read OR Unknown
        if type != "Post" and type != "Comment" and type != "Like" and type != "Read" and type != "Message":
            self.type == "unknown"
        else:
            self.type = type


        if inSourceMedia in Globals.mediaDict:
            parentMedia = Globals.mediaDict[inSourceMedia]
            parentMedia.interactionList.append(self)
            self.sourceMedia = Globals.mediaDict[inSourceMedia]
        else:
            self.sourceMedia = None
        
        if inDestMedia in Globals.mediaDict:
            parentMedia = Globals.mediaDict[inDestMedia]
            parentMedia.interactionList.append(self)
            self.destMedia = Globals.mediaDict[inDestMedia]
        else:
            self.destMedia = None

        
        if inSourcePerson in Globals.personDict:
            parentPerson = Globals.personDict[inSourcePerson]
            parentPerson.activityList.append(self)
            self.sourcePerson = Globals.personDict[inSourcePerson]
        else:
            self.sourcePerson = None

        if inDestPerson in Globals.personDict:
            parentPerson = Globals.personDict[inDestPerson]
            parentPerson.activityList.append(self)
            self.destPerson = Globals.personDict[inDestPerson]
        else:
            self.destPerson = None

        # when we initiate an interaction, we add that to the persons smBundle
        if inSourceMedia in Globals.mediaDict and inSourcePerson in Globals.personDict:
            parentPerson = Globals.personDict[inSourcePerson]
            parentMedia = Globals.mediaDict[inSourceMedia]

            if isinstance(parentPerson.smBundle, str):
                parentPerson.smBundle = parentMedia.contentVector
            else:
                parentPerson.smBundle = torchhd.bundle(parentPerson.smBundle, parentMedia.contentVector)
        
        Globals.interactionDict[self.id]=self
