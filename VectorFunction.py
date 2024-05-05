import torch
import torchhd
import numpy
import random
import Globals

# Torchhd documentation:
# Torch documentation:

# These functions take inputs and produce outputs for HDC algorithms
# Note that these rely on the global memory being established



# Input: Two Vectors to compare
# Process: Cosine similarity equation
# Output: Cosine similarity vector

# Add a new Vector-Value pair. Inputs are labels
def newVectorLabelPair(valueOne: str, valueTwo: str):
    newName = valueOne + "-" + valueTwo
    if newName not in Globals.pair_VectorDictionary:
        vectorOne = Globals.atomic_VectorDictionary[valueOne]
        vectorTwo = Globals.atomic_VectorDictionary[valueTwo]
        newVal = torchhd.bind(vectorOne, vectorTwo)
        Globals.pair_VectorDictionary[newName] = newVal
        Globals.integratedBrain_vectorMemory.add(newVal, newName)


# Add a new Vector-Value pair. Inputs are vectors
def newVectorValPair(vectorOne, vectorTwo):
    vectorOneName = Globals.integratedBrain_vectorMemory.__getitem__(vectorOne)
    vectorOneName = vectorOneName[1]
    vectorTwoName = Globals.integratedBrain_vectorMemory.__getitem__(vectorTwo)
    vectorTwoName = vectorTwoName[1]
    newName = vectorOneName + "-" + vectorTwoName
    if newName not in Globals.pair_VectorDictionary:
        newVal = torchhd.bind(vectorOne, vectorTwo)
        Globals.pair_VectorDictionary[newName] = newVal
        Globals.integratedBrain_vectorMemory.add(newVal, newName)

# Create a new vector trip (i.e. Person x vector Pair)
# THis is when you assign a new vector pair to a person. Then that is added to the case bundle
def newVectorTrio(personObj, pairVector):
    persVector = personObj.persVector
    persId = personObj.id
    trioVector = torchhd.bind(pairVector, persVector)
    nameLookup = Globals.integratedBrain_vectorMemory.__getitem__(pairVector)
    pairLabel = nameLookup[1]
    trioLabel = persId + "-" + pairLabel
    Globals.trio_VectorDictionary[trioLabel] = trioVector
    Globals.integratedBrain_vectorMemory.add(trioVector, trioLabel)

    # Add trio to Case Bundle

    # If its the first bundle, just permute the triovector and add to memory
    if len(Globals.trio_VectorDictionary) == 1:
        caseBundle = torchhd.permute(trioVector)
        Globals.integratedBrain_vectorMemory.add(caseBundle, "SPECIAL_caseBundle")
        Globals.special_VectorDictionary["SPECIAL_caseBundle"] = caseBundle
    # If its the second bundle, delete the old one and make a new one with the 2 vectors (fix prev permutation)
    elif len(Globals.trio_VectorDictionary) == 2:
        vecList = []
        for label in Globals.trio_VectorDictionary:
            vecList.append(Globals.trio_VectorDictionary[label])
        newAllBundleVector = torchhd.bundle(vecList[0], vecList[1])
        oldAllBundle_key = Globals.special_VectorDictionary["SPECIAL_caseBundle"]
        oldAllBundleVector = Globals.integratedBrain_vectorMemory.__delitem__(oldAllBundle_key)
        Globals.integratedBrain_vectorMemory.add(newAllBundleVector,"SPECIAL_caseBundle")
        Globals.special_VectorDictionary["SPECIAL_caseBundle"] = newAllBundleVector
    # If its a longstanding bundle, just add to the existing bundle
    else:
        key = Globals.special_VectorDictionary["SPECIAL_caseBundle"]
        existingBundle = Globals.integratedBrain_vectorMemory.__getitem__(key)
        newBundle = torchhd.bundle(existingBundle[0], trioVector)
        Globals.integratedBrain_vectorMemory.__delitem__(key)
        Globals.integratedBrain_vectorMemory.add(newBundle,"SPECIAL_caseBundle")
        Globals.special_VectorDictionary["SPECIAL_caseBundle"] = newBundle



# Compare two vectors using cosine similarity
def compareVectors(vector1, vector2):
    return torchhd.cosine_similarity(vector1, vector2)

# Get CaseBundle Vector value
def getCaseBundle():
    caseBundle = Globals.special_VectorDictionary["SPECIAL_caseBundle"]
    return caseBundle

# Get Person Object corresponding atomic vector from id
def getPersonVector_fromId(personId):
    personVector = Globals.atomic_VectorDictionary[personId]
    return personVector

# Get Person Object corresponding atomic vector from Person Object
def getPersonVector_fromObj(personObj):
    personVector = Globals.atomic_VectorDictionary[personObj.id]
    return personVector

# Get a pair vector value from a pair label
def getPairVector_fromLabel(pairLabel):
    pairVector = Globals.pair_VectorDictionary[pairLabel]
    return pairVector

# Get an atomic vector value from a label
def getAtomicVector_fromLabel(atomicLabel):
    atomicVector = Globals.atomic_VectorDictionary[atomicLabel]
    return atomicVector

# Get the vector value for positive one
def getPosOneVector():
    posVector = Globals.special_VectorDictionary["SPECIAL_posOneVector"]
    return posVector

# Get the vector value for negative one
def getNegOneVector():
    negVector = Globals.special_VectorDictionary["SPECIAL_negOneVector"]
    return negVector

# FInd out if a person contains a pairing
def doesPersContPair_bool(personObj, pairLabel):
    numInst = doesPersContPair_numInst(personObj, pairLabel)
    if numInst > 0:
        return True
    else:
        return False


# If a person contains a word pairing, how many instances?
def doesPersContPair_numInst(personObj, pairLabel):
    # Get relevant vectors
    caseBundleVector = getCaseBundle()
    personVector = personObj.persVector
    pairVector = getPairVector_fromLabel(pairLabel)
    
    personBundle = torchhd.bind(caseBundleVector, personVector)
   
    # CHeck to see if the XOR of the negative produces -1 vector
    # If it does, find out how many -1s. i.e. -2 ave is 2 instances etc.
    checkForNegative = torchhd.bind(personBundle, torchhd.negative(pairVector))
    searchCheck = Globals.integratedBrain_vectorMemory.__getitem__(checkForNegative) 
    checkForNegative_ave = torch.mean(checkForNegative)   
    if searchCheck[1] == "SPECIAL_negOneVector":
        if checkForNegative_ave <-0.5:
            # Modify to absolute val
            checkForNegative_ave = torchhd.negative(checkForNegative_ave)
        # COnvert to float and round
        numInst_result = checkForNegative_ave.numpy()
        numInst_result = float(numInst_result)
        numInst_result = round(numInst_result)
    else:
        # Else no instances
        numInst_result = 0
    return numInst_result

    

# Get the number of instances of a bind (UNTESTED - only works I think for 2 vector pairs)    
def getNumInstances_bind(bundleVector, bindVector):
    res = torchhd.bind(bundleVector, torchhd.negative(bindVector))
    aveVal = torch.mean(res)
    tempMem = Globals.brain_vectorMemory.__getitem__(res)
    if tempMem[1] == 'negOneVector' or tempMem[1] == 'posOneVector':
        if aveVal <-0.5:
            aveVal = torchhd.negative(aveVal)
        aveVal = aveVal.numpy()
        aveVal = float(aveVal)
        roundAveVal = round(aveVal)
    else:
        roundAveVal = 0
    return roundAveVal

def getTotalNumBinds(bundleVector):
    res = torch.max(bundleVector)
    res = res.numpy()
    res = int(res)
    return res

def main():
    vectorInput = torchhd.random(10,10000)
    print(compareVectors(vectorInput[0], vectorInput[1]))


if __name__ == "__main__":
    main()

