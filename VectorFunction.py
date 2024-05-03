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
def compareVectors(vector1, vector2):
    return torchhd.cosine_similarity(vector1, vector2)
    
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

def main():
    vectorInput = torchhd.random(10,10000)
    print(compareVectors(vectorInput[0], vectorInput[1]))


if __name__ == "__main__":
    main()

