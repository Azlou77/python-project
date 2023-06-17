import pandas as pd
import numpy as np

# Read file villes.txt wiht panda with delimiters: spaces, no header and point as decimal separator
df_ville = pd.read_csv("villes.txt", delimiter = "\t", decimal = ".")

# Add column names
df_ville.columns = ["Nom Ville", "MAJ", "Code Postal", "Code INSEE", "Code Région", "Latitude", "Longitude", "Eloignement"]


# Remove the colum "MAJ" because it's not useful
df_ville = df_ville.drop(columns = ["MAJ"])


# Identify duplicate data in Pandas DataFrame in column "Code INSEE"
duplicateRowsDF = df_ville[df_ville.duplicated(["Code INSEE"])]

# Display duplicate data in Pandas DataFrame
print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')





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



# Display the first 5 rows
print(df_ville.head())








# # count the number of cities in each regions
# print(df_ville["Code Région"].value_counts())

# # Make a dictionary with the number of cities in each regions
# dict_region = dict(df_ville["Code Région"].value_counts())




