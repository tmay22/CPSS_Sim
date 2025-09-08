import numpy
import random
import torch
import torchhd
import Globals
import csv
import sys
import Person
import VectorFunction_Brain
import MediaObjects


# buildSim relies on the three csv files existing in the designated path following the naming convensions
def buildSim(path, historyOption):

    # Set time as 0 until further notice
    Globals.currentTime = 0
    
    # Generates a network based on four input CSVs. One stores Person metadata, One stores network connections, one stores a person's personal narrative, one stores social media data, and a boolean DictOpt.
    # Expected Format: personDataCSV. Row 0 = Titles. Row 0 = [PersonID, *optionalExtras*]
    # Expected Format: connectionsCSV. Row 0 = Titles. Row 0 = [PersonID_A, PersonID_B, Type(Cyber OR Physical)]
    # Expected Format: fileName_persSocialMediaCSV: Row 0 = Titles. Row 0 = [PersonId, Data]
    # Expected Format: fileName_persNarrative: Row 0 = Titles. Row 0 = [PersonId, Data]
    # Create Person Objects

    # Create file paths
    personData_path = path+"PersonData.csv"
    EdgeData_path= path+"EdgeData.csv"
    PersonNarrative_path = path+"PersonNarrative.csv"

    if historyOption:
        PostData_Path = path+"HistoricPostData.csv"
        PostComments_Path = path+"HistoricPostComments.csv"
        PostLikes_Path = path+"HistoricPostLikes.csv"


    # Sm Data not needed yet
    #SmData_path = path+"SmData.csv"

    # Build Person Objects 
    buildPersons(personData_path)

    # Build Edges / Network
    buildEdges(EdgeData_path)

   
    # Create the default person brain for the Globals 
    createPersonBrain_VectorBase()

    # Assign NarrativeData as vector-pairs to Person objects
    assignNarratives(PersonNarrative_path)


    if historyOption:
        # if the historyOption is selected:
        postInput(PostData_Path)
        print("Completion of Post Processing")
        commentsInput(PostComments_Path)
        print("Completion of Comment Processing")
        likesInput(PostLikes_Path)
        print("Completion of Like Processing")

        

    # Need to input SM Data!

    print("SUCCESS: Person pairs and trios added to vector memory")
    print("SUCCESS: Network Generation Completed")


    # Create Social Media vector memory


    # Input historic social media posts


# Build the Person objects and their descriptors
def buildPersons(personData_path):

    # Default num fields = 1
    numFields = 1

    # find out how many fields in csv
    with open(personData_path) as tempPersonFile:
        csv_read = csv.reader(tempPersonFile, delimiter=',')
        numFields = len(next(csv_read))
    
    # Cleanup
    del csv_read
    del tempPersonFile
  
    # iterate through csv to create person objects. Add each person to global person Dict with their ID as the key.
    with open(personData_path) as personFile:
        lineCount = 0
        csv_reader = csv.reader(personFile, delimiter=',')
        fieldList = []

        for row in csv_reader:
            personDesc = {}
            if lineCount != 0:
                fieldCounter=1
                newPerson = Person.Person(row[0])
                if numFields > 1:
                    for fieldContent in row:
                        if fieldCounter > 1:
                            personDesc[fieldList[fieldCounter-1]] = fieldContent
                        fieldCounter = fieldCounter + 1
                    newPerson.addDescriptors(personDesc)
                Globals.personDict[newPerson.id] = newPerson
            else:
                for fieldTitle in row:
                    fieldList.append(fieldTitle)
            lineCount= lineCount + 1

    # Cleanup
    del personFile
    del csv_reader
    del fieldContent
    del newPerson
    del personDesc
    del lineCount
    del numFields
    del fieldTitle
    del fieldList




    #print(f'Number of Persons: {len(Globals.personDict)}')
    print("SUCCESS: Base people objects created with descriptions!")

# Build the edges / network between Person objects
def buildEdges(EdgeData_path):
    
    # Create edges and assign them to each Person object
    # Note that edges are directional and that person order matters
    # Note that there CANNOT be new Persons that have not been created being processed.
    with open(EdgeData_path) as edgesCSV:
        csv_reader = csv.reader(edgesCSV, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount != 0:
                personOne = Globals.personDict[row[0]]
                newEdge = Person.Edge(row[0],row[1],row[2])
                personOne.edgeList.append(newEdge)
            lineCount = lineCount + 1
    print('SUCCESS: Edges of network created.')
    
    # NEED TO BUILD AN EDGE CHECK

# Creates the Person brain base for the Globals
def createPersonBrain_VectorBase():
    # Creates a default Vector Memory, atomic dictionary and pos/neg vectors for the PersonBrain in Globals.
    # Does not create pairs by default. THis occurs later
    # Created outputs stored in Globals.py

    atomicList = []
    numPersons = len(Globals.personDict)
    totalAtomicNum = numPersons

    # Num dimensions per vector
    d = 10000

    # Generate hypervectors for the atomic units unassigned to labels
    vectorGen = torchhd.random(totalAtomicNum,d)

    # Assign hypervectors to python variables for atomic units. Save in vectorDict
    count = 0


    # for each item in the person list, create its corresponding vector in the dicts and memory
    for person in Globals.personDict:
        currentPers =  Globals.personDict[person]
        vectorName = currentPers.id
        vectorVal = vectorGen[count]
        Globals.atomic_VectorDictionary[vectorName] = vectorVal
        currentPers.persVector = vectorVal
        count = count + 1
        Globals.integratedBrain_vectorMemory.add(vectorVal, vectorName)

    
    # Memory Cleanup
    del vectorVal
    del vectorName
    del vectorGen
    del count
    del atomicList
    del currentPers
    
    print(f'No. items in atom_VectorDictionary : ' + str(len(Globals.atomic_VectorDictionary)))

    # Create negative and positive vectors
    tempV =  torchhd.random(1,d)
    tempV = tempV[0]
    negOneVector = torchhd.bind(torchhd.negative(tempV), tempV)
    posOneVector = torchhd.negative(negOneVector)

    Globals.integratedBrain_vectorMemory.add(negOneVector, 'SPECIAL_negOneVector')
    Globals.integratedBrain_vectorMemory.add(posOneVector, 'SPECIAL_posOneVector')

    Globals.special_VectorDictionary["SPECIAL_negOneVector"] = negOneVector
    Globals.special_VectorDictionary["SPECIAL_posOneVector"] = posOneVector
    

    print("SUCCESS: Vector Brain Base Configuration Complete")

# For each person's narrative, create the words and assign to each person
def assignNarratives(fileName_persNarrativeCSV):
    # Read in narrative data from CSV. Parse as vector pairs and assign to appropriate persons
    # No input word dictionary file required

    with open(fileName_persNarrativeCSV) as narrativeCSV:
        csv_reader = csv.reader(narrativeCSV, delimiter=',')
        lineCount = 0
        remChar = "~!#$%^&*()_+`-=[]\\\{\}|;\':\",.,/<>?â€œ"
        for row in csv_reader:
            if lineCount != 0: #remove <x for future. This is just to speed up testing process.
                personId = row[0]
                personNarr = ""
                segCount = 0
                # If there are additional non csv commas in row, append together
                for segment in row:
                    if segCount != 0:
                        personNarr = personNarr + segment
                    segCount = segCount + 1
                maxCells = len(row)
                 # Convert to lower Case
                personNarr = personNarr.lower()
                narrSplit = personNarr.split(" ")
                newSplit = []
                for word in narrSplit:
                    if word != '':
                        newSplit.append(word)
                narrSplit = newSplit
                wordCount = 0
                maxIndex = len(narrSplit)
                maxIndex = maxIndex - 1
                for wordOne in narrSplit:
                    nextIndex = wordCount + 1
                    if nextIndex <= maxIndex:
                        wordTwo = narrSplit[nextIndex]
                        wordOne = wordOne.translate(str.maketrans('', '', remChar))
                        wordTwo = wordTwo.translate(str.maketrans('', '', remChar))
                        VectorFunction_Brain.newAtomicVector(wordOne)
                        VectorFunction_Brain.newAtomicVector(wordTwo)
                        newPair = wordOne + "-" + wordTwo
                        trioLabel = row[0] + "-" + newPair
                        currentPers = Globals.personDict[personId]
                        VectorFunction_Brain.newVectorLabelPair(wordOne, wordTwo)
                        vectorVal = Globals.pair_VectorDictionary[newPair]
                        VectorFunction_Brain.newVectorTrio(currentPers,vectorVal)
                    wordCount = wordCount + 1
            print(lineCount)
            lineCount = lineCount + 1

    print("Here")


# Create social media posts 
def postInput(PostData_Path): 
    with open(PostData_Path) as postsCSV:
        csv_reader = csv.reader(postsCSV, delimiter=',')
        lineCount = 0
        remChar = "~!#$%^&*()_+`-=[]\\\{\}|;\':â€”\",.™/<>?"
        rowCount = 0 # NEED TO DO SOME SORT OF RECURSION HERE

        for row in csv_reader:
            if lineCount != 0:
                personId = row[0]
                # Get Person Object
                currentPers = Globals.personDict[personId]
                postId = row[1]
                timestamp = row[2]
                postContent = ""
                postVector = None
                segCount = 0
                # If there are additional non csv commas in row, append together
                for segment in row:
                    if segCount >2:
                        postContent = postContent + segment
                    segCount = segCount + 1
                maxCells = len(row)
                # convert to lower
                postContent = postContent.lower()
                # Create the Media Object
                curentMedia = MediaObjects.Media(postId,timestamp, personId, postContent)
                # Create Post Interaction of creator
                currentInteraction = MediaObjects.Interaction(None,timestamp, personId, postId, None, None, "Post")

            print(lineCount)
            lineCount = lineCount + 1

    for personCounter in Globals.personDict:
        person = Globals.personDict[personCounter]
        # CHeck to see if there is a 0 (int) or a vector in the budle.
        checkPers = isinstance(person.persBundle, int)
        if checkPers:
            zeros = torchhd.empty(1, 10000)
            person.persBundle = zeros[0]
 # Create social media posts 

# Create social media comments
def commentsInput(PostComments_Path):
    with open(PostComments_Path) as commentsCSV:
        csv_reader = csv.reader(commentsCSV, delimiter=',')
        lineCount = 0
        remChar = "~!#$%^&*()_+`-=[]\\\{\}|;\':\",./”<>?"
        for row in csv_reader:
            if lineCount != 0:
                personId = row[1]
                # Get Person Object
                currentPers = Globals.personDict[personId]
                commentId = None
                postId = row[1]
                timestamp = row[2]
                postContent = ""
                segCount = 0
                 # If there are additional non csv commas in row, append together
                for segment in row:
                    if segCount >2:
                        postContent = postContent + segment
                    segCount = segCount + 1
                maxCells = len(row)
                # convert to lower
                postContent = postContent.lower()
                # Create the Media Object
                currentMedia = MediaObjects.Media(commentId,timestamp, personId, postContent)
                # Create Post Interaction of creator
                commentId = currentMedia.id
                sendInteraction = MediaObjects.Interaction(None,timestamp, personId, commentId, None, postId, "Comment")
                
            print(lineCount)
            lineCount = lineCount + 1


# Create social media likes
def likesInput(PostLikes_Path): 
    # Note that the setup assumes that only those who like or comment have interacted/received posts
    with open(PostLikes_Path) as likesCSV:
        csv_reader = csv.reader(likesCSV, delimiter=',')
        lineCount = 0
        remChar = "~!#$%^&*()_+`-=[]\\\{\}|;\':\",./<>?"
        for row in csv_reader:
            if lineCount != 0:
                personId = row[1]
                postId = row[0]
                timestamp = row[2]
                # Create Post Interaction of creator
                currentInteraction = MediaObjects.Interaction(None,timestamp, personId, None, None, postId, "Like")
            print(lineCount)
            lineCount = lineCount + 1                 


