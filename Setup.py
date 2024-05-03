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
    # This Overload is when there is no Globals.PersonDict to input
    # Creates a default Vector Memory, and atomic and pair dictionaries. 
    # Created outputs stored in Globals.py

    # Size limit set to larger than num of rows in input csv
    # csv.field_size_limit(1885340)

    global atomicList
    atomicList = []

    # Parse the dictionary csv and add the words. Remove duplicates.
    with open('4000_Common_Words.csv') as englishDict:
        csv_reader = csv.reader(englishDict, delimiter=',')
        lineCount = 0
        lastItem = ''
        print("NOTE that this atomic read is limited to 200 terms for memory purposes")
        for row in csv_reader:
            # IF LINECOUNT < 100 PURELY FOR TESTING ONLY. Otherwise remove this second bit
            if lineCount != 0 and lineCount < 202:
                if row[0] != lastItem:
                    atomicList.append(row[0])
            lineCount = lineCount + 1
            lastItem = row[0]
    numWords = len(atomicList)

    # Cleanup
    del csv_reader
    del englishDict
    del lastItem
    del lineCount

    # Num dimensions per vector
    d = 10000

    # Generate hypervectors for the atomic units unassigned to labels
    vectorGen = torchhd.random(numWords,d)

    # Assign hypervectors to python variables for atomic units. Save in vectorDict
    count = 0

    # Globals.atomic_VectorDictionary = {}
    for atom in atomicList:
        vectorName = atomicList[count]
        vectorVal = vectorGen[count]
        Globals.atomic_VectorDictionary[vectorName] = vectorVal
        count = count + 1
             
    # Add Vectors to Memory
    for vector in Globals.atomic_VectorDictionary:
        Globals.brain_vectorMemory.add(Globals.atomic_VectorDictionary[vector], vector )

    # Memory Cleanup
    del vectorVal
    del row
    del vectorName
    del vectorGen
    del count
    del vector
    del atom
    del atomicList

    # Create every Permutation of 2 atomic vectors (doesn't matter order, but duplicates are ok because they will have same value i.e. AB vs BA)
    
    # Globals.pair_VectorDictionary = {}
    for vectorOne in Globals.atomic_VectorDictionary:
        for vectorTwo in Globals.atomic_VectorDictionary:          
                newVal = torchhd.bind(Globals.atomic_VectorDictionary[vectorOne],Globals.atomic_VectorDictionary[vectorTwo])
                newName = vectorOne + "-" + vectorTwo
                Globals.pair_VectorDictionary[newName] = newVal
    
    print(f'No. items in atom_VectorDictionary : ' + str(len(Globals.atomic_VectorDictionary)))
    print(f'No. items in Globals.pair_VectorDictionary: ' + str(len(Globals.pair_VectorDictionary)))

    # cleanup
    del vectorOne
    del vectorTwo
    del newName
    del newVal
    
    # Add vector pairs to memory
    for vector in Globals.pair_VectorDictionary:
         Globals.brain_vectorMemory.add(Globals.pair_VectorDictionary[vector], vector )


    # Create negative and positive vectors
    tempV =  torchhd.random(1,d)
    tempV = tempV[0]
    negOneVector = torchhd.bind(torchhd.negative(tempV), tempV)
    posOneVector = torchhd.negative(negOneVector)

    Globals.brain_vectorMemory.add(negOneVector, 'negOneVector')
    Globals.brain_vectorMemory.add(posOneVector, 'posOneVector')

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



    print(f'Number of Persons: {len(Globals.personDict)}')
    print("SUCCESS: Base people objects created with descriptions!")


    # Create edges and assign them to each Person object
    # Note that edges are directional and that person order matters

    with open(fileName_connectionsCSV) as edgesCSV:
        csv_reader = csv.reader(edgesCSV, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount != 0:
                if row[0] not in Globals.personDict:
                    newPerson = Person.Person(row[0])
                    Globals.personDict[newPerson.id] = newPerson
                if row[1] not in Globals.personDict:
                    newPerson = Person.Person(row[1])
                    Globals.personDict[newPerson.id] = newPerson
                personOne = Globals.personDict[row[0]]
                newEdge = Person.Edge(row[0],row[1],row[2])
                personOne.edgeList.append(newEdge)
            lineCount = lineCount + 1
    print(f'SUCCESS: Edges of network created.')
    
    # NEED TO BUILD AN EDGE CHECK

    # Read in Vector-Pairs from CSV and assign to appropriate Persons

    with open(fileName_persAtomicPairsCSV) as atomicPairsCSV:
        csv_reader = csv.reader(atomicPairsCSV, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            if lineCount != 0:
                personId = row[0]
                newPair = row[1] + "-" + row[2]
                currentPers = Globals.personDict[personId]
                currentVector = Globals.pair_VectorDictionary[newPair]
                currentPers.brainVM.add(currentVector, newPair)
            lineCount = lineCount + 1

    # CHeck, does 1 contain "who-feel"
    currentPers = Globals.personDict["1"]
    anotherPers = Globals.personDict["2"]

    res1 = currentPers.brainVM.__getitem__(Globals.pair_VectorDictionary["who-feel"])
    res2 = anotherPers.brainVM.__getitem__(Globals.pair_VectorDictionary["who-feel"])
    
    print("Test Complete - did it work?")

    # Need to make a cvector function that can check to see if a person's VM contains a pair


    print("Network Generation COmpleted")



def main():
    createBrainVectorBase()
    print("hello")


if __name__ == "__main__":
    main()