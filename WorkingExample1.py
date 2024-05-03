import torchhd
import torch
import itertools
import VectorFunction
import Globals
import pandas


# Create vector memory 
#global Globals.vectorMemory
#Globals.vectorMemory = torchhd.structures.Memory(0.0)
    

def main():

    # ----------------------------------------------------------------------------------------------------------------------------------
    # SETUP
    # ----------------------------------------------------------------------------------------------------------------------------------

    # Insert list of atomic strings (the base vectors) 
    
    print(f'------SETUP--------' )

    global atomicList 
    atomicList = ["computer", "linux", "persistence", "cronjob", "windows", "registry", "psexec", "process", "server", "gpo", "lsass", "credDump"]
    numAtoms = len(atomicList)

    # Num dimensions per vector
    d = 10000

    
    # Generate hypervectors for the atomic units unassigned to labels
    vectorGen = torchhd.random(numAtoms,d)

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

    # Create every Permutation of 2 atomic vectors (doesn't matter order, but duplicates are ok because they will have same value i.e. AB vs BA)
    
    # Globals.pair_VectorDictionary = {}
    for vectorOne in Globals.atomic_VectorDictionary:
        for vectorTwo in Globals.atomic_VectorDictionary:          
                newVal = torchhd.bind(Globals.atomic_VectorDictionary[vectorOne],Globals.atomic_VectorDictionary[vectorTwo])
                newName = vectorOne + "-" + vectorTwo
                Globals.pair_VectorDictionary[newName] = newVal
    
    print(f'No. items in atom_VectorDictionary : ' + str(len(Globals.atomic_VectorDictionary)))
    print(f'No. items in Globals.pair_VectorDictionary: ' + str(len(Globals.pair_VectorDictionary)))

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

    print("Configuration complete!\n")

    # ----------------------------------------------------------------------------------------------------------------------------------    
    # DATA ENTRY TIME
    # ----------------------------------------------------------------------------------------------------------------------------------


    # In this example, there are 3 bundles - AKA Tickets in the incident response investigation

    ticketList = {}

    ticket_1_wordPairs = ("computer-linux","persistence-cronjob")
    count = 0
    # Must be in format "ItemA-ItemB"
    for pair in ticket_1_wordPairs:
        dictTerm = pair
        if count == 0:
            ticket_1 = Globals.pair_VectorDictionary[dictTerm]
        else:
            ticket_1 = torchhd.bundle(ticket_1,Globals.pair_VectorDictionary[dictTerm])
        count = count + 1
    ticketList["ticket_1"] = ticket_1

    # Checks - Passed
    #print(torchhd.cosine_similarity(ticket_1, torchhd.bind(Globals.atomic_VectorDictionary["computer"],Globals.atomic_VectorDictionary["linux"])))
    #ticket_1b = torchhd.bundle(Globals.pair_VectorDictionary["pair_computer-linux"],Globals.pair_VectorDictionary["pair_persistence-cronjob"])
    #print(torchhd.cosine_similarity(ticket_1,ticket_1b))

    ticket_2_wordPairs = ("computer-windows","persistence-registry","psexec-process")
    count = 0
    # Must be in format "ItemA-ItemB"
    for pair in ticket_2_wordPairs:
        dictTerm = pair
        if count == 0:
            ticket_2 = Globals.pair_VectorDictionary[dictTerm]
        else:
            ticket_2 = torchhd.bundle(ticket_2,Globals.pair_VectorDictionary[dictTerm])
        count = count + 1
    ticketList["ticket_2"] = ticket_2

    ticket_3_wordPairs = ("server-windows","persistence-gpo","lsass-credDump","persistence-registry")
    count = 0
    # Must be in format "ItemA-ItemB"
    for pair in ticket_3_wordPairs:
        dictTerm =  pair
        if count == 0:
            ticket_3 = Globals.pair_VectorDictionary[dictTerm]
        else:
            ticket_3 = torchhd.bundle(ticket_3,Globals.pair_VectorDictionary[dictTerm])
        count = count + 1
    ticketList["ticket_3"] = ticket_3

    # Add 3 tickets into memory
    for ticket in ticketList:
        Globals.brain_vectorMemory.add(ticketList[ticket], ticket)
    
    ticket_all = torchhd.bundle(torchhd.bundle(ticket_1, ticket_2),ticket_3)
    Globals.brain_vectorMemory.add(ticket_all, "ticket_all")

    
    # ----------------------------------------------------------------------------------------------------------------------------------
    # TEST SPACE
    # ----------------------------------------------------------------------------------------------------------------------------------

    # -----------
    # Test One
    # -----------
    # Calculate the SImilarity between ticket_1 and ticket_2

    res = VectorFunction.compareVectors(ticket_1, ticket_2)
    res = res.numpy()
    print(f'------Test One--------' )
    print(f'Similarity between ticket_1 and ticket_2: \n' + str(res) + '(0 is orthogonal, 1 is same) \n')

    


    # -----------
    # Test Two
    # -----------
    # How many instances of the "persistance-registry" bind?

    res = VectorFunction.getNumInstances_bind(ticket_all, Globals.pair_VectorDictionary["persistence-registry"])
    
    print(f'------Test Two--------' )
    print(f'Approx number of\'Persistence-registry\' pairings: \n' + str(res) + ' \n')
    

   
    # -----------
    # Test 3
    # -----------
    # How many binds in a bundle in total?

    res = VectorFunction.getTotalNumBinds(ticket_all)

    print(f'------Test Three--------' )
    print(f'Approx number of binds total in the ticket_all bundle: \n' + str(res) + ' \n')
    print("UP TO HERE")

    # -----------
    # Test XX -UP TO HERE
    # -----------
    # What is distro of words?

    word_res = torchhd.bind((torchhd.permute(ticket_all)),ticket_all)
    
    df = pandas.DataFrame({
        "word": Globals.atomic_VectorDictionary,
        "word_res": word_res
    })

    print(df)
    print("hi")


   
    # -----------
    # Test Four -UP TO HERE
    # -----------
    # How many instances of the "persistance" atom

    filter = torchhd.bind(Globals.atomic_VectorDictionary["persistence"], ticket_all)
    resList = []
    #HALFWAY HERE _ INstead look at the -1 thing to check if an item is contained.
    for entry in Globals.atomic_VectorDictionary:
        calc = torchhd.cosine_similarity(Globals.atomic_VectorDictionary[entry],filter)
        if calc > 0.5:
            resList = resList.append(entry)

    print(f'------Test FOur--------' )
    print(f'Approx number of binded pairs with "persistence": \n' )
    
    print(resList)

    print("UP TO HERE")

    #negAns = torchhd.bind((torchhd.negative(Globals.atomic_VectorDictionary["persistence"])),ticket_all)
    query = torchhd.permute(Globals.atomic_VectorDictionary["persistence"])
    res = torchhd.cosine_similarity(query, ticket_all)
    res2 = torchhd.dot_similarity(query, ticket_all)
    print("here")
    #resMinus = torchhd.bundle(negAns,res)

    #absVal = torch.abs(resMinus)
    #aveAbsVal = torch.mean(resMinus)
 

    #topVal = torch.max(resMinus)
    #bottomVal = torch.min(resMinus)
    #aveVal = torch.mean(resMinus)
    


    #absValAve_divTwo = torch.mean(absVal)/2

    #print("here")

    #res = torchhd.bind(Globals.atomic_VectorDictionary["persistence"],ticket_all)
   

    # print(f'------Test Two--------' )
    # print(f'Nature of Persistence' )
    # print(f'TopVal: ' + str(topVal) + '\nAveVal: ' + str(aveVal) + '\nBottomVal: ' + str(bottomVal))
    # print(f'AbsVal' + str(absVal))
    # print(f'AbsValAve_divTwo' + str(absValAve_divTwo))
    # print(f'-' )
    # print(f'cronjob' + str(Globals.atomic_VectorDictionary["cronjob"]))
    # print(f'registry' + str(Globals.atomic_VectorDictionary["registry"]))
    # print(f'gpo' + str(Globals.atomic_VectorDictionary["gpo"]))
    
    # print(f'res' + str(res))

    res2 = Globals.brain_vectorMemory.__getitem__(res)


    # -----------
    # Test 4 - UNFINISHED
    # -----------
    # What is 'persistence' paired to across all tickets? - SHould return 3 results

    
    
    #print(res2)
    #print(f'------------\n \'Persistence\' Pairings: \n' + str(res) + ' \n')

    
   

    



    print("x")

    
    
    
    
    Bun_1 = "a"

    print("---------------------------------------")
    print("hello")  

if __name__ == "__main__":
    main()

