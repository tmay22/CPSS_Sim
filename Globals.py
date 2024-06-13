import torchhd
import torch
import itertools
import VectorFunction_Brain


# A Vector Memory (VM) that contains both the atomic vectors, and bundles for all of the Persons
# ITNEGRATES all of the Person brains together into one VM
global integratedBrain_vectorMemory
integratedBrain_vectorMemory = torchhd.structures.Memory(0.0)


# STRETCH - REPRESENT SM DATA AS ITS OWN VM
# global integratedSocialMedia_vectorMemory
# integratedSocialMedia_vectorMemory = torchhd.structures.Memory(0.0)


# Create vector dictionary for individual words
global atomic_VectorDictionary
atomic_VectorDictionary = {}

# Create vector dictionary for pairs of works
global pair_VectorDictionary 
pair_VectorDictionary = {}

# Create vector dictionary for trios: Person x Pairs
global trio_VectorDictionary 
trio_VectorDictionary = {}

# Storage mechanism of SPECIAL Keys - i.e. posOneVector, negOneVector, caseBundle_persBind, and caseBundle_persBundle
# posOneVector is a vector that is only +1
# negOneVector is a vector that is only -1
# caseBundle_persBind is a vector bundle of all trio_Vectors in the memory (i.e. Person x Word 1 x Word 2)
# caseBunle_persBundle is a vector bundle of all pair_Vectors in memory without a Person bind attached (i.e. Word 1 x Word 2)
global special_VectorDictionary
special_VectorDictionary = {}

# List of all personIds
global personDict
personDict = {}
# Note that the vector memories of each individual person only have their Person's value-pairs.
# If you want the atomic values you need to query the global vector memory


# --------------------------------
### Below is only if you wanted to go down a VSA path for the social network
# --------------------------------

# Create vector memory for a network
# global network_vectorMemory
# network_vectorMemory = torchhd.structures.Memory(0.0)

# Create vector dictionary for individual persons
# global person_VectorDictionary
# person_VectorDictionary = {}

# Create vector ductuibart for edges between two people
# global edge_VectorDictionary
# edge_VectorDictionary = {}