import torch
import torchhd
import numpy
import random
import Globals
import Checks
import statistics


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

    # CHeck to see if there is a 0 (int) or a vector in the budle.
    checkPers = isinstance(personObj.persBundle, int)
    # If it is an int not a vector:
    if checkPers:
        # Add to special bundle as just the VectorPair, save copy of bundle to Person Obj
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

# Check to see if a bundle contains a bind and return the number of counts
def doesBundleContainBind_count(bundle, bind):
   
    # CHeck to see if the XOR of the negative produces -1 vector
    # If it does, find out how many -1s. i.e. -2 ave is 2 instances etc.
    checkForNegative = torchhd.bind(bundle, torchhd.negative(bind))
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
# def getNumInstances_bind(bundleVector, bindVector):
#     res = torchhd.bind(bundleVector, torchhd.negative(bindVector))
#     aveVal = torch.mean(res)
#     tempMem = Globals.brain_vectorMemory.__getitem__(res)
#     if tempMem[1] == 'negOneVector' or tempMem[1] == 'posOneVector':
#         if aveVal <-0.5:
#             aveVal = torchhd.negative(aveVal)
#         aveVal = aveVal.numpy()
#         aveVal = float(aveVal)
#         roundAveVal = round(aveVal)
#     else:
#         roundAveVal = 0
#     return roundAveVal

def getTotalNumBinds(bundleVector):
    res = torch.max(bundleVector)
    res = res.numpy()
    res = int(res)
    return res

# # e.g. how many horse*(value) in PersonOne bundle?
def getNumInstances_atomic(bundle, atomicVector):
    # Bind against the atomic negative
    atomicName = Globals.integratedBrain_vectorMemory.__getitem__(atomicVector)
    atomicName = atomicName[1]

    searchName = atomicName + "-"
    # list of words
    atomicBindList = []
    # unique words
    atomicBindUniqueNum = 0
    # total words
    atomicBindTotalNum = 0

    # iterate through pair dictionary to find pairs
    for vectorName in Globals.pair_VectorDictionary:
        if searchName in vectorName:
            vector = Globals.pair_VectorDictionary[vectorName]
            bindQ = doesBundleContainBind_count(bundle,vector )
            if bindQ > 0:
                atomicBindList.append(vectorName)
                atomicBindUniqueNum = atomicBindUniqueNum + 1
                atomicBindTotalNum = atomicBindTotalNum + bindQ
    return atomicBindList, atomicBindUniqueNum, atomicBindTotalNum    

# # e.g. how many horse*(value) in PersonOne bundle and rank the answers?
def getRankedNumInstances_atomic(bundle, atomicVector):
    # Bind against the atomic negative
    atomicName = Globals.integratedBrain_vectorMemory.__getitem__(atomicVector)
    atomicName = atomicName[1]

    searchName = atomicName + "-"
    # list of words
    atomicBindDict = {}
    # unique words
    atomicBindUniqueNum = 0
    # total words
    atomicBindTotalNum = 0
    # iterate through pair dictionary to find pairs
    for vectorName in Globals.pair_VectorDictionary:
        if searchName in vectorName:
            vector = Globals.pair_VectorDictionary[vectorName]
            bindQ = doesBundleContainBind_count(bundle,vector )
            if bindQ > 0:
                atomicBindDict[vectorName] = bindQ
                atomicBindUniqueNum = atomicBindUniqueNum + 1
                atomicBindTotalNum = atomicBindTotalNum + bindQ
    
    atomicBindDict_sorted = sorted(atomicBindDict.items(), key=lambda x:x[1], reverse=True)
    return atomicBindDict_sorted    

# e.g. What does the network think about "horse"?
def getRankedNetworkBelief_brain(atomicVector):
    # Get the belief states of the network associated with an atomic vecgyor (e.g. the vector for 'horse')
    # Bind against the atomic negative
    atomicName = Globals.integratedBrain_vectorMemory.__getitem__(atomicVector)
    atomicName = atomicName[1]
    bundle = Globals.special_VectorDictionary['SPECIAL_caseBundle_persBundle']
    searchName = atomicName + "-"
    # list of words
    atomicBindDict = {}
    # unique words
    atomicBindUniqueNum = 0
    # total words
    atomicBindTotalNum = 0
    # iterate through pair dictionary to find pairs
    for vectorName in Globals.pair_VectorDictionary:
        if searchName in vectorName:
            vector = Globals.pair_VectorDictionary[vectorName]
            bindQ = doesBundleContainBind_count(bundle,vector )
            if bindQ > 0:
                atomicBindDict[vectorName] = bindQ
                atomicBindUniqueNum = atomicBindUniqueNum + 1
                atomicBindTotalNum = atomicBindTotalNum + bindQ
    
    atomicBindDict_sorted = sorted(atomicBindDict.items(), key=lambda x:x[1], reverse=True)
    return atomicBindDict_sorted    

# e.g. What does the network think about "horse"?
def getRankedNetworkBelief_sm(atomicVector):
    # Get the belief states of the network associated with an atomic vecgyor (e.g. the vector for 'horse')
    # Bind against the atomic negative
    atomicName = Globals.integratedBrain_vectorMemory.__getitem__(atomicVector)
    atomicName = atomicName[1]
    bundle = Globals.special_VectorDictionary['SPECIAL_caseBundle_smBundle']
    searchName = atomicName + "-"
    # list of words
    atomicBindDict = {}
    # unique words
    atomicBindUniqueNum = 0
    # total words
    atomicBindTotalNum = 0
    # iterate through pair dictionary to find pairs
    for vectorName in Globals.pair_VectorDictionary:
        if searchName in vectorName:
            vector = Globals.pair_VectorDictionary[vectorName]
            bindQ = doesBundleContainBind_count(bundle,vector )
            if bindQ > 0:
                atomicBindDict[vectorName] = bindQ
                atomicBindUniqueNum = atomicBindUniqueNum + 1
                atomicBindTotalNum = atomicBindTotalNum + bindQ
    
    atomicBindDict_sorted = sorted(atomicBindDict.items(), key=lambda x:x[1], reverse=True)
    return atomicBindDict_sorted    

# e.g. What does the network think about "horse"?
def getStandardDeviationBelief_brain(atomicVector):
    # Get the belief states of the network associated with an atomic vecgyor (e.g. the vector for 'horse')
    # Bind against the atomic negative
    atomicName = Globals.integratedBrain_vectorMemory.__getitem__(atomicVector)
    atomicName = atomicName[1]
    bundle = Globals.special_VectorDictionary['SPECIAL_caseBundle_persBundle']
    searchName = atomicName + "-"
    # list of words
    atomicBindDict = {}
    # unique words
    atomicBindUniqueNum = 0
    # total words
    atomicBindTotalNum = 0
    # iterate through pair dictionary to find pairs
    for vectorName in Globals.pair_VectorDictionary:
        if searchName in vectorName:
            vector = Globals.pair_VectorDictionary[vectorName]
            bindQ = doesBundleContainBind_count(bundle,vector )
            if bindQ > 0:
                atomicBindDict[vectorName] = bindQ
                atomicBindUniqueNum = atomicBindUniqueNum + 1
                atomicBindTotalNum = atomicBindTotalNum + bindQ
    
    atomicBindDict_sorted = sorted(atomicBindDict.items(), key=lambda x:x[1], reverse=True)

    numberList = []



    for item in  atomicBindDict_sorted:
        newNum = item[1]
        numberList.append(newNum)
    
    standardDev = statistics.stdev(numberList)
    return standardDev    

# e.g. What does the network think about "horse"?
def getStandardDeviationBelief_sm(atomicVector):
    # Get the belief states of the network associated with an atomic vecgyor (e.g. the vector for 'horse')
    # Bind against the atomic negative
    atomicName = Globals.integratedBrain_vectorMemory.__getitem__(atomicVector)
    atomicName = atomicName[1]
    bundle = Globals.special_VectorDictionary['SPECIAL_caseBundle_smBundle']
    searchName = atomicName + "-"
    # list of words
    atomicBindDict = {}
    # unique words
    atomicBindUniqueNum = 0
    # total words
    atomicBindTotalNum = 0
    # iterate through pair dictionary to find pairs
    for vectorName in Globals.pair_VectorDictionary:
        if searchName in vectorName:
            vector = Globals.pair_VectorDictionary[vectorName]
            bindQ = doesBundleContainBind_count(bundle,vector )
            if bindQ > 0:
                atomicBindDict[vectorName] = bindQ
                atomicBindUniqueNum = atomicBindUniqueNum + 1
                atomicBindTotalNum = atomicBindTotalNum + bindQ
    
    atomicBindDict_sorted = sorted(atomicBindDict.items(), key=lambda x:x[1], reverse=True)

    numberList = []



    for item in  atomicBindDict_sorted:
        newNum = item[1]
        numberList.append(newNum)
    
    standardDev = statistics.stdev(numberList)
    return standardDev    



# Get a list of the common atoms in two bundles
def getCommonAtomic(bundleOne, bundleTwo):

    commonDict = {}
    for vectorName in Globals.atomic_VectorDictionary:
        vector = Globals.atomic_VectorDictionary[vectorName]
        resOne = getNumInstances_atomic(bundleOne,vector)
        resOne= resOne[2]
        resTwo = getNumInstances_atomic(bundleTwo,vector)
        resTwo= resTwo[2]
        if resOne > 0 and resTwo > 0:
            # If there is an atomic match for both: find the avaerage between the values and the difference between the values.
            average = resOne + resTwo
            average = average / 2
            average = int(average)
            difference = resOne - resTwo
            difference = abs(difference)
            difference = int(difference)
            commonDict[vectorName] = [average, difference]

    commonDict = sorted(commonDict.items(), key=lambda x:x[1], reverse=True)
    
    return commonDict
    
# Get the most common vector pairs in two bundles
def getCommonPairs(bundleOne, bundleTwo):
    commonPairDict = {}
    for name in Globals.pair_VectorDictionary:
        pairVector = Globals.pair_VectorDictionary[name]
        
        personOneCheck = doesBundleContainBind_count(bundleOne, pairVector)
        # check if both people have bind and if so add to dict
        if personOneCheck > 0:
            personTwoCheck = doesBundleContainBind_count(bundleTwo, pairVector)
            if personTwoCheck > 0:
                average = personOneCheck + personTwoCheck
                average = average / 2
                average = int(average)
                difference = personOneCheck - personTwoCheck
                difference = abs(difference)
                difference = int(difference)
                commonPairDict[name] = [average, difference]

    commonPairDict = sorted(commonPairDict.items(), key=lambda x:x[1], reverse=True)
    return commonPairDict 

# Get the most common atomic vector in two bundles
def getCommonAtomic_newVersion(bundleOne, bundleTwo):
    bundleOneCount = {name: 0 for name in Globals.atomic_VectorDictionary}
    bundleTwoCount = {name: 0 for name in Globals.atomic_VectorDictionary}
    finalCount = {}
    # Can be altered
    similarityThreshhold = 0.05
    # Analyse bundleOne
    for label, vector in Globals.pair_VectorDictionary.items():
        
        if torchhd.cosine_similarity(bundleOne, vector) >= similarityThreshhold:
            wordOne, wordTwo = label.split('-')
            tempval = bundleOneCount[wordOne] 
            tempval = tempval + 1
            bundleOneCount[wordOne] = tempval
            tempval = bundleOneCount[wordTwo] 
            tempval = tempval + 1
            bundleOneCount[wordTwo] = tempval
    
    # Analyse bundleTwo
    for label, vector in Globals.pair_VectorDictionary.items():
        if torchhd.cosine_similarity(bundleTwo, vector) >= similarityThreshhold:
            tempval = bundleTwoCount[wordOne] 
            tempval = tempval + 1
            bundleTwoCount[wordOne] = tempval
            tempval = bundleTwoCount[wordTwo] 
            tempval = tempval + 1
            bundleTwoCount[wordTwo] = tempval

    for name, vector in Globals.atomic_VectorDictionary.items():
        if bundleOneCount[name] > 0 and bundleTwoCount[name] > 0:
            average = bundleOneCount[name] + bundleTwoCount[name]
            average = average / 2
            difference = bundleOneCount[name] - bundleTwoCount[name]
            difference = abs(difference)
            difference = int(difference)
            finalCount[name] = [average, difference]
    
    return finalCount

# ---------- Vector Processing ----------

# Converts a string into a bundle that contains the paired binds of words
# Eg. I like horses = I x Like + Like x Horses
def convertStringToBundleOfBinds(contentString):
    remChar = "~!#$%^&*()_+`-=[]\\\{\}|;\':\",./<>?"
    contentString = contentString.lower()
    contentArray = contentString.split(" ")
    arraySize = len(contentArray)
    countLim = arraySize-1
    count = 0
    currentBundle = None
    # Goes through each word pair and adds to the atomic dictionary if needed
    # Then adds the pairs into a bundle for the media content
    for wordOne in contentArray:
        if count<countLim:
            wordTwo = contentArray[count+1]
            wordOne = wordOne.translate(str.maketrans('', '', remChar))
            wordTwo = wordTwo.translate(str.maketrans('', '', remChar))
            if not Checks.checkAtomicExists(wordOne):
                newAtomicVector(wordOne)
            if not Checks.checkAtomicExists(wordTwo):
                newAtomicVector(wordTwo)
            wordPair = f'{wordOne}-{wordTwo}'
            if not Checks.checkPairExists(wordPair):
                newVectorLabelPair(wordOne, wordTwo)
            response=Globals.pair_VectorDictionary[wordPair]
            if count == 0:
                    response=Globals.pair_VectorDictionary[wordPair]
                    currentBundle = response
            else:
                currentBundle = torchhd.bundle(currentBundle,response)
        count = count+1

    return currentBundle


# ---------- Misc ----------


# COnvert the memory object into a VSA tensor
def createVsaTensorsFromMemory():
    #tensor = [torchhd.ensure_vsa_tensor(hv) for hv in Globals.integratedBrain_vectorMemory.keys]
    tensor = torch.stack(Globals.integratedBrain_vectorMemory.keys, dim=0)
    return tensor

# UNFINISHED def getRangeOfBinds_person(personObj, atomicVector):
#     # Gets the range of binds associated with an atomic vector and a person
#     personBundle = personObj.persBundle
    
#     result = getNumInstances_atomic(personBundle, atomicVector)
    


# ---------- Misc ----------

def main():
    vectorInput = torchhd.random(10,10000)
    print(compareVectors(vectorInput[0], vectorInput[1]))

if __name__ == "__main__":
    main()

