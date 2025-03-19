import torch
import torchhd
import numpy
import Globals
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def visualiseAllPersons_brain():
    # Get a list of all persons who have a hypervector bundle assigned to them
    persList = []
    tensorList = []
    for persId, persObj in Globals.personDict.items():
        if not isinstance(persObj.persBundle, int):
            persList.append(persObj)
            if not isinstance(persObj.persBundle, int):
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
        if not isinstance(persObj.smBundle, int):
            persList.append(persObj)
            if not isinstance(persObj.smBundle, int):
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