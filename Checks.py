import Globals
# ----------------------------------------------
# Utils / Checks
# ----------------------------------------------

def checkPersonExists(personId):
    if personId not in Globals.personDict.keys():
        #print(f'ERROR: PersonID {personId} does not exist in dictionary')
        return False
    else:
        return True

def checkAtomicExists(word):
    if word not in Globals.atomic_VectorDictionary.keys():
        #print(f'ERROR, second word {word} does not exist in dictionary')
        return False
    else:
        return True

def checkPairExists(wordPair):
    if wordPair not in Globals.pair_VectorDictionary.keys():
        #print(f'ERROR, second word {wordPair} does not exist in dictionary')
        return False
    else:
        return True
    
def checkTrioExists(wordTrio):
    if wordTrio not in Globals.trio_VectorDictionary.keys():
        #print(f'ERROR, second word {wordTrio} does not exist in dictionary')
        return False
    else:
        return True
    