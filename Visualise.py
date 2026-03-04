import torch
import torchhd
import numpy
import Globals
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import Checks
import VectorFunction_Brain
import WholeNetworkSocialMediaQueries
import SinglePersonSocialMediaQueries

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
    tensorList_preDict, tensorList_postDict = [], []
    pre_labels, post_labels = [], []

    for prePersId, preVect in preDict.items():
        tensorList_preDict.append(preVect)
        pre_labels.append(prePersId)

    for postPersId, postVect in postDict.items():
        tensorList_postDict.append(postVect)
        post_labels.append(postPersId)

    # Combine lists for fitting
    combined = torch.stack(tensorList_preDict + tensorList_postDict)
    # Fit PCA on unique rows (remove duplicates)
    unique_combined = torch.unique(combined, dim=0)
    pca = PCA(n_components=2)
    pca.fit(unique_combined.numpy())

    # Transform full set using the same PCA
    combined_2d = pca.transform(combined.numpy())
    split_idx = len(tensorList_preDict)
    tensorList_pre_2d = combined_2d[:split_idx]
    tensorList_post_2d = combined_2d[split_idx:]

    plt.figure(figsize=(12, 8))
    scatter1 = plt.scatter(tensorList_pre_2d[:, 0], tensorList_pre_2d[:, 1], c='blue', alpha=0.7, label='Pre Message')
    scatter2 = plt.scatter(tensorList_post_2d[:, 0], tensorList_post_2d[:, 1], c='red', alpha=0.7, label='Post Message')

    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color=color)

    add_labels(tensorList_pre_2d, pre_labels, 'darkblue')
    add_labels(tensorList_post_2d, post_labels, 'darkred')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Hypervector Visualization with Stable PCA Projection')
    plt.legend(handles=[scatter1, scatter2])
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()

def compareTwoTimePeriods():
    preDict, postDict = WholeNetworkSocialMediaQueries.getTwoTimePeriodComparison()
    tensorList_preDict, tensorList_postDict = [], []
    pre_labels, post_labels = [], []

    for prePersId, preVect in preDict.items():
        tensorList_preDict.append(preVect)
        pre_labels.append(prePersId)

    for postPersId, postVect in postDict.items():
        tensorList_postDict.append(postVect)
        post_labels.append(postPersId)

    # Combine lists for fitting
    combined = torch.stack(tensorList_preDict + tensorList_postDict)
    # Fit PCA on unique rows (remove duplicates)
    unique_combined = torch.unique(combined, dim=0)
    pca = PCA(n_components=2)
    pca.fit(unique_combined.numpy())

    # Transform full set using the same PCA
    combined_2d = pca.transform(combined.numpy())
    split_idx = len(tensorList_preDict)
    tensorList_pre_2d = combined_2d[:split_idx]
    tensorList_post_2d = combined_2d[split_idx:]

    plt.figure(figsize=(12, 8))
    scatter1 = plt.scatter(tensorList_pre_2d[:, 0], tensorList_pre_2d[:, 1], c='blue', alpha=0.7, label='Period One')
    scatter2 = plt.scatter(tensorList_post_2d[:, 0], tensorList_post_2d[:, 1], c='red', alpha=0.7, label='Period Two')

    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color=color)

    #add_labels(tensorList_pre_2d, pre_labels, 'darkblue')
    #add_labels(tensorList_post_2d, post_labels, 'darkred')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Hypervector Visualization with Stable PCA Projection')
    plt.legend(handles=[scatter1, scatter2])
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()


def idsCompareTwoTimePeriods():
    preDict, postDict = WholeNetworkSocialMediaQueries.idsGetTwoTimePeriodComparison()
    tensorList_preDict, tensorList_postDict = [], []
    pre_labels, post_labels = [], []

    for prePersId, preVect in preDict.items():
        tensorList_preDict.append(preVect)
        pre_labels.append(prePersId)

    for postPersId, postVect in postDict.items():
        tensorList_postDict.append(postVect)
        post_labels.append(postPersId)

    # Combine lists for fitting
    combined = torch.stack(tensorList_preDict + tensorList_postDict)
    # Fit PCA on unique rows (remove duplicates)
    unique_combined = torch.unique(combined, dim=0)
    pca = PCA(n_components=2)
    pca.fit(unique_combined.numpy())

    # Transform full set using the same PCA
    combined_2d = pca.transform(combined.numpy())
    split_idx = len(tensorList_preDict)
    tensorList_pre_2d = combined_2d[:split_idx]
    tensorList_post_2d = combined_2d[split_idx:]

    plt.figure(figsize=(12, 8))
    scatter1 = plt.scatter(tensorList_pre_2d[:, 0], tensorList_pre_2d[:, 1], c='blue', alpha=0.7, label='Period One')
    scatter2 = plt.scatter(tensorList_post_2d[:, 0], tensorList_post_2d[:, 1], c='red', alpha=0.7, label='Period Two')

    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color=color)

    add_labels(tensorList_pre_2d, pre_labels, 'darkblue')
    add_labels(tensorList_post_2d, post_labels, 'darkred')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Hypervector Visualization with Stable PCA Projection')
    plt.legend(handles=[scatter1, scatter2])
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()    

def idsCompareBrainTwoTimePeriods():
    preDict, postDict = SinglePersonSocialMediaQueries.idsGetBrainTwoTimePeriodComparison()
    
    tensorList_preDict, tensorList_postDict = [], []
    pre_labels, post_labels = [], []

    for prePersId, preVect in preDict.items():
        tensorList_preDict.append(preVect)
        pre_labels.append(prePersId)

    for postPersId, postVect in postDict.items():
        tensorList_postDict.append(postVect)
        post_labels.append(postPersId)

    # Combine lists for fitting
    combined = torch.stack(tensorList_preDict + tensorList_postDict)
    # Fit PCA on unique rows (remove duplicates)
    unique_combined = torch.unique(combined, dim=0)
    pca = PCA(n_components=2)
    pca.fit(unique_combined.numpy())

    # Transform full set using the same PCA
    combined_2d = pca.transform(combined.numpy())
    split_idx = len(tensorList_preDict)
    tensorList_pre_2d = combined_2d[:split_idx]
    tensorList_post_2d = combined_2d[split_idx:]

    plt.figure(figsize=(12, 8))
    scatter1 = plt.scatter(tensorList_pre_2d[:, 0], tensorList_pre_2d[:, 1], c='blue', alpha=0.7, label='Period One')
    scatter2 = plt.scatter(tensorList_post_2d[:, 0], tensorList_post_2d[:, 1], c='red', alpha=0.7, label='Period Two')

    def add_labels(points, labels, color):
        for (x, y), label in zip(points, labels):
            plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, color=color)

    add_labels(tensorList_pre_2d, pre_labels, 'darkblue')
    add_labels(tensorList_post_2d, post_labels, 'darkred')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Hypervector Visualization with Stable PCA Projection')
    plt.legend(handles=[scatter1, scatter2])
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()    