import pandas as pd
import numpy as np

# Read file villes.txt wiht panda with delimiters: spaces, no header and point as decimal separator
df_ville = pd.read_csv("villes.txt", delimiter = "\t", header = None, decimal = ".")


# Remove useless columns "MAJ"
df_ville = df_ville.drop(columns = [6])

# Remove duplicate data  in Pandas DataFrame
df_ville = df_ville.drop_duplicates(
    subset = [0, 1, 2, 3, 4, 5],
    keep = "first"

)

# Rename columns
df_ville = df_ville.rename(columns = {
    0: "Nom Ville",
    1: "Code Postal",
    2: "Code INSEE",
    3: "Code Région",
    4: "Latitude",
    5: "Longitude",
    7: "Eloignement"
})

# Display the first 5 rows
print(df_ville.head())







# # find INSEE's numbers codes differents
# print(df_ville["Code INSEE"].unique())

# # calcul average with grouby 
# # average of Nom Ville
# print(df_ville.groupby["Nom Ville"].mean())

# # average of Code Postal
# print(df_ville.groupby["Code Postal"].mean())

# # average of Code INSEE
# print(df_ville.groupby["Code INSEE"].mean())

# # average of Code Région
# print(df_ville.groupby["Code Région"].mean())

# # average of Latitude
# print(df_ville.groupby["Latitude"].mean())

# # average of Longitude
# print(df_ville.groupby["Longitude"].mean())

# # average of Eloignement
# print(df_ville.groupby["Eloignement"].mean())

# # count the number of cities in each regions
# print(df_ville["Code Région"].value_counts())

# # Make a dictionary with the number of cities in each regions
# dict_region = dict(df_ville["Code Région"].value_counts())




