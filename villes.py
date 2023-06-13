import pandas as pd
import numpy as np

# read file villes.txt wiht panda
df_ville = pd.read_csv("villes.txt", delimiter = "\t")

# display the first lines
print(df_ville.head())

# remove useless columns "MAJ"
df_ville = df_ville.drop(columns = ["MAJ"])

# find INSEE's numbers codes differents
print(df_ville["Code INSEE"].unique())

# calcul average with grouby 
# average of Nom Ville
print(df_ville.groupby["Nom Ville"].mean())

# average of Code Postal
print(df_ville.groupby["Code Postal"].mean())

# average of Code INSEE
print(df_ville.groupby["Code INSEE"].mean())

# average of Code Région
print(df_ville.groupby["Code Région"].mean())

# average of Latitude
print(df_ville.groupby["Latitude"].mean())

# average of Longitude
print(df_ville.groupby["Longitude"].mean())

# average of Eloignement
print(df_ville.groupby["Eloignement"].mean())

# count the number of cities in each regions
print(df_ville["Code Région"].value_counts())

# Make a dictionary with the number of cities in each regions
dict_region = dict(df_ville["Code Région"].value_counts())




