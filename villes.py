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

# count the number of cities in each regions
print(df_ville["Code Région"].value_counts())

# Make a dictionary with the number of cities in each regions
dict_region = dict(df_ville["Code Région"].value_counts())




