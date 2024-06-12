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

# ---------- VECTOR SETUP ---------- #
  

# Create a new AtomicVector and add to dictionary (note not for Person vectors)
def newAtomicVector(value):
    if value not in Globals.atomic_VectorDictionary.keys():
        newVector = torchhd.random(1,10000)
        Globals.atomic_VectorDictionary[value] = newVector[0]
        Globals.integratedBrain_vectorMemory.add(newVector[0],value)

# Add a new Vector-Value pair. Inputs are labels
def newVectorLabelPair(valueOne: str, valueTwo: str):
    newName = valueOne + "-" + valueTwo
    newNameTwo = valueTwo + "-" + valueOne
    if newName not in Globals.pair_VectorDictionary:
        # If same value, make a permutation of vector one for vector two
        if valueOne == valueTwo:
            vectorOne = Globals.atomic_VectorDictionary[valueOne]
            vectorTwo = torchhd.permute(vectorOne)
        else:
            vectorOne = Globals.atomic_VectorDictionary[valueOne]
            vectorTwo = Globals.atomic_VectorDictionary[valueTwo]
        newVal = torchhd.bind(vectorOne, vectorTwo)
        Globals.pair_VectorDictionary[newName] = newVal
        Globals.integratedBrain_vectorMemory.add(newVal, newName)
        # Add inverse name too
        Globals.pair_VectorDictionary[newNameTwo] = newVal
        Globals.integratedBrain_vectorMemory.add(newVal, newNameTwo)


# Add a new Vector-Value pair. Inputs are vectors
def newVectorValPair(vectorOne, vectorTwo):
    vectorOneName = Globals.integratedBrain_vectorMemory.__getitem__(vectorOne)
    vectorOneName = vectorOneName[1]
    vectorTwoName = Globals.integratedBrain_vectorMemory.__getitem__(vectorTwo)
    vectorTwoName = vectorTwoName[1]
    newName = vectorOneName + "-" + vectorTwoName
    if newName not in Globals.pair_VectorDictionary:
        # If same value, make a permutation of vector one for vector two
        if vectorOneName == vectorTwoName:
            vectorTwo = torchhd.permute(vectorOne)
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

    # Add trio to CaseBundle_persBind
    # If its the first bundle, just permute the triovector and add to memory
    if len(Globals.trio_VectorDictionary) == 1:
        caseBundle_persBind = torchhd.permute(trioVector)
        # Add to special bundle as a VectorTrio (I.e. Person x v1 x v2)
        Globals.integratedBrain_vectorMemory.add(caseBundle_persBind, "SPECIAL_caseBundle_persBind")
        Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"] = caseBundle_persBind
    # If its the second bundle, delete the old one and make a new one with the 2 vectors (fix prev permutation)
    elif len(Globals.trio_VectorDictionary) == 2:
        vecList = []
        for label in Globals.trio_VectorDictionary:
            vecList.append(Globals.trio_VectorDictionary[label])
        newAllBundleVector = torchhd.bundle(vecList[0], vecList[1])
        oldAllBundle_key = Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"]
        oldAllBundleVector = Globals.integratedBrain_vectorMemory.__delitem__(oldAllBundle_key)
        Globals.integratedBrain_vectorMemory.add(newAllBundleVector,"SPECIAL_caseBundle_persBind")
        Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"] = newAllBundleVector
    # If its a longstanding bundle, just add to the existing bundle
    else:
        key = Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"]
        existingBundle = Globals.integratedBrain_vectorMemory.__getitem__(key)
        newBundle = torchhd.bundle(existingBundle[0], trioVector)
        Globals.integratedBrain_vectorMemory.__delitem__(key)
        Globals.integratedBrain_vectorMemory.add(newBundle,"SPECIAL_caseBundle_persBind")
        Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"] = newBundle

    # Add pair to PersobObj and SPECIAL_CaseBundle_PersonBundle
    checkPers = isinstance(personObj.persBundle, int)
    if checkPers:
        # Add to special bundle as just the VectorPair, save copy of budle to Person Obj
        personObj.persBundle = pairVector
        if "SPECIAL_caseBundle_persBundle" in Globals.special_VectorDictionary:
            originalBundle = Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"]
            currentBundle = torchhd.bundle(originalBundle, pairVector)   
            Globals.integratedBrain_vectorMemory.__delitem__(originalBundle)     
            Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"] = currentBundle
            Globals.integratedBrain_vectorMemory.add(currentBundle,"SPECIAL_caseBundle_persBundle")
        else:
            currentBundle = pairVector
            Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"] = currentBundle
            Globals.integratedBrain_vectorMemory.add(currentBundle,"SPECIAL_caseBundle_persBundle")
    else:
        personObj.persBundle = torchhd.bundle(personObj.persBundle, pairVector)
        totalPersBundle = Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"]
        newPersBundle = torchhd.bundle(totalPersBundle, pairVector)
        key = Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"] 
        Globals.integratedBrain_vectorMemory.__delitem__(key)
        Globals.special_VectorDictionary["SPECIAL_caseBundle_persBundle"] = newPersBundle
        Globals.integratedBrain_vectorMemory.add(newPersBundle,"SPECIAL_caseBundle_persBundle")

# Get CaseBundle Vector value
def getCaseBundle_persBind():
    caseBundle = Globals.special_VectorDictionary["SPECIAL_caseBundle_persBind"]
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


# ---------- VECTOR QUERIES ----------

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
    caseBundleVector = getCaseBundle_persBind()
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


# Compare two vectors using cosine similarity
def compareVectors(vector1, vector2):
    return torchhd.cosine_similarity(vector1, vector2)
   

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



# ---------- Misc ----------

def main():
    vectorInput = torchhd.random(10,10000)
    print(compareVectors(vectorInput[0], vectorInput[1]))

if __name__ == "__main__":
    main()

