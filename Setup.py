from ConfigObjects import *
from NetworkObjects import *
import numpy
import random



def build(setupOption):

    global currentSetting

    

    if setupOption == "1":
        currentSetting = generateDefaultSettings()
        print("Default Settings Generated")
    elif setupOption == "2":
        currentSetting=generateSmallSettings()

    network = generateNetwork(currentSetting)
    #print(currentSetting)
    #Note that you can generate a build or input a dataset

def generateDefaultSettings():

    #See ConfigObjects.py and NetworkObjects.py  for variable definitions

    # Note that the default build distributes people in connection to each other randomly and does not prioritise their similarities in network building.
    # The default build contains 100 people, averaging 10 connections each, with a SD variance of 5.
    # The default build uses the standard variables mean as 50 and the SD as 34 generally for variables.
    # The default build person has on average 5 concepts and 5 facts per concept, with each an SD of 2.

    numConcepts = 20

    numPeople = 100
    numPeopleEdges_mean = 10
    numPeopleEdges_scale = 5

    numPeopleConcepts_mean = 5
    numPeopleConcepts_scale = 2

    personInfluenceOpeness_mean = 50
    personInfluenceOpeness_scale = 34

    personNuance_mean = 2
    personNuance_scale = 0.3

    personInteractiveness_mean = 50
    personInteractiveness_scale = 34

    personKlout_mean = 50
    personKlout_scale = 34

    personTrustingOthers_mean = 50
    personTrustingOthers_scale = 34

    conceptFactNum_mean=5
    conceptFactNum_scale=2

    changeThreshold_mean = 10
    changeThreshold_scale = 2
    
    discriminationThreshold_mean = 5
    discriminationThreshold_scale = 1

    global currentSetting
    currentSetting = Settings(numConcepts, numPeople, numPeopleEdges_mean, numPeopleEdges_scale, numPeopleConcepts_mean, numPeopleConcepts_scale, personInfluenceOpeness_mean, personInfluenceOpeness_scale, personNuance_mean, personNuance_scale, personInteractiveness_mean, personInteractiveness_scale, personKlout_mean, personKlout_scale, personTrustingOthers_mean, personTrustingOthers_scale, changeThreshold_mean, changeThreshold_scale, discriminationThreshold_mean, discriminationThreshold_scale, conceptFactNum_mean, conceptFactNum_scale)
    print(currentSetting)
    return currentSetting

def generateSmallSettings():

    #See ConfigObjects.py and NetworkObjects.py  for variable definitions

    # Note that the default build distributes people in connection to each other randomly and does not prioritise their similarities in network building.
    # The default build contains 100 people, averaging 10 connections each, with a SD variance of 5.
    # The default build uses the standard variables mean as 50 and the SD as 34 generally for variables.
    # The default build person has on average 5 concepts and 5 facts per concept, with each an SD of 2.

    numConcepts = 20

    numPeople = 10
    numPeopleEdges_mean = 3
    numPeopleEdges_scale = 1

    numPeopleConcepts_mean = 5
    numPeopleConcepts_scale = 2

    personInfluenceOpeness_mean = 50
    personInfluenceOpeness_scale = 34

    personNuance_mean = 2
    personNuance_scale = 0.3

    personInteractiveness_mean = 50
    personInteractiveness_scale = 34

    personKlout_mean = 50
    personKlout_scale = 34

    personTrustingOthers_mean = 50
    personTrustingOthers_scale = 34

    changeThreshold_mean = 10
    changeThreshold_scale = 2
    
    discriminationThreshold_mean = 5
    discriminationThreshold_scale = 1

    conceptFactNum_mean=5
    conceptFactNum_scale=2

    global currentSetting
    currentSetting = Settings(numConcepts, numPeople, numPeopleEdges_mean, numPeopleEdges_scale, numPeopleConcepts_mean, numPeopleConcepts_scale, personInfluenceOpeness_mean, personInfluenceOpeness_scale, personNuance_mean, personNuance_scale, personInteractiveness_mean, personInteractiveness_scale, personKlout_mean, personKlout_scale, personTrustingOthers_mean, personTrustingOthers_scale, changeThreshold_mean, changeThreshold_scale, discriminationThreshold_mean, discriminationThreshold_scale, conceptFactNum_mean, conceptFactNum_scale)
    print(currentSetting)
    return currentSetting


def generateNetwork(currentSetting):
    # Step 1 make people
    personKey = 1
    count = 0
    global personList
    personList = []

    # SD generation for People objects
    influenceOpenessArray = numpy.random.normal(currentSetting.personInfluenceOpeness_mean, currentSetting.personInfluenceOpeness_scale, currentSetting.numPeople)
    nuanceArray= numpy.random.normal(currentSetting.personNuance_mean, currentSetting.personNuance_scale, currentSetting.numPeople)
    interactivenessArray= numpy.random.normal(currentSetting.personInteractiveness_mean, currentSetting.personInteractiveness_scale, currentSetting.numPeople)
    kloutArray= numpy.random.normal(currentSetting.personKlout_mean, currentSetting.personKlout_scale, currentSetting.numPeople)
    trustingOthersArray = numpy.random.normal(currentSetting.personTrustingOthers_mean, currentSetting.personTrustingOthers_scale, currentSetting.numPeople)
    changeThresholdArray = numpy.random.normal(currentSetting.changeThreshold_mean, currentSetting.changeThreshold_scale, currentSetting.numPeople)
    discriminationThresholdArray = numpy.random.normal(currentSetting.discriminationThreshold_mean, currentSetting.discriminationThreshold_scale, currentSetting.numPeople)

    
    # Build the number of people required. Does not include their connections, concepts or facts.
    while count < currentSetting.numPeople:
        key = f"P{personKey}"

        influenceOpenness = influenceOpenessArray[count]
        influenceOpenness = round(influenceOpenness)
        if influenceOpenness > 100:
            influenceOpenness = 100
        if influenceOpenness < 0:
            influenceOpenness = 0

        nuance = nuanceArray[count]
        nuance = round(nuance)
        if nuance > 3:
            nuance = 3
        if nuance < 1:
            nuance = 1

        interactiveness = interactivenessArray[count]
        interactiveness = round(interactiveness)
        if interactiveness > 100:
            interactiveness = 100
        if interactiveness < 0:
            interactiveness = 0

        klout = kloutArray[count]
        klout = round(klout)
        if klout > 100:
            klout = 100
        if klout < 0:
            klout = 0

        trustingOthers = trustingOthersArray[count]
        trustingOthers = round(trustingOthers)
        if trustingOthers > 100:
            trustingOthers = 100
        if trustingOthers < 0:
            trustingOthers = 0

        changeThreshold = changeThresholdArray[count]
        changeThreshold = round(changeThreshold)
        if changeThreshold > 100:
            changeThreshold = 100
        if changeThreshold < 0:
            changeThreshold = 0

        discriminationThreshold = discriminationThresholdArray[count]
        discriminationThreshold = round(discriminationThreshold)
        if discriminationThreshold > 100:
            discriminationThreshold = 100
        if discriminationThreshold < 0:
            discriminationThreshold = 0
        
        personList.append(Person(key, influenceOpenness, nuance, interactiveness, klout, trustingOthers, changeThreshold, discriminationThreshold))

        personKey=personKey+1
        count=count+1

    print("done!")

    # Step 2. Make concepts for people
    numConceptArray = numpy.random.normal(currentSetting.numPeopleConcepts_mean, currentSetting.numPeopleConcepts_scale, currentSetting.numPeople)
    
    
    personCount=0

    # For each person you have generated, allocate concepts to their brain and facts
    for eachPers in personList:
        conceptKey = 1
        numConceptsThisPers=0

        numConceptsAllocated=numConceptArray[personCount]
        numConceptsAllocated=round(numConceptsAllocated)
        if numConceptsAllocated < 0:
            numConceptsAllocated = 0

        # whilst this person has less concepts than those allocated in the SD, create new concepts
        while numConceptsThisPers<numConceptsAllocated:
            
            # work out the number of facts for this concept
            numFactsAlloc = numpy.random.normal(currentSetting.conceptFactNum_mean, currentSetting.conceptFactNum_scale)
            numFactsAlloc = round(numFactsAlloc)
            if numFactsAlloc < 0:
                numFactsAlloc = 0

            numFactsActual = 0
            factKey = 1
    
            # unique key for this concept's initialisation 
            newConceptKey=f"{eachPers.key}-C{conceptKey}"
            
            # name/category of concept based on number of existing 
            newConceptName=random.randint(1,currentSetting.numConcepts)
            
            # empty list for that concept
            tempFactList = []

            # whilst there are not all the allocated facts for this concept, generate facts
            while numFactsActual < numFactsAlloc:
                
                newFactKey = f"{newConceptKey}-F{factKey}"
                #RGB for 3 colour dimensions (i.e. nuance)
                if eachPers.nuance >= 1:
                    colourR = random.randint(1, 255)
                if eachPers.nuance >= 2:
                    colourG = random.randint(1,255)
                else:
                    colourG = 0
                if eachPers.nuance >= 3:
                    colourB = random.randint(1,255)
                else:
                    colourB = 0
                factValue=[colourR, colourG, colourB]
                # May want to change the lastupdate and weight defaults later
                lastupdate = 0
                weight = 1

                tempFactList.append(Fact(newFactKey, factValue, lastupdate, weight))

                numFactsActual = numFactsActual + 1
                factKey = factKey + 1

            # Now, add the new concept and its associated factlist to the person
            tempConcept=Concept(newConceptKey, newConceptName, tempFactList)
            eachPers.conceptMap.append(tempConcept)
            numConceptsThisPers = numConceptsThisPers + 1
            conceptKey = conceptKey + 1
        personCount = personCount + 1
    print("we generated the peeps!")

    # Step 3. Make edges for people.

    # SD generation for networkforeach loop p
        
# 



def inputDataset():
    print('tbc')





# Deault Setup: assigns values based on basic template

# Template 1 - Blank Brains (No concept maps filled per person)

# Template x Setup

# Custom setup: person inputs values
    
