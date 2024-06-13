import pandas as pd
import torch
import csv
import torchhd

recipes_data = pd.read_csv("Recipes_with_origin.csv").iloc[:, 2:]

ingredients = []
recipes = {}
regions = []

with open("Recipes_with_origin.csv") as recipeCSV:
    csv_reader = csv.reader(recipeCSV, delimiter=',')
    lineCount = 0
    columnCount = 1
    
    for row in csv_reader:
        if lineCount == 0:
            for item in row:
                if columnCount < 383 and columnCount != 1:
                    ingredients.append(item)
                elif columnCount >= 383:
                    regions.append(item)
                columnCount = columnCount + 1
            
        else:
            columnCount = 1
            ing_array = []
            reg_array = []
            for item in row:
                if columnCount == 1 :
                    key = item
                elif columnCount < 383 and columnCount != 1:
                    ing_array.append(item)
                else:
                    reg_array.append(item)
                columnCount = columnCount + 1
            recipes[key] = ing_array, reg_array
        lineCount = lineCount + 1
        columnCount = 1

d = 10000
vector_ingredients = torchhd.random(len(ingredients))

ingredientDict = {}
count = 0
for ingred in ingredients:
    ingredientDict[ingred] = vector_ingredients[count]
    count = count + 1



Xingr = torch.eye(len(ingredients))

Xrec = torch.sign(recipes @ Xingr)

recipes_hdv = torch.sign(Xrec.sum(dim=0))

Xorigin = origins.T @ Xrec
Xorigin = torch.sign(Xorigin)

C_or = Xorigin @ Xorigin.T

origin_df = pd.DataFrame(C_or.numpy(), columns=["origin"] + list(regions))

top10 = lambda x: sorted(x, key=lambda y: y[1], reverse=True)[:10]

region_ingr_df = pd.DataFrame({r: top10([(ingr, torch.cosine_similarity(Xingr[i], Xorigin[j]).item()) for i, ingr in enumerate(ingredients)]) for j, r in enumerate(regions)}, index=ingredients)

def embed_ingr(ingr):
    return Xingr[ingr2ind[ingr]]

def encode_recipe(recipe):
    return torch.stack([embed_ingr(ingr) for ingr in recipe])

my_recipe_hdv = encode_recipe(["wine", "butter", "lemon peel", "chicken", "black pepper", "cheese"])

torch.cosine_similarity(my_recipe_hdv.mean(dim=0), recipes_hdv)

rand_ingr = recipes_data.sample(5, axis=1).columns[:-11]

fake_rec_hdv = encode_recipe(rand_ingr)

torch.cosine_similarity(fake_rec_hdv.mean(dim=0), recipes_hdv)

top10(zip(regions, Xorigin @ my_recipe_hdv.mean(dim=0)))

top10([(ingr, torch.cosine_similarity(recipes_hdv, Xingr[i] * my_recipe_hdv.mean(dim=0)).item()) for i, ingr in enumerate(ingredients)])