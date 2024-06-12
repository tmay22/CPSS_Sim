import Globals
import VectorFunction_Brain

def doesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics. e.g. like and horse
    print("----------------------------------------")
    print("Does Person Contain Paired Association?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give first word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give second word: ")
    print("You input: " + wordTwo)
   
    # General error check of inputs
    if not checkPersonExists(personId):
        return
    elif not checkAtomicExists(wordOne):
        return
    elif not checkAtomicExists(wordTwo):
        return
    
    print("----------------------------------------")

    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    wordPair = wordOne + "-" + wordTwo
    result = Globals.VectorFunction_Brain.doesPersContPair_bool(persObj, wordPair)
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'RESULT: {result}')
    return


def howManyDoesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics and HOW MANY. e.g. like and horse
    print("----------------------------------------")
    print("Does Person Contain Paired Association?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give first word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give second word: ")
    print("You input: " + wordTwo)
   
    # General error check of inputs
    if not checkPersonExists(personId):
        return
    elif not checkAtomicExists(wordOne):
        return
    elif not checkAtomicExists(wordTwo):
        return
    
    print("----------------------------------------")
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    wordPair = wordOne + "-" + wordTwo
    result = Globals.VectorFunction_Brain.doesPersContPair_numInst(persObj, wordPair)
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'RESULT: {result}')
    return


# ----------------------------------------------
# Utils / Checks
# ----------------------------------------------

def checkPersonExists(personId):
    if personId not in Globals.personDict.keys():
        print(f'ERROR: PersonID {personId} does not exist in dictionary')
        return False
    else:
        return True

def checkAtomicExists(word):
    if word not in Globals.atomic_VectorDictionary.keys():
        print(f'ERROR, second word {word} does not exist in dictionary')
        return False
    else:
        return True