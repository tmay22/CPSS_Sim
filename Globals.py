import torchhd
import torch
import itertools
import VectorFunction


# A Vector Memory (VM) that contains both the atomic vectors, and bundles for all of the Persons
# ITNEGRATES all of the Person brains together into one VM
global integratedBrain_vectorMemory
integratedBrain_vectorMemory = torchhd.structures.Memory(0.0)

# Create vector dictionary for individual words
global atomic_VectorDictionary
atomic_VectorDictionary = {}

# Create vector dictionary for pairs of works
global pair_VectorDictionary 
pair_VectorDictionary = {}

# Create vector dictionary for trios: Person x Pairs
global trio_VectorDictionary 
trio_VectorDictionary = {}

# Storage mechanism of SPECIAL Keys - i.e. posOneVector, negOneVector, caseBundle
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