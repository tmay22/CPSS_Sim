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
   
    # Convert words to lower case
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()

    # General error check of inputs
    wordPair = wordOne + "-" + wordTwo
    if not checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    elif not checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    elif not checkAtomicExists(wordTwo):
        print(f'{wordTwo} does not exist')
        return
    elif not checkPairExists(wordPair):
        print(f'RESULT: {personId} does not contain {wordPair}')
        return
    
    print("----------------------------------------")

    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    
    result = Globals.VectorFunction_Brain.doesPersContPair_bool(persObj, wordPair)
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    print(f'RESULT: {result}')
    return


def howManyDoesPersContainPair():
    # CHeck to see if a person contains a binded pair of topics and HOW MANY. e.g. like and horse
    print("----------------------------------------")
    print("How Many Results Does a Person Contain of a Paired Association?")
    print("----------------------------------------")
    # COllect inputs
    personId= input("Give PersonId: ")
    print("Your input: " + personId)
    wordOne= input("Give first word: ")
    print("You input: " + wordOne)
    wordTwo= input("Give second word: ")
    print("You input: " + wordTwo)
   
    print("----------------------------------------")
    print(f'Checking if PersonId {personId} contains {wordOne}-{wordTwo} pair...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()
    wordTwo = wordTwo.lower()
    
    # General error check of inputs
    wordPair = wordOne + "-" + wordTwo
    if not checkPersonExists(personId):
        print(f'{personId} does not exist')
        return
    elif not checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    elif not checkAtomicExists(wordTwo):
        print(f'{wordTwo} does not exist')
        return
    elif not checkPairExists(wordPair):
        print(f'RESULT: {personId} does not contain {wordPair}')
        return
    
    # CHeck and call vector function
    persObj = Globals.personDict[personId]
    wordPair = wordOne + "-" + wordTwo
    result = Globals.VectorFunction_Brain.doesPersContPair_numInst(persObj, wordPair)

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

def checkPairExists(wordPair):
    if wordPair not in Globals.pair_VectorDictionary.keys():
        print(f'ERROR, second word {wordPair} does not exist in dictionary')
        return False
    else:
        return True
    
def checkTrioExists(wordTrio):
    if wordTrio not in Globals.trio_VectorDictionary.keys():
        print(f'ERROR, second word {wordTrio} does not exist in dictionary')
        return False
    else:
        return True