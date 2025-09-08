import torch
import torchhd
import numpy
import Globals
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import Checks
import VectorFunction_Brain

def visualiseAllPersons_brain():
    # Get a list of all persons who have a hypervector bundle assigned to them
    persList = []
    tensorList = []
    for persId, persObj in Globals.personDict.items():
        if not isinstance(persObj.persBundle, str):
            persList.append(persObj)
            if not isinstance(persObj.persBundle, str):
                tensorList.append(persObj.persBundle)
    
    combinedTensor = torch.stack(tensorList)
    labels = []

    for personObj in persList:
        persBundle = personObj.persBundle
        labels.append(personObj.id)
   
    # combine vectors and reduce dimemsionality to 2d
    pca = PCA(n_components=2)
    hvs_2d = pca.fit_transform(combinedTensor.numpy())

    # Create plot with labels 
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(hvs_2d[:, 0], hvs_2d[:, 1], s=100)

    for i, (x, y) in enumerate(hvs_2d):
        plt.annotate(
            labels[i],
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=12,
            arrowprops=dict(arrowstyle="->", color='gray', alpha=0.6)
        )

    plt.title("2D Visualization of Hypervectors", fontsize=14)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(alpha=0.2)
    plt.show()

def visualiseAllPersons_sm():
    # Get a list of all persons who have a hypervector bundle assigned to them
    persList = []
    tensorList = []
    for persId, persObj in Globals.personDict.items():
        if not isinstance(persObj.smBundle, str):
            persList.append(persObj)
            if not isinstance(persObj.smBundle, str):
                tensorList.append(persObj.smBundle)
    
    combinedTensor = torch.stack(tensorList)
    labels = []

    for personObj in persList:
        persBundle = personObj.smBundle
        labels.append(personObj.id)

        
    # combine vectors and reduce dimemsionality to 2d
    pca = PCA(n_components=2)
    hvs_2d = pca.fit_transform(combinedTensor.numpy())

    # Create plot with labels 
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(hvs_2d[:, 0], hvs_2d[:, 1], s=100)

    for i, (x, y) in enumerate(hvs_2d):
        plt.annotate(
            labels[i],
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=12,
            arrowprops=dict(arrowstyle="->", color='gray', alpha=0.6)
        )

    plt.title("2D Visualization of Hypervectors", fontsize=14)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(alpha=0.2)
    plt.show()

def compareAllPersonsBrainVsSm():
    # Get a list of all persons who have a hypervector bundle assigned to them
    persList = []
    tensorList_brain = []
    tensorList_sm = []
    labelList = []
    for persId, persObj in Globals.personDict.items():
        if not isinstance(persObj.persBundle, str):
            if not isinstance(persObj.smBundle, str):
                persList.append(persObj)
                tensorList_brain.append(persObj.persBundle)
                tensorList_sm.append(persObj.smBundle)
                labelList.append(persObj.id)
    
    # Make combinedList
    comList = []
    #add all items into comList
    for item in tensorList_brain:
        comList.append(item)
    

    
    for item in tensorList_sm:
        comList.append(item)


    # Combine and convert to numpy
    combined = torch.stack(comList)

    pca = PCA(n_components=2)
    combined_2d = pca.fit_transform(combined.numpy())

    # Split reduced vectors
    split_idx = len(tensorList_brain)
    tensorList_brain_2d = combined_2d[:split_idx]
    tensorList_sm_2d = combined_2d[split_idx:]

    # Create plot
    plt.figure(figsize=(12, 8))
    scatter1 = plt.scatter(tensorList_brain_2d[:, 0], tensorList_brain_2d[:, 1], c='blue', alpha=0.7, label='Brain Data')
    scatter2 = plt.scatter(tensorList_sm_2d[:, 0], tensorList_sm_2d[:, 1], c='red', alpha=0.7, label='Social Media Data')

    # Add labels with text positioning
    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(
                label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 7),
                ha='center',
                fontsize=9,
                color=color,
                arrowprops=dict(arrowstyle="-", color=color, alpha=0.3)
            )

    add_labels(tensorList_brain_2d, labelList, 'darkblue')
    add_labels(tensorList_sm_2d, labelList, 'darkred')

    plt.xlabel('Principal Component 1', fontsize=12)
    plt.ylabel('Principal Component 2', fontsize=12)
    plt.title('Hypervector Visualization with Custom Labels', pad=20)
    plt.legend(handles=[scatter1, scatter2], loc='best')
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()

# Visualise changes to vectors
def visualiseCauseEffect(preDict, postDict):
    # Expected format is id : vector for Dicts
    
    # Make lists
    preList = []
    postList = []
    labelList = []
    comList = []

    for id, vector in preDict.items():
        labelList.append(id)
        preList.append(vector)
        comList.append(vector)

    for id, vector in postDict.items():
        labelList.append(id)
        postList.append(vector)
        comList.append(vector)



    # Combine and convert to numpy
    combined = torch.stack(comList)

    pca = PCA(n_components=2)
    combined_2d = pca.fit_transform(combined.numpy())

    # Split reduced vectors
    split_idx = len(preList)
    preList_2d = combined_2d[:split_idx]
    postList_2d = combined_2d[split_idx:]

    # Create plot
    plt.figure(figsize=(12, 8))
    scatter1 = plt.scatter(preList_2d[:, 0], preList_2d[:, 1], c='blue', alpha=0.7, label='Pre-Changes')
    scatter2 = plt.scatter(postList_2d[:, 0], postList_2d[:, 1], c='red', alpha=0.7, label='Post Changes')

    # Add labels with text positioning
    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(
                label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 7),
                ha='center',
                fontsize=9,
                color=color,
                arrowprops=dict(arrowstyle="-", color=color, alpha=0.3)
            )

    add_labels(preList_2d, labelList, 'darkblue')
    add_labels(postList_2d, labelList, 'darkred')

    plt.xlabel('Principal Component 1', fontsize=12)
    plt.ylabel('Principal Component 2', fontsize=12)
    plt.title('Hypervector Visualization with Custom Labels', pad=20)
    plt.legend(handles=[scatter1, scatter2], loc='best')
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()


def visualiseAllPersons_sm_RD():
    # visualisation of the republican and democrat datasets
    demNameList = []
    repNameList = []
    demTensorList = []
    repTensorList = []

    for persId, persObj in Globals.personDict.items():
        if not isinstance(persObj.smBundle, str):
            if "D" in persObj.id:
                demNameList.append(persObj)
                demTensorList.append(persObj.smBundle)
            elif "R" in persObj.id:
                repNameList.append(persObj)
                repTensorList.append(persObj.smBundle)

    # Combine tensor lists for PCA
    comList = demTensorList + repTensorList

    # Reduce via PCA
    combined = torch.stack(comList)
    pca = PCA(n_components=2)
    combined_2d = pca.fit_transform(combined.numpy())

    # Split back to two sets
    split_idx = len(demTensorList)
    demTensorList_2d = combined_2d[:split_idx]
    rebTensorList_2d = combined_2d[split_idx:]

    # Labels
    demLabels = [p.id for p in demNameList]
    rebLabels = [p.id for p in repNameList]

    plt.figure(figsize=(12, 8))
    scatter_dem = plt.scatter(demTensorList_2d[:, 0], demTensorList_2d[:, 1], c='blue', alpha=0.7, label='Dem')
    scatter_reb = plt.scatter(rebTensorList_2d[:, 0], rebTensorList_2d[:, 1], c='red', alpha=0.7, label='Reb')

    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(
                label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 7),
                ha='center',
                fontsize=9,
                color=color,
                arrowprops=dict(arrowstyle="-", color=color, alpha=0.3)
            )

    add_labels(demTensorList_2d, demLabels, 'darkblue')
    add_labels(rebTensorList_2d, rebLabels, 'darkred')

    plt.xlabel('Principal Component 1', fontsize=12)
    plt.ylabel('Principal Component 2', fontsize=12)
    plt.title('Dem vs Rep Tensor Visualization (PCA)', pad=20)
    plt.legend(handles=[scatter_dem, scatter_reb], loc='best')
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()

def visualiseTopicAll_sm_RD():
    # visualisation of the republican and democrat datasets based on a topic

    print("----------------------------------------")
    print("What are the strongest feelings the network has about a topic?")
    print("----------------------------------------")
    # COllect inputs
    wordOne= input("Give word: ")
    print("You input: " + wordOne)
    
   
    print("----------------------------------------")
    print(f'Checking inputs...')
    
    # Convert words to lower case
    wordOne = wordOne.lower()

    # General error check of inputs
    if not Checks.checkAtomicExists(wordOne):
        print(f'{wordOne} does not exist')
        return
    
    wordVect = VectorFunction_Brain.getAtomicVector_fromLabel(wordOne)
    demNameList = []
    repNameList = []
    demTensorList = []
    repTensorList = []

    for persId, persObj in Globals.personDict.items():
        if not isinstance(persObj.smBundle, str):
            bindNameList, bindUniqueNum, bindTotalNum = VectorFunction_Brain.getNumInstances_atomic(persObj.smBundle,wordVect )
            if bindTotalNum > 0:
                if "D" in persObj.id:
                    for bindName in bindNameList:
                        demNameList.append(bindName)
                        nameVector = VectorFunction_Brain.getPairVector_fromLabel(bindName)
                        demTensorList.append(nameVector)
                elif "R" in persObj.id:
                    for bindName in bindNameList:
                        repNameList.append(bindName)
                        nameVector = VectorFunction_Brain.getPairVector_fromLabel(bindName)
                        repTensorList.append(nameVector)

    # Combine tensor lists for PCA
    comList = demTensorList + repTensorList

    # Reduce via PCA
    combined = torch.stack(comList)
    pca = PCA(n_components=2)
    combined_2d = pca.fit_transform(combined.numpy())

    # Split back to two sets
    split_idx = len(demTensorList)
    demTensorList_2d = combined_2d[:split_idx]
    rebTensorList_2d = combined_2d[split_idx:]

    # Labels
    demLabels = [p for p in demNameList]
    rebLabels = [p for p in repNameList]

    plt.figure(figsize=(12, 8))
    scatter_dem = plt.scatter(demTensorList_2d[:, 0], demTensorList_2d[:, 1], c='blue', alpha=0.7, label='Dem')
    scatter_reb = plt.scatter(rebTensorList_2d[:, 0], rebTensorList_2d[:, 1], c='red', alpha=0.7, label='Reb')

    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(
                label,
                (x, y),
                textcoords="offset points",
                xytext=(0, 7),
                ha='center',
                fontsize=9,
                color=color,
                arrowprops=dict(arrowstyle="-", color=color, alpha=0.3)
            )

    add_labels(demTensorList_2d, demLabels, 'darkblue')
    add_labels(rebTensorList_2d, rebLabels, 'darkred')

    plt.xlabel('Principal Component 1', fontsize=12)
    plt.ylabel('Principal Component 2', fontsize=12)
    plt.title('Dem vs Reb Tensor Visualization (PCA)', pad=20)
    plt.legend(handles=[scatter_dem, scatter_reb], loc='best')
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()



