import numpy
import random
import torch
import torchhd
import Globals
import csv
import sys
import Person
import VectorFunction

def createBrainVectorBase():
    # Creates a default Vector Memory, atomic dictionary and pos/neg vectors
    # Does not create pairs by default. THis occurs later
    # Created outputs stored in Globals.py

    atomicList = []

    # Parse the dictionary csv and add the words. Remove duplicates.
    with open('4000_Common_Words.csv') as englishDict:
        csv_reader = csv.reader(englishDict, delimiter=',')
        lineCount = 0
        lastItem = ''
        print("NOTE that this atomic read is limited to 200 terms for memory purposes")
        for row in csv_reader:
            # IF LINECOUNT < 100 PURELY FOR TESTING ONLY. Otherwise remove this second bit
            if lineCount != 0 and lineCount < 201:
                if row[0] != lastItem:
                    atomicList.append(row[0])
            lineCount = lineCount + 1
            lastItem = row[0]
    
    # Determine how many atomic vectors we need to generate
    numWords = len(atomicList)
    numPersons = len(Globals.personDict)
    totalAtomicNum = numWords + numPersons

 
    # Cleanup
    del csv_reader
    del englishDict
    del lastItem
    del lineCount

    # Num dimensions per vector
    d = 10000

    # Generate hypervectors for the atomic units unassigned to labels
    vectorGen = torchhd.random(totalAtomicNum,d)

    # Assign hypervectors to python variables for atomic units. Save in vectorDict
    count = 0

    # for each item in the atomic list, create its corresponding vector in the dicts and memory
    for atom in atomicList:
        vectorName = atomicList[count]
        vectorVal = vectorGen[count]
        Globals.atomic_VectorDictionary[vectorName] = vectorVal
        count = count + 1
        Globals.integratedBrain_vectorMemory.add(vectorVal, vectorName)


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
    del row
    del vectorName
    del vectorGen
    del count
    del atom
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
    

    print("SUCCESS: Vector Brain Base Configuration Complete!\n")


def createTestSim():

    # Create Test Brains
    
    fileName_personDataCSV = "PersonPairs_Mini5_PersonData.csv"
    fileName_connectionsCSV = "PersonPairs_Mini5_Network.csv"
    fileName_persAtomicPairsCSV = "PersonPairs_Mini5_PairsSnap1.csv"
    
    generateNetwork(fileName_personDataCSV,fileName_connectionsCSV, fileName_persAtomicPairsCSV)
    
    # Create Test Network


def generateNetwork(fileName_personDataCSV, fileName_connectionsCSV,fileName_persAtomicPairsCSV):
    # Generates a network based on three input CSVs. One stores Person metadata, One stores network connections, one stores the atomic pairs of each person in network.
    # Expected Format: personDataCSV. Row 0 = Titles. Row 0 = [PersonID, *optionalExtras*]
    # Expected Format: connectionsCSV. Row 0 = Titles. Row 0 = [PersonID_A, PersonID_B, Type(Cyber OR Physical)]
    # Expected Format: persAtomicPairsCSV: Row 0 = Titles. Row 0 = [PersonID, AtomicWord1, AtomicWord2]

    # Create Person Objects

    # Default num fields = 1
    numFields = 1

    # find out how many fields in csv
    with open(fileName_personDataCSV) as tempPersonFile:
        csv_read = csv.reader(tempPersonFile, delimiter=',')
        numFields = len(next(csv_read))
    
    # Cleanup
    del csv_read
    del tempPersonFile
  
    # iterate through csv to create person objects. Add each person to global person Dict with their ID as the key.
    with open(fileName_personDataCSV) as personFile:
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




    print(f'Number of Persons: {len(Globals.personDict)}')
    print("SUCCESS: Base people objects created with descriptions!")


    # Create edges and assign them to each Person object
    # Note that edges are directional and that person order matters
    # Note that there CANNOT be new Persons that have not been created being processed.
    with open(fileName_connectionsCSV) as edgesCSV:
        csv_reader = csv.reader(edgesCSV, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount != 0:
                # if row[0] not in Globals.personDict:
                #     newPerson = Person.Person(row[0])
                #     Globals.personDict[newPerson.id] = newPerson
                # if row[1] not in Globals.personDict:
                #     newPerson = Person.Person(row[1])
                #     Globals.personDict[newPerson.id] = newPerson
                personOne = Globals.personDict[row[0]]
                newEdge = Person.Edge(row[0],row[1],row[2])
                personOne.edgeList.append(newEdge)
            lineCount = lineCount + 1
    print(f'SUCCESS: Edges of network created.')
    
    # NEED TO BUILD AN EDGE CHECK

    createBrainVectorBase()

    # Read in Vector-Pairs from CSV and assign to appropriate Persons


    with open(fileName_persAtomicPairsCSV) as atomicPairsCSV:
        csv_reader = csv.reader(atomicPairsCSV, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount != 0:
                personId = row[0]
                newPair = row[1] + "-" + row[2]
                trioLabel = row[0] + newPair
                currentPers = Globals.personDict[personId]
                VectorFunction.newVectorLabelPair(row[1], row[2])
                vectorVal = Globals.pair_VectorDictionary[newPair]
                VectorFunction.newVectorTrio(currentPers,vectorVal)
            lineCount = lineCount + 1

    # TEST Does Person 1 contain "who-feel" - SUCCESS
    # currentPers = Globals.personDict["1"]
    # anotherPers = Globals.personDict["2"]
    # person1 = VectorFunction.doesPersContPair_bool(currentPers, "who-feel")
    # person2 = VectorFunction.doesPersContPair_bool(anotherPers, "who-feel")
    # print("Finished test")
        

    print("SUCCESS: Person pairs and trios added to vector memory")

    # Need to make a cvector function that can check to see if a person's VM contains a pair


    print("Network Generation Completed")



def main():
    createBrainVectorBase()
    print("hello")


if __name__ == "__main__":
    main()