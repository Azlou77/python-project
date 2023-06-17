import pandas as pd
import numpy as np

# Read file villes.txt wiht panda with delimiters: spaces, no header and point as decimal separator
df_ville = pd.read_csv("villes.txt", delimiter = "\t", decimal = ".")


# Add column names
df_ville.columns = ["Nom Ville", "MAJ", "Code Postal", "Code INSEE", "Code Région", "Latitude", "Longitude", "Eloignement"]


# Remove the colum "MAJ" because it's not useful
df_ville = df_ville.drop(columns = ["MAJ"])



# Display the first 5 rows
print(df_ville.head())


# Identify duplicate data in Pandas DataFrame in column "Code INSEE"
duplicateRowsDF = df_ville[df_ville.duplicated(["Code INSEE"])]

# Display duplicate data in Pandas DataFrame
print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')


# calcul average, the number and the maximum for each variable numeric
print(df_ville.describe())

# Count the number of cities per region
print(df_ville.groupby("Code Région").size())

# Make a dictionary with the number of cities per region
dict_nb_ville = df_ville.groupby("Code Région").size().to_dict()
print(dict_nb_ville)
















