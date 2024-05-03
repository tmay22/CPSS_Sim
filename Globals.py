import torchhd
import torch
import itertools
import VectorFunction

# Create vector memory for a brain
global brain_vectorMemory
brain_vectorMemory = torchhd.structures.Memory(0.0)

# Create vector dictionary for individual words
global atomic_VectorDictionary
atomic_VectorDictionary = {}

# Create vector dictionary for pairs of works
global pair_VectorDictionary 
pair_VectorDictionary = {}


# List of all Edge objects
global edgeList
edgeList = []

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